import matplotlib.pyplot as plt
from InputData import input_data


def chart():#绘图
    data = input_data()
    y = [data[i] for i in range(1, 30)]
    x = [str(i) for i in range(1, 30)]
    plt.title("new patients of 2019-nCoV in China in each day of Febrary")
    plt.xlabel("date")
    plt.ylabel("number of new patients")
    plt.axis([0, 31, 0, 16000])
    plt.plot(x, y, "b")
    plt.show()
