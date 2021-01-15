import binascii
import re
import time
# import binascii
import func_timeout
from PyQt5.QtCore import QThread, pyqtSignal
import serial
import public_var
import Listeners_thread

class Prod_test(QThread):
    _signal = pyqtSignal(dict)

    def __init__(self,id,sn):
        super(Prod_test, self).__init__()
        self.id = id
        self.ser_flag = False
        self.rep_order = 'ED 00 08 03 CF 00 00 00 FF FF D0 EE'
        self.recv_flag = True
        self.test_flag = False
        self.check_crc32 = ''
        self.dev_reply = 'ED000883CF000000FFFF50EE'
        self.sn = sn

    def check_com_port(self):

        com_port = public_var.com_port.split(",")
        bps = public_var.bps
        # print(com_port)
        port = 'COM' + com_port[self.id]
        if not self.ser_flag:
            try:
                self.ser = serial.Serial(port, bps, timeout=0.01)
                self.ser_flag = True
                # for i in range(20):
                #     time.sleep(1)
                #     if self.ser.inWaiting():
                #         res = self.ser.readall().hex().upper()
                #         print(res,'接收')
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

    def port_write(self,data):
        obj_write_info = binascii.a2b_hex(data.replace(" ", ""))
        self.ser.write(obj_write_info)
        time.sleep(0.3)
        for i in range(30):
            if self.ser.inWaiting():
                self.bin_res = self.ser.readall().hex().upper()
                # print(res)
                break
            # time.sleep(0.1)
        return self.bin_res

    def port_write_1(self,data):
        obj_write_info = binascii.a2b_hex(data.replace(" ", ""))
        print('停电上报发送', data)
        self.ser.write(obj_write_info)
        time.sleep(8)
        for i in range(50):
            if self.ser.inWaiting():
                self.p_bin_res = self.ser.readall().hex().upper()
                print('停电上报接收',self.p_bin_res)
            # time.sleep(0.1)
        return self.p_bin_res


    def tools(self,datas):
        arguments = re.findall(".{2}", datas)
        arguments = " ".join(arguments)
        return arguments

    def write_tool(self,datas):
        obj_write_info = binascii.a2b_hex(datas.replace(" ", ""))
        print('write_tool发送', datas)
        self.ser.write(obj_write_info)
        while True:
            res = self.ser.readall().hex().upper()
            if res != self.dev_reply and res:
                print('write_tool接收', res)
                return res
            # if self.ser.in_waiting():
            #     res = self.ser.readall().hex().upper()
            #     print('write_tool接收',res)
            #     if res != self.dev_reply:
            #         return res
            # time.sleep(0.2)

    def check_version(self):
        self.send_signal(self.id, '版本号验证开始！', 2)
        prefix = 'ED 00 0F '
        middle = '03 04 00 00 00 04 '
        soft_ver = public_var.config_dict.get('21')
        ver = public_var.config_dict.get('22')
        arguments = ver + soft_ver
        arguments = self.tools(arguments)
        cs_num = middle + arguments
        cs = self.count_checknum(cs_num)
        last_order = prefix + cs_num + cs + 'EE'
        res = self.port_write(last_order)
        if res == self.dev_reply:
            print('参数设置成功，启动测试')
        else:
            print('参数设置失败')
            return False
        start_check = 'ED 00 07 03 04 00 00 00 01 08 EE'
        res = self.write_tool(start_check)
        self.port_write(self.rep_order)
        res = res.replace(self.dev_reply,'')
        if res[18:20] == '01':
            self.send_signal(self.id, '版本号验证结束！pass', 2)
            # self.port_write(self.rep_order)
            return True
        else:
            self.send_signal(self.id, '版本号验证结束！fail', 3)
            # self.port_write(self.rep_order)
            return False

    def communication_test(self):

        self.send_signal(self.id, '通讯验证开始！', 2)
        prefix = 'ED 00 95 '
        middle = '03 05 00 00 00 04 '
        arguments = self.tools(public_var.end_order)
        cs_num = middle + arguments
        cs = self.count_checknum(cs_num)
        last_order = prefix + cs_num + cs + 'EE'
        res = self.port_write(last_order)
        if res == self.dev_reply:
            print('参数设置成功，启动测试')
        else:
            print('参数设置失败')
            return False
        start_check = 'ED 00 07 03 05 00 00 00 01 09 EE'
        res = self.write_tool(start_check)
        self.port_write(self.rep_order)
        res = res.replace(self.dev_reply, '')
        if res[18:20] == '01':
            self.send_signal(self.id, '通讯验证结束！pass', 2)
            # self.port_write(self.rep_order)
            return True
        else:
            self.send_signal(self.id, '通讯验证结束！fail', 3)
            # self.port_write(self.rep_order)
            return False


    def check_pinVoltage(self):
        self.send_signal(self.id, 'pin，电压验证开始！', 2)
        prefix = 'ED 00 17 '
        middle = '03 03 00 00 00 04 '
        arguments = []
        config_value = []
        config_key = [1, 2, 3, 4, 9, 10, 7, 8]
        for i in config_key:
            num = public_var.config_dict.get(str(i))
            config_value.append(num)
        for i in config_value:
            if '.' not in i:
                i = i + '.'
            # print(i, '*' * 30)
            # 整数
            num_i = i[0:i.rfind('.')].rjust(2, '0')
            arguments.append(num_i)
            # 小数
            num_f = i[i.rfind('.') + 1:].ljust(2, '0')
            arguments.append(num_f)
        new_arg = " ".join(arguments)
        cs_num = middle + new_arg
        cs = self.count_checknum(cs_num)
        last_order = prefix + cs_num + cs + 'EE'
        # print(last_order)
        res = self.port_write(last_order)
        if res == self.dev_reply:
            print('PIN参数设置成功，启动测试')
        else:
            print('PIN参数设置失败')
            return False
        start_check = 'ED 00 07 03 03 00 00 00 01 07 EE'
        res = self.write_tool(start_check)
        self.port_write(self.rep_order)
        res = res.replace(self.dev_reply, '')
        if res[18:20] == '01':
            self.send_signal(self.id, 'pin，电压验证结束！pass', 2)
            return True
        else:
            self.send_signal(self.id, 'pin，电压验证结束！fail', 3)
            return False

    def check_offset(self):
        self.send_signal(self.id, '频偏验证开始！', 2)
        prefix = 'ED 00 09 '
        middle = '03 06 00 00 00 04 '
        min_set = public_var.config_dict.get('15')
        max_set = public_var.config_dict.get('16')
        before = [int(min_set),int(max_set)]
        f1 = lambda d: "%.2X" %(int(256-abs(d))) if (d<0) else "%.2X" %(d)
        after = []
        for i in before:
            after.append(f1(i))
        new_arg = " ".join(after)
        cs_num = middle + new_arg
        cs = self.count_checknum(cs_num)
        last_order = prefix + cs_num + cs + 'EE'
        print(last_order)
        res = self.port_write(last_order)
        if res == self.dev_reply:
            print('频偏参数设置成功，启动测试')
        else:
            print('频偏参数设置失败')
            return False
        start_check = 'ED 00 07 03 06 00 00 00 01 0A EE'
        res = self.write_tool(start_check)
        self.port_write(self.rep_order)
        res = res.replace(self.dev_reply, '')
        if res[18:20] == '01':
            self.send_signal(self.id, '频偏验证结束！pass', 2)
            return True
        else:
            self.send_signal(self.id, '频偏验证结束！fail', 3)
            return False

    def zero_circuit(self):
        self.send_signal(self.id, '过零电路验证开始！', 2)
        start_check = 'ED 00 07 03 08 00 00 00 01 0C EE'
        res = self.write_tool(start_check)
        self.port_write(self.rep_order)
        res = res.replace(self.dev_reply, '')
        if res[18:20] == '01':
            self.send_signal(self.id, '过零电路验证结束！pass', 2)
            return True
        else:
            self.send_signal(self.id, '过零电路验证结束！fail', 3)
            return False

    def power_consumption(self):
        self.send_signal(self.id, '功耗验证开始！', 2)
        prefix = 'ED 00 0F '
        middle = '03 07 00 00 00 04 '
        arguments = []
        config_value = []
        config_key = [17, 18, 19, 20,]
        for i in config_key:
            num = public_var.config_dict.get(str(i))
            config_value.append(num)
        for i in config_value[0:2]:
            num_i = i.ljust(4, '0')
            arguments.append(num_i)
        for i in config_value[2:]:
            num_i = i.rjust(4, '0')
            arguments.append(num_i)
        new_arg = "".join(arguments)
        # sup_over = re.findall(".{2}", new_arg)
        # sup_over = " ".join(sup_over)
        new_arg = self.tools(new_arg)
        cs_num = middle + new_arg
        cs = self.count_checknum(cs_num)
        last_order = prefix + cs_num + cs + 'EE'
        print(last_order)
        res = self.port_write(last_order)
        if res == self.dev_reply:
            print('功耗参数设置成功，启动测试')
        else:
            print('功耗参数设置失败')
            return False
        start_check = 'ED 00 07 03 07 00 00 00 01 0B EE'
        res = self.write_tool(start_check)
        self.port_write(self.rep_order)
        res = res.replace(self.dev_reply, '')
        if res[18:20] == '01':
            self.send_signal(self.id, '功耗验证结束！pass', 2)
            return True
        else:
            self.send_signal(self.id, '功耗验证结束！fail', 3)
            return False

    def power_report(self):
        self.send_signal(self.id, '停电上报验证开始！', 2)
        prefix = 'ED 00 0F '
        middle = '03 0A 00 00 00 04 '
        arguments = []
        config_value = []
        config_key = [5, 6, 11, 12,]
        for i in config_key:
            num = public_var.config_dict.get(str(i))
            config_value.append(num)
        for i in config_value:
            if '.' not in i:
                i = i + '.'
            # 整数
            num_i = i[0:i.rfind('.')].rjust(2, '0')
            arguments.append(num_i)
            # 小数
            num_f = i[i.rfind('.') + 1:].ljust(2, '0')
            arguments.append(num_f)
        new_arg = " ".join(arguments)
        cs_num = middle + new_arg
        cs = self.count_checknum(cs_num)
        last_order = prefix + cs_num + cs + 'EE'
        # print(last_order)
        res = self.port_write(last_order)
        if res == self.dev_reply:
            print('停电上报参数设置成功，启动测试')
        else:
            print('停电上报参数设置失败')
            return False
        start_check = 'ED 00 07 03 0A 00 00 00 01 0E EE'
        res = self.port_write_1(start_check)
        self.port_write(self.rep_order)
        if res[18:20] == '01':
            self.send_signal(self.id, '停电上报验证结束！pass', 2)
            return True
        else:
            self.send_signal(self.id, '停电上报验证结束！fail', 3)
            return False

    def wirte_snid(self):
        self.send_signal(self.id, '读写ID开始验证！', 2)
        prefix = 'ED 00 33 '
        middle = '03 0B 00 00 00 01 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 '
        # self.send_signal(self.id, '请扫码！', 2)
        # sn = input()
        sn = self.tools(self.sn)
        cs_num = middle + sn
        cs = self.count_checknum(cs_num)
        start_check = prefix + cs_num + cs + 'EE'
        res = self.write_tool(start_check)
        self.port_write(self.rep_order)
        res = res.replace(self.dev_reply, '')
        if res[18:20] == '01':
            self.send_signal(self.id, '读写ID开始验证结束！pass', 2)
            return True
        else:
            self.send_signal(self.id, '读写ID开始验证结束！fail', 3)
            return False

    def product_test(self):

        # while True:
        #     self.send_signal(self.id, '等待插入模块！', 2)
        # 侦听循环
        while self.recv_flag:
            if self.ser.inWaiting():
                res = self.ser.readall().hex().upper()
                if res == 'ED000783CC000000FF4EEE':
                    obj_write_info = binascii.a2b_hex(self.rep_order.replace(" ", ""))
                    self.ser.write(obj_write_info)
                    self.recv_flag = False
                    # self.test_flag = True
        # while self.test_flag:
        print('part 1,check version')
        res = self.check_version()
        # if not res:
        #     break
        time.sleep(1)
        print('part 2,voltage test')
        res = self.check_pinVoltage()
        # if not res:
        #     break
        time.sleep(1)
        print('part 3,Communication to verify')
        res = self.communication_test()
        time.sleep(1)
        print('part 4,offset test')
        res = self.check_offset()
        time.sleep(1)
        print('part 5,Zero circuit')
        res = self.zero_circuit()
        time.sleep(1)
        print('part 6,power consumption')
        res = self.power_consumption()
        time.sleep(1)
        print('part 7,Power failure report')
        res = self.power_report()
        time.sleep(1)
        print('part 8,Written to the ID')
        res = self.wirte_snid()
            # self.recv_flag = True
            # self.test_flag = False

    def run_all(self):
        self.check_com_port() # open port
        if not self.ser_flag:
            return
        self.product_test() # test

    def run(self):
        print('产测线程启动')
        try:
            self.run_all()
        except Exception as e:
            print(e)
        finally:
            print('产测线程结束')
            if self.ser_flag:
                self.ser.close()
            return
