import tkinter as tk
from chart import chart
def gui(maxNum,maxDay,minNum,minDay,ave,mid,data):
    root=tk.Tk()
    lis1=[' '+str(i)+'      '+str(data[i]) for i in range(1,30)]
    lis2=["minNum:"+str(minNum),"minDay:"+str(minDay),"maxNum:"+str(maxNum)\
        ,"maxDay:"+str(maxDay),"average:"+str(ave),"median:"+str(mid)]
    list1=tk.Listbox(root)
    list2=tk.Listbox(root)
    for i in range(len(lis1)):
        list1.insert(0,lis1[len(lis1)-i-1])
    list1.insert(0,"date number")
    for i in range(len(lis2)):
        list2.insert(0,lis2[len(lis2)-i-1])
    list1.pack()
    list2.pack()
    bt=tk.Button(root,text="show the chart",command=chart)
    bt.pack()
    root.mainloop()
