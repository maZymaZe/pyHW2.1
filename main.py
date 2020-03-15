from InputData import input_data
from calculation import cal
from gui import gui
from web import web
web()
data=input_data()
maxNum,maxDay,minNum,minDay,ave,mid=cal(data)
gui(maxNum,maxDay,minNum,minDay,ave,mid,data)