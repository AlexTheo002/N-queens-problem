import random

class ChessBoard:

    def __init__(self,boardSize):
        self.board = [[0] * boardSize for _ in range(boardSize)]
        self.boardSize = boardSize

    def clearBoard(self):
        boardSize = self.boardSize
        self.board = [[0] * boardSize for _ in range(boardSize)]

    def placeQueen(self,pos):
        x,y = pos
        self.board[x][y] = 1
    
    def getQueens(self):
        boardSize = self.boardSize
        queens = []
        for x in range(boardSize):
            for y in range(boardSize):
                if self.board[x][y] == 1:
                    queens.append((x,y))
        return queens
    
    def isThreatened(self, pos):
        x,y = pos
        for queen in self.getQueens():
            qx,qy = queen
            #print (pos, queen)
            if pos!=queen: # queen is not the same
                #print(pos,queen)
                if x == qx or y == qy or abs(x-qx) == abs(y-qy): # check if threatened
                    #print(f" {pos}  is threatened by {queen}")
                    return True
        #print(f"{pos} is not threatened")
        return False



    def isGoal(self):
        for queen in self.getQueens():
            #print("check for threaten ",queen)
            if self.isThreatened(queen):
                return False
        return True
    
    def boardDisplay(self):
        boardSize = self.boardSize
        for i in reversed(range(boardSize)):
            row = [self.board[j][i] for j in range(boardSize)]
            print(row)


    def bogoSolve(self):
        tries = 0
        boardSize = self.boardSize
        while tries == 0 or not self.isGoal():
            print(tries)
            self.clearBoard()
            for x in range(0,boardSize):
                y = random.randint(0,boardSize-1)
                pos = (x,y)
                self.placeQueen(pos)
            tries +=1
        print("Goal found after",tries,"tries!")
        self.boardDisplay()


game = ChessBoard(8)
game.bogoSolve()
