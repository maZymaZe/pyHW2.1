def manual_get():
    f=open("data.txt","w")
    for i in range(1,30):
        print("please input tne number of new patients on Feb %d"%i)
        t=input()
        while (not t.isdigit()):
            print("please input the number ONLY")
            t=input()
        s=str(i)+" "+t
        f.write(s)
    f.close()
#manual_get()