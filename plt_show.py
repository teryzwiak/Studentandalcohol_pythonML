import matplotlib.pyplot as plt
class plt_show:
    def show(students):
        students['age'].plot(kind='box')
        plt.show()
        students['health'].plot(kind='box')
        plt.show()