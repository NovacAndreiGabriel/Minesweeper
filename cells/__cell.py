from cells.cell import Cell
from abc import abstractmethod

def indexCheck(row, column, numberOfRows, numberOfColumns):
    if row >= 0 and row < numberOfRows and column >= 0 and column < numberOfColumns:
        return True
    return False

class __Cell(Cell):
    def __init__(self, row, column):
        super().__init__()
        self.__flagOn = False
        self.__visible = False
        self.__row = row
        self.__column = column
        self.__x = 0
        self.__y = 0
    
    @property
    def flagOn(self):
        return self.__flagOn
    
    @flagOn.setter
    def flagOn(self, flagOn):
        self.__flagOn = flagOn
    
    @property
    def visible(self):
        return self.__visible
    
    @visible.setter
    def visible(self, visible):
        self.__visible = visible
    
    @property
    def row(self):
        return self.__row
    
    @property
    def column(self):
        return self.__column
     
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @x.setter
    def x(self, x):
        self.__x = x
        
    @y.setter
    def y(self, y):
        self.__y = y