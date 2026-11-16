class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        input: grid
        output: integer --> max area of island (horizontally/vertically)
        edgeC: empty grid, out of range

        plan: 
            if not grid:
                return 0

            maxArea = 0
            rows, cols = len(grid), len(grid[0])
            
            visited = set() #(3,3)
            directions = [(1,0), (-1, 0), (0, -1), (0, 1)]

            for row in range(rows):
                for col in range(cols):

                    if grid[row][col] == '1' and (row, col) not in visited:
                        area = 0
                        stack = [(row, col)]

                        while stack:
                            currRow, currCol = stack.pop()
                            if (currRow, currCol) in visited:
                                continue

                            visited.add((currRow, currCol))
                            area += 1

                            for dr, dc in directions:
                                newRow = currRow + dr
                                newCol = currCol + dc

                                if (0 <= newRow < rows
                                and 0 <= newCol < cols
                                and grid[newRow][newCol] == '1'
                                and (newRow, newCol) not in visited):
                                    stack.append((newRow, newCol))

                        maxArea = max(maxArea, area)

            return maxArea
        """

        if not grid:
            return 0

        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        
        visited = set() #(3,3)
        directions = [(1,0), (-1, 0), (0, -1), (0, 1)]

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 1 and (row, col) not in visited:
                    area = 0
                    stack = [(row, col)]

                    while stack:
                        currRow, currCol = stack.pop()
                        if (currRow, currCol) in visited:
                            continue

                        visited.add((currRow, currCol))
                        area += 1

                        for dr, dc in directions:
                            newRow = currRow + dr
                            newCol = currCol + dc

                            if (0 <= newRow < rows
                            and 0 <= newCol < cols
                            and grid[newRow][newCol] == 1
                            and (newRow, newCol) not in visited):
                                stack.append((newRow, newCol))

                    maxArea = max(maxArea, area)

        return maxArea