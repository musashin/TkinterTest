
from Tkinter import *

__pad_x__ = 5
__pad_y__ = 5

class Browser(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title('ICD Browser')
        self.master.iconname("calc1")
        #self.master.columnconfigure(0, weight=1)
        #self.master.columnconfigure(1, weight=1)
        #self.master.rowconfigure(0, weight=1)
        #self.master.rowconfigure(1, weight=1)
        #self.grid(sticky="news")

        fm = Frame(self.master)
        self.create_equipment_labels(fm)
        fm.pack(side=TOP)

        fm2 = Frame(self.master)
        scrollbar = Scrollbar(self, orient=VERTICAL)
        list = Listbox(fm2, yscrollcommand=scrollbar.set)
        list.pack(expand=YES,fill=BOTH, padx=__pad_x__, pady=__pad_y__)
        for item in range(70):
            list.insert(END, {'test':'x', 'toto':item})

        fm2.pack(side=TOP)

    def create_equipment_labels(self, frame):
        Label(frame, text="Equipment Name",
              relief=RAISED).pack(side=LEFT,anchor=N,expand=YES,fill=X, padx=__pad_x__, pady=__pad_y__)
        Label(frame, text="Equipment FIN",
              relief=RAISED).pack(side=LEFT,anchor=N,expand=YES,fill=X, padx=__pad_x__, pady=__pad_y__)


root = Tk()
app = Browser(parent=root)
app.mainloop()