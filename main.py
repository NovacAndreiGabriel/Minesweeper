import pygame
import random
import os

from cells.empty import Empty
from cells.number import Number
from cells.mine import Mine 

NUMBER_OF_ROWS = 9
NUMBER_OF_COLUMNS = 9
NUMBER_OF_MINES = 10

COLORS = {
    "WHITE" : (255, 255, 255),
    "BLACK" : (0, 0, 0),
    "LIGHT_GRAY" : (192, 192, 192),
    "DARK_GRAY" : (128, 128, 128),
    "BLUE" : (0, 0, 255),
    "GREEN" : (0, 255, 0),
    "RED" : (255, 0, 0),
    "PURPLE" : (128, 0, 128),
    "MAROON" : (128, 0, 0), 
    "TURQUOISE" : (64, 224, 208),
}

COLORS_OF_NUMBERS = {
    1 : COLORS["BLUE"],
    2 : COLORS["GREEN"],
    3 : COLORS["RED"],
    4 : COLORS["PURPLE"],
    5 : COLORS["MAROON"],
    6 : COLORS["TURQUOISE"],
    7 : COLORS["BLACK"],
    8 : COLORS["DARK_GRAY"],
}

WIDTH = 540
HEIGHT = 540

CELL_WIDTH = int(WIDTH / NUMBER_OF_COLUMNS)
CELL_HEIGHT = int(HEIGHT / NUMBER_OF_ROWS)

grid = []

def indexInRange(row, column, numberOfRows, numberOfColumns):
    if row in range(0, numberOfRows) and column in range(0, numberOfColumns):
        return True
    return False

def createGrid(numberOfRows, numberOfColumns, numberOfMines):
    grid = []
    for _ in range(numberOfRows):
        gridRow = []
        for __ in range(numberOfColumns):
            gridRow.append(None)
        grid.append(gridRow)
    
    numberOfMinesPlaced = 0
    
    while numberOfMinesPlaced != numberOfMines:
        row = random.randint(0, numberOfRows - 1)
        column = random.randint(0, numberOfColumns - 1)
        if grid[row][column] == None:
            grid[row][column] = '*'
            numberOfMinesPlaced += 1
    
    for _ in range(numberOfRows):
        for __ in range(numberOfColumns):
            if grid[_][__] == None:
                numberOfAdjacentMines = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if indexInRange(_ + i, __ + j, numberOfRows, numberOfColumns) and grid[_ + i][__ + j] == '*':
                            numberOfAdjacentMines += 1
                if numberOfAdjacentMines == 0:
                    grid[_][__] = "_"
                else:
                    grid[_][__] = numberOfAdjacentMines
                    
    file = open("minesweeper.txt", "w")
    
    for _ in range(NUMBER_OF_ROWS):
        for __ in range(NUMBER_OF_COLUMNS):
            cellAsString = str(grid[_][__]) + " "
            file.write(cellAsString)
        file.write("\n")

    file.close()

def getGridFromFile(fileName):
    file = open(fileName, "r")
    
    grid = []
    row = 0
    column = 0
    for line in file:
        gridRow = []
        for character in line:
            if character != ' ' and character != '\n':
                cell = None
                if character == '_':
                    cell = Empty(row, column)
                elif character == '*':
                    cell = Mine(row, column)
                else:
                    cell = Number(row, column)
                    cell.value = int(character)
                cell.x = int(column * WIDTH / NUMBER_OF_COLUMNS)    
                cell.y = int(row * HEIGHT / NUMBER_OF_ROWS)
                column += 1
                gridRow.append(cell)
        grid.append(gridRow)
        column = 0
        row += 1
    
    file.close()
    os.remove(fileName)
    return grid
    
def reveal(cell):
    global grid
    grid[cell.row][cell.column].visible = True
    if isinstance(cell, Mine):
        for _ in range(len(grid)):
            for __ in range(len(grid[0])):
                if not grid[_][__].visible:
                    grid[_][__].visible = True
    elif isinstance(cell, Empty):
        for _ in range(-1, 2):
            for __ in range(-1, 2):
                row = cell.row + _
                column = cell.column + __
                if indexInRange(row, column, len(grid), len(grid[0])):
                    if not isinstance(cell, Mine) and not grid[row][column].visible:
                        reveal(grid[row][column])               
    
def main():
    global grid
    createGrid(NUMBER_OF_ROWS, NUMBER_OF_COLUMNS, NUMBER_OF_MINES)
    grid = getGridFromFile("minesweeper.txt")
    
    
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Minesweeper")
    running = True
    
    mousePosition = (0, 0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                cellRow = mousePosition[1] // CELL_HEIGHT
                cellColumn = mousePosition[0] // CELL_WIDTH
                reveal(grid[cellRow][cellColumn])
                
        for row in grid:
            for cell in row:
                outsideRectangle = pygame.Rect(cell.x, cell.y, CELL_WIDTH, CELL_HEIGHT)
                insideRectangle = pygame.Rect(cell.x + 1, cell.y + 1, CELL_WIDTH - 2, CELL_HEIGHT - 2)
                
                pygame.draw.rect(screen, COLORS["WHITE"], outsideRectangle)
                if cell.visible == True:
                    pygame.draw.rect(screen, COLORS["LIGHT_GRAY"], insideRectangle)
                    if isinstance(cell, Mine):
                        pygame.draw.circle(screen, COLORS["BLACK"], (outsideRectangle.centerx, outsideRectangle.centery), int(outsideRectangle.width / 4))
                        pygame.draw.circle(screen, COLORS["DARK_GRAY"], (insideRectangle.centerx, insideRectangle.centery), int(insideRectangle.width / 4 - 2))
                    elif isinstance(cell, Number):
                        font = pygame.font.SysFont("arial", CELL_HEIGHT)
                        text = font.render(str(cell.value), True, COLORS_OF_NUMBERS[cell.value])
                        screen.blit(text, (cell.x + 12, cell.y - 4))
                else:
                    pygame.draw.rect(screen, COLORS["DARK_GRAY"], insideRectangle)
        pygame.display.update()
                
    pygame.quit()
                
if __name__ == "__main__":
    main()