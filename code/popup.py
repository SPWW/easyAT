# -*- coding: UTF-8 -*-
import Tkinter as tkinter
import sqlite3

class popup(tkinter.Frame):
    def __init__(self,arg=None):
        tkinter.Frame.__init__(self,arg)
        self.pack()
        self.CreatWidget()
        self.OpenDatabase()

    def CreatWidget(self):
        self.list = tkinter.Listbox(self)
        self.list.pack()

    def OpenDatabase(self):
        self.__data = sqlite3.connect('data.db')
        self.__cursor = self.__data.cursor()

    def FetchDate(self,text):
        # Do this instead
        self.__cursor.execute('SELECT name FROM members WHERE name LIKE \''+text+'%\' LIMIT 5')
        return self.__cursor.fetchall()

    def Show(self,text,geo):
        for item in self.FetchDate(text):
            print item
            self.list.insert(tkinter.END,item)
        #self.list.pack()
        try:
            self.master.geometry('%dx%d+%d+%d' % geo)
            self.master.update()
            self.master.deiconify()
        except:
            print "wront"
        print "show over"

    def Hide(self):
        self.master.withdraw()


    def __del__(self):
        self.__data.close()
        print "close"



if __name__ == "__main__":
    app = popup()
    app.Show("t")
    app.mainloop()


