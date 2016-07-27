import serial

class com_port(object):
    def __init__(self):
        self.parity='N'
        self.stopbits=1
        self.timeout=1
        self.rtscts=False
        self.dsrdtr=False
        self.bytesize=8
        self.state = "close"

    def open(self,port='COM4',baudrate=115200):
        self.connection = serial.Serial(port, baudrate, self.bytesize, self.parity, self.stopbits, self.timeout, self.rtscts, self.dsrdtr)



    def close(self):
        self.connection.close()

    def send(self,command):
        print("........")
        print command
        print("--------")
        cmd=command + "\n\n\r"
        self.connection.write(cmd.encode())
        msg=self.connection.read(200)
        print(msg)
        return msg
