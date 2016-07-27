#for python2.7
import Tkinter as tkinter
import serialctl

class setframe(tkinter.Frame):
    def __init__(self,arg=None):
        tkinter.Frame.__init__(self,arg)
        self.pack()
        self.addwidget()
        self.master.connection = serialctl.com_port(self.master.text)

    def addwidget(self):
        self.entry_com = tkinter.Entry(self)
        self.entry_com.insert(0,"COM4")
        self.entry_com.pack(side=tkinter.LEFT)
        self.entry_fre = tkinter.Entry(self)
        self.entry_fre.insert(0,"115200")
        self.entry_fre.pack(side=tkinter.LEFT)
        self.button_open = tkinter.Button(self,text="open",command=self.open)
        self.button_open.pack(side=tkinter.LEFT)


    def open(self):
        com_number = self.entry_com.get() or "COM4"
        frequency = self.entry_fre.get() or 115200
        if self.master.connection.state == "close":
            try:
                self.master.connection.open(com_number,frequency)
                self.button_open.configure(bg = "red",text="close")
                self.master.connection.state = "open"
            except:
                print("error: port can't open.")
        else:
            try:
                self.master.connection.state = "close"
                self.master.connection.close()
                self.button_open.configure(bg = "white",text="open")
            except:
                print("error: port can't close.")




class mainframe(tkinter.Frame):
    """docstring for mianframe"""
    def __init__(self, arg = None):
        tkinter.Frame.__init__(self,arg)
        self.pack()
        self.addwidget()

    def addwidget(self):
        self.text = tkinter.Text(self)
        self.text.pack()
        self.text.tag_config("in", foreground="blue")
        self.text.tag_config("out", foreground="red")
        self.control = setframe(self)
        self.control.pack()
        self.text.bind("<Return>",self.KeyEnter)

    def KeyEnter(self,event):
        #print(self.text.get("1.0",'end-1c'))
        try:
            msg = self.connection.send(self.text.get("insert linestart",'end-1c'))
            #self.text.insert("end+1c","\n"+str(msg))
        except:
            print("error: send.")




def CreateMainFrame():
    test = mainframe()
    test.master.title('EasyAT')
    test.master.geometry('500x415')
    test.master.resizable(width=False,height=False)
    test.mainloop()


if __name__ == '__main__':
    CreateMainFrame()
