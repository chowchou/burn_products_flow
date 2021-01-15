import func_timeout
from PyQt5.QtCore import QThread, pyqtSignal
import serial
import public_var


class Listeners_thread(QThread):
    _signal = pyqtSignal(str)
    def __init__(self):
        super(Listeners_thread, self).__init__()
        self.id = id
        self.ser_flag = False
        self.port = 'COM62'

    def run(self):
        try:
            self.ser = serial.Serial(self.port, 9600, timeout=0.1)
            while True:
                if not public_var.first_step:
                    return
                if self.ser.inWaiting():
                    res = self.ser.readall().hex().upper()
                    print(res,'接收')
                    self._signal.emit(res)
        except Exception as e:
            print(e)
        # finally:
        #     return
