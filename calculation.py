from InputData import input_data


def cal(data):
    maxNum = data[1]
    minNum = data[1]
    minDay = 1
    maxDay = 1
    summ = 0
    for i in range(1, 30):
        summ += data[i]        #求和
        if data[i] > maxNum:   #最大值
            maxNum = data[i]
            maxDay = i
        if data[i] < minNum:   #最小值
            minDay = i
            minNum = data[i]
    tmp = data[1:30]
    tmp = tmp.sort()
    ave = summ / 29            #平均值
    ave = round(ave, 1)        #四舍五入
    mid = data[14]             #中位数
    return maxNum, maxDay, minNum, minDay, ave, mid


#data=input_data()
#cal(data)
