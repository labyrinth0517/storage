import time
from threading import Thread
basket = 0


class chef(Thread):
    __name = ''
    __make = 0

    def setName0(self, name0):
        self.__name = name0

    def run(self) -> None:
        global basket
        while True:
            if basket < 500:
                self.__make = self.__make + 1
                basket += 1
                print(self.__name, '做了', self.__make, '个蛋挞，篮子里目前共', basket, '个蛋挞')
            elif basket == 500:
                time.sleep(3)
                if basket == 500:
                    print('没人买了。')
                    print(self.__name, '今天工作了蛋挞：', self.__make, '个，工资有：', self.__make * 12, '元')
                    break


class customer(Thread):
    __name1 = ''
    __count = 0
    __money = 3000

    def setName1(self, name1):
        self.__name1 = name1

    def getName1(self):
        return self.__name1

    def getCount(self):
        return self.__count

    def run(self) -> None:
        global basket
        while True:
            if self.__money > 0 and basket > 0:
                self.__count += 1
                self.__money -= 3  # 每个蛋挞3元
                basket -= 1
                print(self.__name1, '抢了', self.__count, '个蛋挞')
            elif basket == 0:
                time.sleep(3)
            elif self.__money == 0:
                print(self.__name1, '没钱了,共抢到蛋挞', self.__count, '个，花费金钱：', self.__count * 3)
                break


w1 = chef()
w2 = chef()
w1.setName('工人A')
w2.setName('工人B')

c1 = customer()
c2 = customer()
c1.setName('韭菜a')
c2.setName('韭菜b')

w1.start()
w2.start()
c1.start()
c2.start()
