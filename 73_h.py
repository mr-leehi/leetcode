class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        zero_row = []
        zero_column = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_row.append(i)
                    zero_column.append(j)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i in zero_row) or (j in zero_column):
                    matrix[i][j] = 0
                    
        return matrix

        