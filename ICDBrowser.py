
from Tkinter import *
import ttk

__pad_x__ = 5
__pad_y__ = 5


class Browser(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self)
        self.pack(expand=NO, fill=X)
        self.master.title('ICD Browser')
        self.master.iconname("calc1")

        self.create_equipment_labels(self.master)

        self.create_message_list()

    def create_message_list(self):
        fm2 = Frame(self.master)
        t=ttk.Treeview(fm2)
        t["columns"]=("first","second")
        t.column("first")
        t.column("second")
        t.heading("first",text="first column")
        t.heading("second",text="second column")
        t.insert("",'end',text="directory 1",values=("file 1 A","file 1 B"))
        t.insert("",'end',"dir2",text="directory 2",values=("file 1 A","file 1 B"))
        t.tag_configure("ttk")
        t["displaycolumns"]=("second","first")
        t["show"]=('headings')
        t.pack(fill=BOTH,expand=YES)
        fm2.pack(side=BOTTOM, expand=YES, fill=BOTH)

    def create_equipment_labels(self, frame):

        fm = Frame(self.master, bg="blue")

        fm.pack(side=TOP, expand=NO, fill=X)

        Label(fm, text="Equipment Name",
              relief=RAISED).pack(side=LEFT,anchor=N,expand=YES,fill=X, padx=__pad_x__, pady=__pad_y__)
        Label(fm, text="Equipment FIN",
              relief=RAISED).pack(side=LEFT,anchor=N,expand=YES,fill=X, padx=__pad_x__, pady=__pad_y__)


root = Tk()
app = Browser(parent=root)
app.mainloop()