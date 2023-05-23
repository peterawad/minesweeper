import random
class Cell(object):
    value = 0
    selected = False
    mine = False
    flag=False

    def __init__(self):
        self.selected = False

    def __str__(self):
        return str(Cell.value)

    def isMine(self):
        if Cell.value == -1:
            return True
        return False


class Grid(object):
    def __init__(self, m_GridSize, m_numMines):
        self.Grid = [[Cell() for i in range(m_GridSize)] for j in range(m_GridSize)]
        self.GridSize = m_GridSize
        self.numMines = m_numMines
        self.selectableSpots = m_GridSize * m_GridSize - m_numMines
        i = 0
        while i < m_numMines:#add mines random in Grid
            x = random.randint(0, self.GridSize-1)
            y = random.randint(0, self.GridSize-1)
            if not self.Grid[x][y].mine:
                self.addMine(x, y)
                i += 1
            else:
                i -= 1

    def __str__(self):
        returnString = " "
        divider = "\n---"

        for i in range(0, self.GridSize):
            returnString += " | " + str(i)
            divider += "----"
        divider += "\n"

        returnString += divider
        for y in range(0, self.GridSize):
            returnString += str(y)
            for x in range(0, self.GridSize):
                if self.Grid[x][y].mine and self.Grid[x][y].selected:
                    returnString += " |" + str(self.Grid[x][y].value)
                elif self.Grid[x][y].selected:
                    returnString += " | " + str(self.Grid[x][y].value)
                elif self.Grid[x][y].flag and self.Grid[x][y].selected:
                    returnString += " | " + str(self.Grid[x][y].value)
                else:
                    returnString += " |  "
            returnString += " |"
            returnString += divider
        return returnString

    def addMine(self, x, y):# Function add mines 
        self.Grid[x][y].value = -1
        self.Grid[x][y].mine = True
        for i in range(x-1, x+2):
            if i >= 0 and i < self.GridSize:
                if y-1 >= 0 and not self.Grid[i][y-1].mine:
                    self.Grid[i][y-1].value += 1
                if y+1 < self.GridSize and not self.Grid[i][y+1].mine:
                    self.Grid[i][y+1].value += 1
        if x-1 >= 0 and not self.Grid[x-1][y].mine:
            self.Grid[x-1][y].value += 1
        if x+1 < self.GridSize and not self.Grid[x+1][y].mine:
            self.Grid[x+1][y].value += 1

    def makeMove(self, x, y):
        self.Grid[x][y].selected = True
        self.selectableSpots -= 1
        if self.Grid[x][y].value == -1:
            return False
        if self.Grid[x][y].value == 0:
            for i in range(x-1, x+2):
                if i >= 0 and i < self.GridSize:
                    if y-1 >= 0 and not self.Grid[i][y-1].selected:
                        self.makeMove(i, y-1)
                    if y+1 < self.GridSize and not self.Grid[i][y+1].selected:
                        self.makeMove(i, y+1)
            if x-1 >= 0 and not self.Grid[x-1][y].selected:
                self.makeMove(x-1, y)
            if x+1 < self.GridSize and not self.Grid[x+1][y].selected:
                self.makeMove(x+1, y)
            return True
        else:
            return True

    def hitMine(self, x, y):# check me click on mine or not
        return self.Grid[x][y].value == -1

    def isWinner(self):
        return self.selectableSpots == 0

    def addflag(self, x, y):# Function add flag 
        self.Grid[x][y].value = " F"
        self.Grid[x][y].flag = True

def main():
    GridSize=int(8)
    numMines = int(10)
    gameOver = False
    winner = False
    board = Grid(GridSize, numMines)
    while not gameOver:
        print(board)
        print("Make your move:")
        x = int(input("x: "))
        y = int(input("y: "))
        command = input("Enter F for flag or O to open")
        if x>=0 and x<=GridSize and y>=0 and y<=GridSize:
            if command=="O" or command=="o":
                board.makeMove(x, y)
                gameOver = board.hitMine(x, y)
            if command=="F" or command=="f":
                board.makeMove(x, y)
                board.addflag(x,y)
            if board.isWinner() and gameOver == False:
                gameOver = True
                winner = True
        else :
            print("wrong value")
    print(board)
    if winner:
        print("You Win")
    else:
        print("Game Over!")

main()
