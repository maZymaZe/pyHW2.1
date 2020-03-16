from web import web
from show_data import show_data
from manual_get import manual_get
from main import root
def jw():
    root.destroy()
    web()
def jm():
    root.destroy()
    manual_get()
def jf():
    root.destroy()
    show_data()