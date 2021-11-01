import re


class laptop:
    __ScreenSize = 0
    __Price = 0
    __CPUmodel = ''
    __MemorySize = ''
    __StandbyTime = ''

    def setScreenSize(self, size):
        if size > 0:
            self.__ScreenSize = str(size) + 'inch'
        else:
            pass

    def setPrice(self, price):
        if price > 0:
            self.__Price = '$' + str(price)
        else:
            pass

    def setCPUmodel(self, Cmodel):
        if bool(re.search(r'[^a-zA-Z0-9]', Cmodel)) is False:
            self.__CPUmodel = Cmodel
        else:
            pass

    def setMemorySize(self, memorySize):
        if bool(re.search(r'B', memorySize[-2:])) is True:
            self.__MemorySize = memorySize
        else:
            print('unit?')

    def setStandbyTime(self, time):
        if 'h' or 'days' or 'min' or 's' in time:
            self.__StandbyTime = time
        else:
            print('Unit?')

    def Typewords(self, type0):
        print(self.__ScreenSize, '大的屏幕上显示出：', type0)

    def PlayGame(self, GameName):
        print(self.__CPUmodel, '正在处理', GameName, '这款游戏')

    def WatchVideo(self, Video):
        print(self.__CPUmodel, '正在看', Video, '视频')


la = laptop()
la.setPrice(1000)
la.setStandbyTime('10h')
la.setMemorySize('100MB')
la.setCPUmodel('Labyrin0517')
la.setScreenSize(5.8)

la.Typewords('abcdeF')
la.PlayGame('Portal')
la.WatchVideo('一只狗正在吃桃')
