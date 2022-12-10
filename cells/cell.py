from abc import ABC, abstractmethod

class Cell(ABC):
    
    @property
    @abstractmethod
    def flagOn(self):
        pass
    
    @flagOn.setter
    @abstractmethod
    def flagOn(self, flagOn):
        pass
    
    @property
    @abstractmethod
    def visible(self):
        pass
    
    @visible.setter
    @abstractmethod
    def visible(self, visible):
        pass
    
    @property
    @abstractmethod
    def row(self):
        pass
    
    @property
    @abstractmethod
    def column(self):
        pass
    
    @property
    @abstractmethod
    def x(self):
        pass
    
    @property
    @abstractmethod
    def y(self):
        pass

    @x.setter
    @abstractmethod
    def x(self, x):
        pass

    @y.setter
    @abstractmethod
    def y(self, y):
        pass