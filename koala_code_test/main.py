from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as tkst

# CONSTANT VARIABLES
BLACK = "#000000"
WHITE = "#FFFFFF"

# DECLARED VARIABLES
no_of_windows = 1

class Sticky_Notes(Toplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master , **kwargs)
        # Clearing default titlebar, setting up custom version with buttons
        self.overrideredirect(True)
        self.titlebar = Frame(self, bg=WHITE)
        self.titlebar.bind('<1>', self.get_pos)
        self.titlebar.bind('<B1-Motion>', self.move_window)
        # positioned at top to facilitate click and drag of windows
        self.titlebar.pack(fill=X, side=TOP)

        self.xclick = 0
        self.yclick = 0


        global no_of_windows
        self.geometry('200x350+' + str(1000+no_of_windows*(-30)) + '+' + str(100 + no_of_windows*20))
        self.config(bg=WHITE)
        self.attributes('-topmost', 'true')
        self.resizable(True, True)

        self.delete = Label(self.titlebar, text='Delete Note', bg=WHITE, relief='flat')
        self.delete.bind('<1>', self.delete_note)
        self.delete.pack(side=RIGHT)

        self.create_new = Label(self.titlebar, text='Create New Note', bg=WHITE, relief='flat')
        self.create_new.pack(side=LEFT)
        self.create_new.bind('<1>', self.another_window)

        self.note_body = tkst.ScrolledText(self, bg=WHITE, font=('Menlo', 14, 'italic'), relief='flat',
                                          padx=5, pady=10)
        self.note_body.pack(fill=BOTH, expand=1)
        # Increase number of windows variable, necessary for close button to function properly
        no_of_windows += 1

    def get_pos(self, event):
        self.xclick = event.x
        self.yclick = event.y

    def move_window(self, event):
        self.geometry('+{0}+{1}'.format(event.x_root - self.xclick, event.y_root - self.yclick))

    def another_window(self, event):

        sticky = Sticky_Notes(root)

    # def clear_all(self, event):
    #     if (messagebox.askyesno('Clear All?', parent=self)):
    #         root.destroy()

    def delete_note(self, event):
        if (messagebox.askyesno('Remove Note?', parent=self)):
            global no_of_windows
            self.destroy()
            no_of_windows -= 1
            if (no_of_windows == 1):
                root.destroy()
            return


root = Tk()
root.withdraw()
sticky = Sticky_Notes(root)
root.mainloop()
