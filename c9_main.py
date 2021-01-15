import configparser
import sys

from PyQt5 import QtWidgets

from main import Ui_MainWindow

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QComboBox, QRadioButton, QMessageBox, QCheckBox, \
    QLineEdit
import public_var
from product_test import Prod_test
from port_down import Port_down
from Listeners_thread import Listeners_thread

class C9v_burn( QWidget , Ui_MainWindow):
    def __init__(self):
        super(C9v_burn,self).__init__()
        self.setupUi(self)
        self.init_show()
        # self.group_0.setEnabled(False)
        self.button_o()
        self.read_config()
        self.show_config()
        self.bin_src = False
        self.qcode_dict = {0:None,1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None}
    def init_show(self):
        for i in range(10):
            group_name = 'self.group_%s.setEnabled(False)' %str(i)
            eval(group_name)
            qcode_name = 'self.qcode_%s.setEnabled(False)' %str(i)
            eval(qcode_name)
            list_name = 'self.textBrowser_0_%s.setEnabled(False)' % str(i)
            eval(list_name)
            pro_name = 'self.progressBar_0_%s.setValue(0)' % str(i)
            eval(pro_name)
            text_name = 'self.label_res_%s' % str(i)
            eval(text_name).setText('串口未开启')
        # self.progressBar_0_0.setValue(0)
        self.checkBox_option_2.setChecked(True)
        self.checkBox_option_2.setEnabled(False)
        self.pushButton_20.setEnabled(False)
        self.bin_lab.setText('请选择bin文件')
        self.bin_button.setEnabled(False)
        self.close_third()
        self.label_2.setText('0')
        self.label_4.setText('0')
        self.label_6.setText('0')
        self.qcode_0.returnPressed.connect(lambda: self.qcode_slot(0))
        self.qcode_1.returnPressed.connect(lambda: self.qcode_slot(1))
        self.qcode_2.returnPressed.connect(lambda: self.qcode_slot(2))
        self.qcode_3.returnPressed.connect(lambda: self.qcode_slot(3))
        self.qcode_4.returnPressed.connect(lambda: self.qcode_slot(4))
        self.qcode_5.returnPressed.connect(lambda: self.qcode_slot(5))
        self.qcode_6.returnPressed.connect(lambda: self.qcode_slot(6))
        self.qcode_7.returnPressed.connect(lambda: self.qcode_slot(7))
        self.qcode_8.returnPressed.connect(lambda: self.qcode_slot(8))
        self.qcode_9.returnPressed.connect(lambda: self.qcode_slot(9))

    def qcode_slot(self,data):
        try:
            ss = 'self.qcode_%s.text()' %str(data)
            qcode_value = eval(ss)
            self.qcode_dict[data] = qcode_value
            if data == 9:
                self.qcode_0.setFocus()
            else:
                ss = 'self.qcode_%s.setFocus()' %str(data+1)
                eval(ss)
        except Exception as e:
            print(e)

    def count_nums(self,data):
        data = data.split(',')
        res_list = []
        for i in data:
            res = "%.2X" % (int(i))
            res_list.append(res)
        return ''.join(res_list)

    def count_2nums(self,data):
        data = data.split(',')
        res_list = []
        f2 = lambda d: "%.4X" % (int(65536 - abs(d))) if (d < 0) else "%.4X" % (d)
        for i in data:
            res = f2(int(i))
            res_list.append(res)
        return ''.join(res_list)

    def button_click(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", "./", "All Files (*);;Text Files (*.txt)")
        self.bin_lab.setText(directory[0])
        # print(self.bin_lab.text())
        public_var.bin_src = self.bin_lab.text()
        # print(public_var.bin_src[-3:])
        if public_var.bin_src[-3:] == 'bin':
            self.bin_src = True
            print('bin正确')
            public_var.second_step = True
            self.show_third()

    def save_config(self):
        try:
            read_ini = configparser.ConfigParser()
            read_ini.read('config.ini')

            rx_snr = self.count_nums(read_ini.get('communication', 'rx_snr_min_max'))
            rx_flatness = self.count_nums(read_ini.get('communication', 'rx_flatness_min_max'))
            rx_rssi = self.count_2nums(read_ini.get('communication', 'rx_rssi_min_max'))
            com_succ = self.count_nums(read_ini.get('communication', 'com_succ_min_max'))
            tx_snr = self.count_nums(read_ini.get('communication', 'tx_snr_min_max'))
            tx_flatness = self.count_nums(read_ini.get('communication', 'tx_flatness_min_max'))
            tx_rssi = self.count_2nums(read_ini.get('communication', 'tx_rssi_min_max'))
            public_var.end_order = rx_snr + rx_flatness + rx_rssi + com_succ + tx_snr + tx_flatness + tx_rssi


            if self.checkBox_option_1.isChecked():
                public_var.burn_flag = 1
                read_ini.set('test option','burn_flag','1')
            else:
                public_var.burn_flag = 0
                read_ini.set('test option', 'burn_flag', '0')
            for i in range(len(public_var.test_option)):
                num = str(i)
                ss = 'self.toption_%s.isChecked()'%num
                res = eval(ss)
                public_var.test_option[num] = res
            print('test option:',public_var.test_option)
            read_ini.write(open("config.ini", "w"))
                # print(res,'----',i)
            # for i in range(len(public_var.config_dict)):
            #     con_value = 'self.config_%s.text()' %str(i)
            #     con_value = eval(con_value)
            #     public_var.config_dict[str(i)] = con_value
            #     read_tag = public_var.config_name.get(str(i))
            #     # read_ini['test station'][read_tag] = con_value
            #     read_ini.set('test station', read_tag, con_value)
            #     read_ini.write(open("config.ini", "w"))
            #     ss = 'self.config_%s.setEnabled(False)'%str(i)
            #     eval(ss)
            self.textBrowser.append('写入配置成功')
            public_var.first_step = True
            self.pushButton_19.setEnabled(False)
            self.pushButton_20.setEnabled(True)
            self.groupBox_17.setEnabled(False)
            self.checkBox_option_1.setEnabled(False)
            if public_var.burn_flag:
                self.bin_button.setEnabled(True)
            else:
                self.bin_button.setEnabled(False)
                public_var.second_step = True
                self.show_third()
                self.no_burn()
                self.bin_lab.setText('无烧录流程')
            self.listeners_t = Listeners_thread()
            self.listeners_t._signal.connect(self.run_start)
            self.listeners_t.start()
        except Exception as e:
            print(e)
            self.textBrowser.append('写入配置失败')
        # print(public_var.config_dict)

    def run_start(self,data):
        print(data)
        if data == '00':
            print('模块上电，开始启动产测流程')
        else:
            return

        # for i in range(10):
        if self.qcode_dict.get(0):
            self.run_flow_0 = Prod_test(0,sn = self.qcode_dict.get(0))
            self.run_flow_0._signal.connect(self.run_flow_res)
            self.run_flow_0.start()
        if self.qcode_dict.get(1):
            self.run_flow_1 = Prod_test(1, sn=self.qcode_dict.get(1))
            self.run_flow_1._signal.connect(self.run_flow_res)
            self.run_flow_1.start()
        if self.qcode_dict.get(2):
            self.run_flow_2 = Prod_test(2, sn=self.qcode_dict.get(2))
            self.run_flow_2._signal.connect(self.run_flow_res)
            self.run_flow_2.start()

        # self.run_flow_3 = Prod_test(3, sn=self.qcode_dict.get(3))
        # self.run_flow_3._signal.connect(self.run_flow_res)
        # self.run_flow_3.start()
        #
        # self.run_flow_4 = Prod_test(4, sn=self.qcode_dict.get(4))
        # self.run_flow_4._signal.connect(self.run_flow_res)
        # self.run_flow_4.start()
        #
        # self.run_flow_5 = Prod_test(5, sn=self.qcode_dict.get(5))
        # self.run_flow_5._signal.connect(self.run_flow_res)
        # self.run_flow_5.start()
        #
        # self.run_flow_6 = Prod_test(6, sn=self.qcode_dict.get(6))
        # self.run_flow_6._signal.connect(self.run_flow_res)
        # self.run_flow_6.start()
        #
        # self.run_flow_7 = Prod_test(7, sn=self.qcode_dict.get(7))
        # self.run_flow_7._signal.connect(self.run_flow_res)
        # self.run_flow_7.start()
        #
        # self.run_flow_8 = Prod_test(8, sn=self.qcode_dict.get(8))
        # self.run_flow_8._signal.connect(self.run_flow_res)
        # self.run_flow_8.start()
        #
        # self.run_flow_9 = Prod_test(9, sn=self.qcode_dict.get(9))
        # self.run_flow_9._signal.connect(self.run_flow_res)
        # self.run_flow_9.start()

    def run_flow_res(self,data):
        # print(data)
        mes_type = data.get('mes_type')
        ser_flag = data.get('ser_flag')
        i = data.get('id')
        err = data.get('err')
        if mes_type == '2':
            # info
            mess = data.get('mess')
            es = 'self.textBrowser_0_%s.append(mess)' % str(i)
            eval(es)
        if mes_type == '3':
            # error
            mess = data.get('mess')
            datas = '<font color=\"#ff2121\">' + str(mess) + '</font>'
            es = 'self.textBrowser_0_%s.append(datas)' % str(i)
            eval(es)


    def show_config(self):
        # for i in range(len(public_var.config_dict)):
        #     ss = 'self.config_%s.setText(public_var.config_dict.get(str(i)))' %str(i)
        #     eval(ss)
        self.config_0.setText(public_var.config_dict.get('0'))
        if public_var.burn_flag:
            self.checkBox_option_1.setChecked(True)
        else:
            self.checkBox_option_1.setChecked(False)
        for i in range(len(public_var.test_option)):
            num = str(i)
            res = public_var.test_option.get(num)
            ss = 'self.toption_%s.setChecked(res)' %num
            eval(ss)

    def show_third(self):
        for i in range(10):
            ss = 'self.test_button_%s.setEnabled(True)' %str(i)
            eval(ss)

    def close_third(self):
        public_var.third_step = False
        for i in range(10):
            ss = 'self.test_button_%s.setEnabled(False)' % str(i)
            eval(ss)
            ss = 'self.progressBar_0_%s.setValue(0)' % str(i)
            eval(ss)

    def no_burn(self):
        for i in range(10):
            ss = 'self.progressBar_0_%s.setValue(100)' % str(i)
            eval(ss)

    def read_config(self):
        read_ini = configparser.ConfigParser()
        read_ini.read('config.ini')
        public_var.com_port = read_ini.get('test option', 'com')
        public_var.bps = read_ini.get('test option','bps')
        public_var.burn_flag = int(read_ini.get('test option','burn_flag'))
        public_var.config_dict = {'0':read_ini.get('test station','order_id'),
                                  '1':read_ini.get('test station', 'min_txd'),
                                  '2':read_ini.get('test station', 'max_txd'),
                                  '3':read_ini.get('test station', 'min_sta'),
                                  '4':read_ini.get('test station', 'max_sta'),
                                  '5':read_ini.get('test station', 'min_cap'),
                                  '6':read_ini.get('test station', 'max_cap'),
                                  '7': read_ini.get('test station', 'min_1.2v'),
                                  '8': read_ini.get('test station', 'max_1.2v'),
                                  '9': read_ini.get('test station', 'min_3.3v'),
                                  '10': read_ini.get('test station', 'max_3.3v'),
                                  '11': read_ini.get('test station', 'min_12vboost'),
                                  '12': read_ini.get('test station', 'max_12vboost'),
                                  '13': read_ini.get('test station', 'min_damping'),
                                  '14': read_ini.get('test station', 'max_damping'),
                                  '15': read_ini.get('test station', 'min_fre_offset'),
                                  '16': read_ini.get('test station', 'max_fre_offset'),
                                  '17': read_ini.get('test station', 'min_set_static'),
                                  '18': read_ini.get('test station', 'max_set_static'),
                                  '19': read_ini.get('test station', 'min_set_dynamic'),
                                  '20': read_ini.get('test station', 'max_set_dynamic'),
                                  '21': read_ini.get('test station', 'soft_version'),
                                  '22': read_ini.get('test station', 'version'),}
        option_Test = read_ini.get('test option','option_list')
        option_Test = option_Test.split(',')
        for i in range(len(option_Test)):
            res = int(option_Test[i])
            s = str(i)
            public_var.test_option[s] = res

        devId = read_ini.items('dev')
        for i in range(len(devId)):
            public_var.dev_id[devId[i][0]] = devId[i][1]

    def change_option(self):
        public_var.first_step = False
        public_var.second_step = False
        self.pushButton_19.setEnabled(True)
        self.pushButton_20.setEnabled(False)
        self.groupBox_17.setEnabled(True)
        self.checkBox_option_1.setEnabled(True)
        self.bin_lab.setText('请选择bin文件')
        self.bin_button.setEnabled(False)
        self.close_third()

    def button_o(self):
        try:
            # for i in range(10):
            #     s = 'self.test_button_%s' %i
            #     eval(s).clicked.connect(lambda: self.work_start(i))
            # The for loop cannot be used #####
            self.test_button_0.clicked.connect(lambda: self.work_start(0))
            self.test_button_1.clicked.connect(lambda: self.work_start(1))
            self.test_button_2.clicked.connect(lambda: self.work_start(2))
            self.test_button_3.clicked.connect(lambda: self.work_start(3))
            self.test_button_4.clicked.connect(lambda: self.work_start(4))
            self.test_button_5.clicked.connect(lambda: self.work_start(5))
            self.test_button_6.clicked.connect(lambda: self.work_start(6))
            self.test_button_7.clicked.connect(lambda: self.work_start(7))
            self.test_button_8.clicked.connect(lambda: self.work_start(8))
            self.test_button_9.clicked.connect(lambda: self.work_start(9))
            self.pushButton_19.clicked.connect(self.save_config)
            self.bin_button.clicked.connect(self.button_click)
            self.pushButton_20.clicked.connect(self.change_option)
        except Exception as e:
            print(e)

    def work_start(self,i):
        # if not self.bin_src:
        #     print('未选择bin文件')
        #     return

        if i == 0:
            self.pro_test_0 = Port_down(id = i)
            self.pro_test_0._signal.connect(self.mytest)
            self.pro_test_0.start()
        if i == 1:
            self.pro_test_1 = Port_down(id=i)
            self.pro_test_1._signal.connect(self.mytest)
            self.pro_test_1.start()
        if i == 2:
            self.pro_test_2 = Port_down(id=i)
            self.pro_test_2._signal.connect(self.mytest)
            self.pro_test_2.start()
        if i == 3:
            self.pro_test_3 = Port_down(id=i)
            self.pro_test_3._signal.connect(self.mytest)
            self.pro_test_3.start()
        if i == 4:
            self.pro_test_4 = Port_down(id=i)
            self.pro_test_4._signal.connect(self.mytest)
            self.pro_test_4.start()
        if i == 5:
            self.pro_test_5 = Port_down(id=i)
            self.pro_test_5._signal.connect(self.mytest)
            self.pro_test_5.start()
        if i == 6:
            self.pro_test_6 = Port_down(id=i)
            self.pro_test_6._signal.connect(self.mytest)
            self.pro_test_6.start()
        if i == 7:
            self.pro_test_7 = Port_down(id=i)
            self.pro_test_7._signal.connect(self.mytest)
            self.pro_test_7.start()
        if i == 8:
            self.pro_test_8 = Port_down(id=i)
            self.pro_test_8._signal.connect(self.mytest)
            self.pro_test_8.start()
        if i == 9:
            self.pro_test_9 = Port_down(id=i)
            self.pro_test_9._signal.connect(self.mytest)
            self.pro_test_9.start()

    def work_stop(self,i):
        print(i)
        try:
            group_name = 'self.group_%s.setEnabled(False)' % str(i)
            eval(group_name)
            qcode_name = 'self.qcode_%s.setEnabled(False)' % str(i)
            eval(qcode_name)
            list_name = 'self.textBrowser_0_%s.setEnabled(False)' % str(i)
            eval(list_name)
            self.qcode_0.setFocus()
            # qcode_name = 'self.qcode_%s.setFocus()' % str(i)
            # eval(qcode_name)
        except Exception as e:
            print(e)

    def mytest(self,data):
        print(data)
        mes_type = data.get('mes_type')
        ser_flag = data.get('ser_flag')
        i = data.get('id')
        err = data.get('err')
        if mes_type == '2':
            # info
            mess = data.get('mess')
            es = 'self.textBrowser_0_%s.append(mess)' %str(i)
            eval(es)

        if mes_type == '3':
            # error
            mess = data.get('mess')
            datas = '<font color=\"#ff2121\">' + str(mess) + '</font>'
            es = 'self.textBrowser_0_%s.append(datas)' % str(i)
            eval(es)
        if mes_type == '5':
            # progress bar
            try:
                rate = data.get('rate')
                print(rate)
                ss = 'self.progressBar_0_%s.setValue(rate)'%str(i)
                eval(ss)
            except Exception as e:
                print(e)
            # print('11')
        if mes_type == '1':
            if ser_flag:
                # i = data.get('id')
                try:
                    ss = 'self.label_res_%s.setText("串口已打开")' % str(i)
                    eval(ss)
                    datas = 'font-family:微软雅黑;color:#32CD32;font-weight:bold;font-size:14px'
                    ss = 'self.label_res_%s.setStyleSheet(datas)' % str(i)
                    eval(ss)
                    group_name = 'self.group_%s.setEnabled(True)' % str(i)
                    eval(group_name)
                    qcode_name = 'self.qcode_%s.setEnabled(True)' % str(i)
                    eval(qcode_name)
                    list_name = 'self.textBrowser_0_%s.setEnabled(True)' % str(i)
                    eval(list_name)
                    # qcode_name = 'self.qcode_%s.setFocus(True)' % str(i)
                    # eval(qcode_name)
                    self.qcode_0.setFocus()
                    ss = 'self.test_button_%s.setEnabled(False)' % str(i)
                    eval(ss)
                except Exception as e:
                    print(e)
            else:
                print(err)
                try:
                    # self.label_res_0.setText(err)
                    ss = 'self.label_res_%s' % str(i)
                    err = '打开失败：' + err
                    eval(ss).setText(err)
                    datas = 'font-family:微软雅黑;color:#FF0000;font-weight:bold;font-size:14px'
                    ss = 'self.label_res_%s.setStyleSheet(datas)' % str(i)
                    eval(ss)
                except Exception as e:
                    print(e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = C9v_burn()
    a.show()
    sys.exit(app.exec_())