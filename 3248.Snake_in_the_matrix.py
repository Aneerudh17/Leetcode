class Solution:
    def finalPositionOfSnake(self, gridSize: int, commands: List[str]) -> int:
        x, y = 0, 0
        #onyl works when the snake starts from position 0,0
        for command in commands:
            if command == "UP":
                x -= 1
            elif command == "DOWN":
                x += 1
            elif command == "RIGHT":
                y += 1
            elif command == "LEFT":
                y -= 1
        
        return (x * gridSize) + y