#! Transpose a Matrix : 

class Solution(object):
    def transpose(self, matrix):
        transpose_row = zip(*matrix)
        transpose_matrix = [list(row) for row in transpose_row]
        return transpose_matrix


matrix =[[1,2,3],[4,5,6],[7,8,9]]      
sol = Solution() 
last = sol.transpose(matrix)
print(last)