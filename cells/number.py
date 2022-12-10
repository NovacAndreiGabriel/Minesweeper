from cells.__cell import __Cell

class Number(__Cell):
    def __init__(self, row, column):
        super().__init__(row, column)
        self.__value = 0
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value
        