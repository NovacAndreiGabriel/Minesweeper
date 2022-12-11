from math import sqrt

class Flag():
    def __init__(self, row, column, CELL_WIDTH, CELL_HEIGHT):
        self.__row = row
        self.__column = column
        
        self.__clothTrianglePoints = []
        
        cellWidth = CELL_WIDTH - 2
        cellHeight = CELL_HEIGHT - 2
        
        self.__stickRectangleHeight = int(4 * cellHeight / 5)
        self.__stickRectangleWidth = int(self.__stickRectangleHeight / 20)
        
        clothTriangleSize = int(self.__stickRectangleHeight / 2)
        clothTriangleHeight = int(clothTriangleSize * sqrt(3) / 2)
        
        hitboxWidth = self.__stickRectangleWidth + clothTriangleHeight
        hitboxHeight = self.__stickRectangleHeight
        
        hitboxX = int((column * CELL_WIDTH - 2) + (cellWidth - hitboxWidth) / 2)
        hitboxY = int((row * CELL_HEIGHT - 2) + (cellHeight - hitboxHeight) / 2)
        
        clothTrianglePoint0 = (hitboxX + clothTriangleHeight, hitboxY)
        clothTrianglePoint1 = (hitboxX + clothTriangleHeight, hitboxY + int(hitboxHeight / 2))
        clothTrianglePoint2 = (hitboxX, hitboxY + int(clothTriangleSize / 2))
            
        self.__stickRectanglePointX = clothTrianglePoint1[0]
        self.__stickRectanglePointY = clothTrianglePoint1[1]
        
        self.__clothTrianglePoints.append(clothTrianglePoint0)
        self.__clothTrianglePoints.append(clothTrianglePoint1)
        self.__clothTrianglePoints.append(clothTrianglePoint2)
        
    @property 
    def row(self):
        return self.__row
    
    @property 
    def column(self):
        return self.__column    
    
    @property
    def stickRectangleX(self):
        return self.__stickRectanglePointX
    
    @property
    def stickRectangleY(self):
        return self.__stickRectanglePointY
    
    @property
    def clothTrianglePoints(self):
        return self.__clothTrianglePoints
    
    @property
    def stickRectangleWidth(self):
        return self.__stickRectangleWidth
    
    @property
    def stickRectangleHeight(self):
        return self.__stickRectangleHeight