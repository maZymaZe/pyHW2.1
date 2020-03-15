def input_data():
    data=[]
    for i in range(30):
        data.append(0)
    f=open("data.txt","r")
    for i in range(29):
        line=f.readline().split()
        data[int(line[0])]=int(line[1])
    f.close()
    return data
#input_data()