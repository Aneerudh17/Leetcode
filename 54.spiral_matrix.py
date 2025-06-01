class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top , bottom = 0, len(matrix)-1
        left , right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            #left to right along the top row, so top +=1
            for col in range(left,right +1):
                result.append(matrix[top][col])
            top += 1

            #top to bottom along the right column, so right -= 1
            for row in range(top,bottom+1):
                result.append(matrix[row][right])
            right -= 1

            #left to right along bottom row, so bottom -=1 
            if top <= bottom:
                for col in range(right,left-1,-1):
                    result.append(matrix[bottom][col])
                bottom -=1

                #bottom to top along the left coloumn , so left +=1
            if left <= right:
                for row in range(bottom,top-1,-1):
                    result.append(matrix[row][left])
                left += 1
        
        
        return result