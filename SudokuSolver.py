"""

    HEXADECIMAL SUDOKU SOLVER
    CREATED BY
    RAMKUMAR RAJABASKARAN
    ADITHYA SRINIVASAN
    SRISRUTHI SRIDHAR
    SHRAAVANTH PENUGONDA
"""

VALUES = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
ROW=4
COL=4

class Board:
    """
        Parent Class
        Data structure to contain the board
    """
    def __init__(self,matrix):
        
    def isBoardValid(self):
        
    
class Rows(Board):
    """
        Data structure to work on row of a board
    """
    def _isRowValid(self,row):

class Columns(Board):
    """
        Data structure to work on coloumn of a board
    """
    def _isColValid(self,col):

class Boxes(Board):
    """
        Data structure to work on a Box of a board
    """
    def _isBoxValid(self,boxNum):

class Cell(Board,Rows,Columns,Boxes):
    """
        Elemental Data structure to represent a cell
        of the Sudoku puzzle
    """
    def __init__(self,row,col,value):

    def _isCellVaild(self,row,col):

def CreateBoard(maxtrix):
    """
        Creates a board and checks the validity of the board
    """
    board = Board(matrix)
    return Board._isBoardValid(board)

def main(argv):
    """
        Main function to start the procedure and
        provide Flow Control
    """

if __name__== "__main__":
    main(sys.argv)
