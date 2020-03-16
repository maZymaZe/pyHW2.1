from show_data import show_data
def manual_get():
    f = open("data.txt", "w")
    s = []
    for i in range(1, 30):
        print("please input tne number of new patients on Feb %d" % i)
        t = input()
        while (not(t.isdigit() and float(t) % 1 < 0.0001 and float(t)+0.5 > 0)):
            print("please input natural number ONLY")
            # print(t)
            t = input()
        s.append(str(i)+" "+t+"\n")
    f.writelines(s)
    f.close()
    show_data()
# manual_get()
