from web import web
from manual_get import manual_get
import tkinter as tk
from show_data import show_data


def jw():
    root.destroy()
    web()


def jm():
    root.destroy()
    manual_get()


def jf():
    root.destroy()
    show_data()

#tkinter gui  3个分支
root = tk.Tk()
root.title("get data")
root.geometry('300x350')
l1 = tk.Label(root,
              text="    Hello! In this programme\
, you\ncan learn something about\nnew patients of 2019-nCoV in\
 \nChina in each day of Febrary.",
              fg='black',
              font=('Arial', 12),
              width=90,
              height=8)
l1.pack()
bt = tk.Button(root,
               text="get data from Internet(recommended)",
               height=3,
               width=35,
               command=jw)
bt.pack()
bt2 = tk.Button(root, text="manual input", height=3, width=35, command=jm)
bt2.pack()
bt3 = tk.Button(root, text="file is prepared", height=3, width=35, command=jf)
bt3.pack()
root.mainloop()
