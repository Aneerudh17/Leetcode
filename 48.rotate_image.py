class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        total_length = len(matrix)
        #first performing a vertical reversal
        #to vertically reverse , swap the last and first coloumn of top and bottom row using a temporary variable
        #and then move the pointer by one till top < bottom

        top = 0
        bottom = total_length -1

        while top < bottom :
            for col in range(total_length):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp 
            top += 1
            bottom -= 1

            #the above for loops handles the vertical reversal for every coloumn until top = bottom
            #next for is to transpose the elements byb 90 degrees
            #swap the row and coloumn with a temp variable

        for row in range(total_length):
            for col in range(row+1,total_length):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp

        return matrix  