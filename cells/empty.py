from cells.__cell import __Cell
from cells.__cell import indexCheck
from cells.mine import Mine

class Empty(__Cell):
    def __init__(self, row, column):
        super().__init__(row, column)
                        