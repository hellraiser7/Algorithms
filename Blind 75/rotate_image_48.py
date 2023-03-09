class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Rotating by 90 degrees is equivalent to transposing the matrix and reversing each row individually afterwards
        # Transpose first
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for i in range(len(matrix)):
            # loop through each row
            matrix[i] = matrix[i][::-1]
            # and reverse
        return matrix
    
# output = reverse(Transpose(A))
