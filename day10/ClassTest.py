import re


class Waterglass:
    __height = ''
    __volumn = 0
    __color = ''
    __material = ''

    @staticmethod
    def setHeight(height):
        if int(height[:-2]) > 0 and height[-1] == 'm':
            Waterglass.__height = height
        else:
            pass

    @staticmethod
    def getHeight():
        print(Waterglass.__height)

    @staticmethod
    def setVolumn(volumn):
        if int(volumn) > 0 and int(volumn) > int(Waterglass.__height[:-2]):
            Waterglass.__volumn = volumn + Waterglass.__height[-2:] + '3'
        else:
            pass

    @staticmethod
    def getVolumn():
        print(Waterglass.__volumn)

    @staticmethod
    def setColor(color):
        if color[-1] == '色':
            Waterglass.__color = color
        else:
            print('error.')

    @staticmethod
    def getColor():
        print(Waterglass.__color)

    @staticmethod
    def setMaterial(material):
        if bool(re.search(r'\d', material)) is False:
            Waterglass.__material = material
        else:
            print('error.')

    @staticmethod
    def getMaterial():
        print(Waterglass.__material)

    @staticmethod
    def functionDescription():
        print("这是一个高度为：", Waterglass.__height, '容积为：', Waterglass.__volumn, '颜色为：', Waterglass.__color,
              '材质为：', Waterglass.__material, '的杯子')


# start from here
w = Waterglass
w.setHeight('10cm')
w.setVolumn('30')
w.setColor('蓝色')
w.setMaterial('诡异的南瓜')

Waterglass.functionDescription()
