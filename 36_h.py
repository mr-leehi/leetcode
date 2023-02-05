class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            temp = []
            for i in range(9):
                if row[i] != ".":
                    if row[i] in temp:
                        return False
                    else:
                        temp.append(row[i])
                        
        for i in range(9):
            temp = []
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in temp:
                        return False
                    else:
                        temp.append(board[j][i])
        
        temp = []
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] != ".":
                    if board[i][j] in temp:
                        return False
                    else:
                        temp.append(board[i][j])
                        
        temp = []
        for i in range(0,3):
            for j in range(3,6):
                if board[i][j] != ".":
                    if board[i][j] in temp:
                        return False
                    else:
                        temp.append(board[i][j])
        
        temp = []
        for i in range(0,3):
            for j in range(6,9):
                if board[i][j] != ".":
                    if board[i][j] in temp:
                        return False
                    else:
                        temp.append(board[i][j])
                        
        temp = []
        for i in range(3,6):
            for j in range(0,3):
                if board[i][j] != ".":
                    if board[i][j] in temp:
                        return False
                    else:
                        temp.append(board[i][j])
                        
        temp = []
        for i in range(3,6):
            for j in range(3,6):
                if board[i][j] != ".":
                    if board[i][j] in temp:
                        return False
                    else:
                        temp.append(board[i][j])
                        
        temp = []
        for i in range(3,6):
            for j in range(6,9):
                if board[i][j] != ".":
                    if board[i][j] in temp:
                        return False
                    else:
                        temp.append(board[i][j])
                        
        temp = []
        for i in range(6,9):
            for j in range(0,3):
                if board[i][j] != ".":
                    if board[i][j] in temp:
                        return False
                    else:
                        temp.append(board[i][j])
                        
        temp = []
        for i in range(6,9):
            for j in range(3,6):
                if board[i][j] != ".":
                    if board[i][j] in temp:
                        return False
                    else:
                        temp.append(board[i][j])
                        
        temp = []
        for i in range(6,9):
            for j in range(6,9):
                if board[i][j] != ".":
                    if board[i][j] in temp:
                        return False
                    else:
                        temp.append(board[i][j])
                        
        return True
        
        