
from Tkinter import *
import ttk

__pad_x__ = 5
__pad_y__ = 5


class SignalList():
    def __init__(self, parent, heading_list, signal_list):
        t=ttk.Treeview(parent)
        t["columns"]=heading_list

        ysb = ttk.Scrollbar(orient=VERTICAL, command= t.yview)
        xsb = ttk.Scrollbar(orient=HORIZONTAL, command= t.xview)
        t['yscroll'] = ysb.set
        t['xscroll'] = xsb.set

        for col in heading_list:
            t.heading(col, text=col)

        for item in signal_list:
         t.insert("",'end',values=item)

        t.tag_configure("ttk")
        t["displaycolumns"]=("second","first")
        t["show"]=('headings')

        t.pack(side=LEFT,fill=BOTH,expand=YES)
        ysb.pack(side=LEFT, fill=Y)
        #xsb.pack(side=TOP)

        self.treeview  =t

    def set_columns(self):
        self.treeview["displaycolumns"]=("first","second")

class Browser(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self)
        self.pack(expand=NO, fill=X)
        self.master.title('ICD Browser')
        self.master.iconname("calc1")

        self.create_equipment_labels(self.master)

        self.signal_list = self.create_message_list()

        menu = Menu(parent)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Open...", command=None)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)

        viewmenu = Menu(menu)
        menu.add_cascade(label="View", menu=viewmenu)
        viewmenu.add_command(label="columns", command=self.select_column)

    def select_column(self):
        self.signal_list.set_columns()
        popup = Tk()
        popup.wm_title("Select Column")
        listbox = Listbox(popup)
        listbox.pack()

        for item in self.signal_list.treeview['columns']:
            listbox.insert(END, item)

        label = ttk.Label(popup, text="hello")
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()

    def create_message_list(self):
        fm2 = Frame(self.master)

        test = list()
        for i in range(0,30):
            test.append(('toto {!s}'.format(i),'titi {!s}'.format(i)))

        signalList = SignalList(self.master, ("first", "second"), test)
        fm2.pack(side=BOTTOM, expand=YES, fill=BOTH)

        return signalList

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