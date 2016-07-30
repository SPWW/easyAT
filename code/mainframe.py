#for python2.7
# -*- coding: UTF-8 -*-
import Tkinter as tkinter
import serialctl
import popup

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
        self.newtop =tkinter.Toplevel(self.master,width=150)
        self.newtop.overrideredirect(True)
        self.popwin = popup.popup(self.newtop)
        self.popwin.Hide()
        #self.popwin.Show('王')

    def GetCurserLoc(self):
        w = self.text
        # Get the Text widget's current location
        pos_x, pos_y = w.winfo_rootx(), w.winfo_rooty()
        # Get the bounding box of the insertion cursor
        cursor = tkinter.INSERT
        bbox = w.bbox(cursor)
        if bbox is None:
            print('Cursor is not currently visible. Scrolling...')
            w.see(cursor)
            bbox = w.bbox(cursor)
        bb_x, bb_y, bb_w, bb_h = bbox
        ox = pos_x + bb_x
        oy = pos_y + bb_y + bb_h
        s = 'Cursor: (%d, %d)' % (ox, oy)
        print(s)
        geo = (200, 400, ox, oy)
        return geo

    def KeyEnter(self,event):
        #print(self.text.get("1.0",'end-1c'))
        try:
            command = self.text.get("insert linestart",'end-1c')
            #msg = self.connection.send(self.text.get("insert linestart",'end-1c'))
            #self.text.insert("end+1c","\n"+str(msg))
            geo = self.GetCurserLoc()
            print geo
            self.popwin.Show(command,geo)
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
