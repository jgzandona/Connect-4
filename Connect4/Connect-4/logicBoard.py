
import numpy as np
from numpy.lib.function_base import _calculate_shapes
numRows = 6
numColumns = 7


class LogicBoard():
    def __init__(self):
        self.state = np.zeros((numRows, numColumns))
        self.turn = 1
        self.winner = 0

    def getTurn(self):
        return self.turn

    def nextTurn(self):
        self.turn = -self.turn

    def getState(self):
        return self.state

    def canDrop(self, column):
        if self.state[numRows-1][column]:
            return False
        return True

    def isFull(self):
        for column in range(7):
            if not self.state[numRows-1][column]:
                return False
        return True

    def verifyRow(self, row):
        board = self.state
        tempValue = 0
        tempSequence = 0
        for i in range(numColumns):
            if tempSequence == 4:
                self.winner = tempValue
                return True
            if board[row][i] == 0:
                tempSequence = 0
                tempValue = 0
            else:
                if board[row][i] == tempValue:
                    tempSequence += 1
                else:
                    tempSequence = 1
                    tempValue = board[row][i]
        return False

    def verifyRows(self):
        for i in range(numRows):
            if self.verifyRow(i):
                return True
        return False

    def verifyColumn(self, column):
        tempValue = 0
        tempSequence = 0
        for i in range(numRows):
            if tempSequence == 4:
                self.winner = tempValue
                return True
            if self.state[i][column] == 0:
                tempSequence = 0
                tempValue = 0
            else:
                if self.state[i][column] == tempValue:
                    tempSequence += 1
                else:
                    tempSequence = 1
                    tempValue = self.state[i][column]
        return False

    def verifyColumns(self):
        for i in range(numColumns):
            if self.verifyColumn(i):
                return True
        return False

    def verifyDiagonal(self):
        board = self.state
        for i in range(numColumns-3):
            for j in range(numRows-3):
                if(board[j][i] == board[j+1][i+1] == board[j+2][i+2] == board[j+3][i+3]):
                    self.winner = board[j][i]
                    return True
        return False

    def verifyOpositeDiagonal(self):
        board = self.state
        for i in range(numColumns-3):
            for j in range(numRows-3):
                if(board[j][numColumns-i-1] == board[j+1][numColumns-i-2] == board[j+2][numColumns-i-3] == board[j+3][numColumns-i-4]):
                    self.winner = board[j][numColumns-i-1]
                    return True
        return False

    def topOfColumn(self, column):
        for i in range(numRows):
            if self.state[i][column] == 0:
                return i

    def isGameOver(self):
        return(self.verifyOpositeDiagonal() or self.verifyDiagonal() or self.verifyColumns() or self.verifyRows() or self.isFull())

    def getWinner(self):
        return self.winner

    def dropPiece(self, column):
        if self.canDrop(column):
            self.state[self.topOfColumn(column)][column] = self.turn
            return True
        return False
