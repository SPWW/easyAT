import serial
import threading

class com_port(object):
    def __init__(self,board = None):
        self.parity='N'
        self.stopbits=1
        self.timeout=1
        self.rtscts=False
        self.dsrdtr=False
        self.bytesize=8
        self.state = "close"
        self.text_board = board
        self.t = None

    def listing(self):
        while True:
            if self.state == "open":
                msg = self.connection.read(200)
                cm = msg
                cm = cm.replace("\r","<CR>")
                cm = cm.replace("\n","<CN>\n")
                if self.text_board is not None:
                    self.text_board.insert("end+1c",str(cm))
                    #"\n"+str(cm)

    def open(self,port='COM4',baudrate=115200):
        self.connection = serial.Serial(port, baudrate, self.bytesize, self.parity, self.stopbits, self.timeout, self.rtscts, self.dsrdtr)
        try:
            self.t=threading.Thread(target=self.listing)
            self.t.start()
        except:
            print "unable to start thread."

    def close(self):
        self.connection.close()

    def send(self,command):
        print("........")
        print command
        print("--------")
        cmd="".join([command,"\r\n"])
        self.connection.write(cmd.encode())
#        msg=self.connection.read(200)
#        cm = msg
#        cm = cm.replace("\r","<CR>")
#        cm = cm.replace("\n","<CN>\n")
#        print cm
        return ""
