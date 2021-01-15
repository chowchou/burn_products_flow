import binascii
import re
import time
# import binascii
import traceback

import func_timeout
from PyQt5.QtCore import QThread, pyqtSignal
import serial
import public_var
import Listeners_thread

class Port_down(QThread):
    _signal = pyqtSignal(dict)

    def __init__(self,id):
        super(Port_down, self).__init__()
        self.id = id
        self.ser_flag = False
        self.rep_order = 'ED 00 08 03 CF 00 00 00 FF FF D0 EE'
        self.recv_flag = True
        self.test_flag = False
        self.check_crc32 = ''
        self.dev_reply = 'ED000883CF000000FFFF50EE'
        self.db_res = ''

    def check_com_port(self):
        com_port = public_var.com_port.split(",")
        bps = public_var.bps
        port = 'COM' + com_port[self.id]
        if not self.ser_flag:
            try:
                self.ser = serial.Serial(port, bps, timeout=0.01)
                obj_write_info = binascii.a2b_hex(self.rep_order.replace(" ", ""))
                time.sleep(2)
                self.ser.write(obj_write_info)
                self.ser_flag = True
                a = {'id': self.id, 'ser_flag': True, 'mes_type': '1'}
                self._signal.emit(a)
                # for i in range(20):
                #     time.sleep(1)
                #     if self.ser.inWaiting():
                #         res = self.ser.readall().hex().upper()
                #         print('<端口测试/固件下载>接收:',res)
                #         obj_write_info = binascii.a2b_hex(self.rep_order.replace(" ", ""))
                #         self.ser.write(obj_write_info)
                #         self.ser_flag = True
                #         a = {'id': self.id, 'ser_flag': True,'mes_type':'1'}
                #         self._signal.emit(a)
                #         return True
                #     else:
                #         print('底板无上送数据，请检测')
                #         self.ser_flag = False
                #         a = {'id': self.id, 'ser_flag': False,'err':'F101','mes_type':'1'}
                #         self._signal.emit(a)
                #         return False
            except Exception as e:
                print(e,'错误')
                a = {'id': self.id, 'ser_flag': False , 'err':'F100','mes_type':'1'}
                self._signal.emit(a)
                return False
        # else:

    def sup_num(self,data,num):
        # hex补充命令长度
        sup_over = str(data).replace('0x', '')
        sup_over = sup_over.rjust(num, '0').upper()
        sup_over = re.findall(".{2}", sup_over)
        sup_over = " ".join(sup_over)
        return sup_over

    def count_checknum(self,data):
        check_id = "%.2x" % (sum([int(sn, 16) for sn in data.split(" ")]) % 256)
        return check_id.upper()

    def send_signal(self,id,data,num):
        a = {'id':id, 'mes_type': str(num), 'mess': str(data)}
        self._signal.emit(a)

    def send_bin(self):
        self.rate = 0
        self.send_signal(self.id,'bin文件开始下载，请稍等！',2)
        bin_src = public_var.bin_src
        with open(bin_src, 'rb') as f:
            dblst = f.read()
        bin_length = hex(len(dblst))
        # 00 06 be 94
        sup_binlenth = self.sup_num(bin_length,8)
        print(sup_binlenth)
        order_crc32 = binascii.crc32(dblst)
        sup_crc32 = self.sup_num(hex(order_crc32),8)
        print(sup_crc32)
        self.check_crc32 = sup_crc32.replace(' ','')
        joint_order = '03 0D 00 00 00 01 ' + sup_binlenth +' ' + sup_crc32
        print(joint_order)
        check_id = self.count_checknum(joint_order)
        start_send = 'ED 00 0F %s %s EE' %(joint_order,check_id)
        print(start_send)
        # obj_write_info = binascii.a2b_hex(start_send.replace(" ", ""))
        # self.ser.write(obj_write_info)
        ws = self.port_write(start_send)
        print(ws)
        if ws:
            print('启动成功，准备发送文件')
        else:
            return

        for i in range(int(len(dblst) / 1024) + 1):
            self.rate = int(((i + 1) / (int(len(dblst) / 1024) + 1)) * 100)
            res = dblst[i * 1024:(i + 1) * 1024]
            alf_res = res.hex().upper()
            res = re.findall(".{2}", alf_res)
            res = " ".join(res)
            # print(res)
            res_length = int(len(alf_res)/2)
            order_res_length = self.sup_num(hex(res_length),4)
            # print(order_res_length)
            count_orders = '03 0D 00 00 00 04 '+ order_res_length + ' ' + res
            # print(count_orders)
            check_ids = self.count_checknum(count_orders)
            addc = count_orders + ' ' +check_ids
            addc = addc.replace(" ", "")
            addc_length = int(len(addc) / 2)
            cf = self.sup_num(hex(addc_length), 4)
            last_order = 'ED' + cf + addc + 'EE' #整合命令帧
            print(last_order)
            send_oo = self.port_write_t(last_order,self.rate)
            print(send_oo)
            if send_oo and self.rate != 100:
                a = {'id': self.id,'mes_type':'5','rate':self.rate}
                self._signal.emit(a)
                self.port_write(self.rep_order)
            if send_oo and self.rate == 100:
                a = {'id': self.id, 'mes_type': '5', 'rate': self.rate}
                self._signal.emit(a)
                self.port_write(self.rep_order)
                if self.check_crc32 in send_oo:
                    self.send_signal(self.id, 'bin下载完成！', 2)
                    return True
                else:
                    self.send_signal(self.id, 'bin下载失败！', 3)
                    return False

            # break

    def dev_id(self):
        # pass
        sname = 'dev_' + str(self.id)
        dev_value = public_var.dev_id.get(sname)
        sup_over = re.findall(".{2}", dev_value)
        sup_over = " ".join(sup_over)
        prefix = 'ED 00 0D '
        devId_len = '03 02 00 00 00 01 ' + sup_over
        check_id = "%.2x" % (sum([int(sn, 16) for sn in devId_len.split(" ")]) % 256)
        last_devid_order = prefix + devId_len + check_id + 'EE'
        res = self.port_write(last_devid_order)
        print(res)
        if dev_value in res:
            message = '工装ID写入成功：'+str(dev_value)
            self.send_signal(self.id, message, 2)
            self.port_write(self.rep_order)
            return True
        else:
            self.send_signal(self.id, '工装ID写入失败！', 3)
            self.port_write(self.rep_order)
            return False

    def port_write(self,data):
        obj_write_info = binascii.a2b_hex(data.replace(" ", ""))
        self.ser.write(obj_write_info)
        time.sleep(0.2)
        for i in range(20):
            if self.ser.inWaiting():
                self.bin_res = self.ser.read_all().hex().upper()
                # print(res)
        return self.bin_res

    def port_write_t(self,data,num):
        print(num)
        obj_write_info = binascii.a2b_hex(data.replace(" ", ""))
        self.ser.write(obj_write_info)
        time.sleep(0.2)
        for i in range(200):
            if self.ser.inWaiting():
                self.bin_res = self.ser.read_all().hex().upper()
                if num == 100:
                    if self.bin_res != self.dev_reply:
                        return self.bin_res
                    else:
                        pass
                else:
                    return self.bin_res

    def check_downs(self):
        while True:
            if self.ser.inWaiting():
                self.db_res = self.ser.readall().hex().upper()
                print(self.db_res)
            if self.db_res != self.dev_reply:
                return self.db_res

    # def tools(self,datas):
    #     arguments = re.findall(".{2}", datas)
    #     arguments = " ".join(arguments)
    #     return arguments
    #
    # def write_tool(self,datas):
    #     obj_write_info = binascii.a2b_hex(datas.replace(" ", ""))
    #     self.ser.write(obj_write_info)
    #     time.sleep(0.5)
    #     while True:
    #         if self.ser.inWaiting():
    #             res = self.ser.readall().hex().upper()
    #             print(res)
    #             if res != self.dev_reply:
    #                 return res

    def run_all(self):
        self.check_com_port() # open port
        if not self.ser_flag:
            return
        res = self.dev_id() # write devid
        if not res:
            return
        if public_var.burn_flag: # burn
            res = self.send_bin()
            if not res:
                return
        else:
            self.send_signal(self.id, '当前模式：无烧录！', 2)
        public_var.third_step = True

    def run(self):
        print('端口检测、下载固件线程启动')
        try:
            self.run_all()
        except Exception as e:
            print(e)
            traceback.print_exc()
        finally:
            print('端口检测、下载固件线程结束')
            if self.ser_flag:
                self.ser.close()
            return
