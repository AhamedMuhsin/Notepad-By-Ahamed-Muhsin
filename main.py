from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def File():
    global file
    root.title("Untitled - Notepad by Ahamed Muhsin")
    file = None
    TextArea.delete(1.0, END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt,", filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad by Ahamed Muhsin")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def Savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = "Untitled.txt", defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad by Ahamed Muhsin")

    else:
        f = open("file", "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def Quitapp():
    root.destroy()

def cut():
    TextArea.event_generate("<<Cut>>")

def copy():
    TextArea.event_generate("<<Copy>>")

def paste():
    TextArea.event_generate("<<Paste>>")

def about():
    showinfo("Notepad", "Notepad by Ahamed Muhsin")

if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad by Ahamed MUhsin")
    root.wm_iconbitmap("notepad.ico")
    root.geometry("750x500")

    TextArea = Text(root, font="simple 10")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    MenuBar = Menu(root)

    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_cascade(label="New", command=File)

    FileMenu.add_cascade(label="Open", command=openfile)

    FileMenu.add_cascade(label="Save", command= Savefile)
    FileMenu.add_separator()
    FileMenu.add_cascade(label="Exit", command=Quitapp)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_cascade(label="Cut", command=cut)
    EditMenu.add_cascade(label="Copy", command =copy)
    EditMenu.add_cascade(label="Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_cascade(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    root.config(menu=MenuBar)

    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
