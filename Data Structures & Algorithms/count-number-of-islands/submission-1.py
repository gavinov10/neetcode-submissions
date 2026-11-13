class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        input: grid --> rows, cols
        output: integer --> # of islands
        edgeC: empty grid, out of range, 

        plan:
            if not grid:
                return 0

            islands = 0
            rows = len(grid)
            cols = len(grid[0])

            visited = set() # (2,3)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == '1' and (row, col) not in visited:
                        islands += 1

                    stack = [(row, col)]

                    while stack:
                        currRow, currCol = stack.pop()

                        if (currRow, currCol) in visited:
                            continue

                        visited.add((currRow, currCol))

                        for dr, dc in directions:
                            newRow = currRow + dr
                            newCol = currCol + dc

                            if (0 <= newRow < rows
                            and 0 <= newCol < cols
                            and grid[newRow][newCol] == '1'
                            and (newRow, newCol) not in visited:
                                stack.append((newRow, newCol))
            return islands
        '''

        if not grid:
            return 0

        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        visited = set() # --> 2,3
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == '1' and (row, col) not in visited:
                    islands += 1

                    stack = [(row, col)]

                    while stack:
                        (currRow, currCol) = stack.pop()
                        if (currRow, currCol) in visited:
                            continue

                        visited.add((currRow, currCol))

                        for dr, dc in directions:
                            newRow = currRow + dr
                            newCol = currCol + dc

                            if (0 <= newRow < rows
                            and 0 <= newCol < cols
                            and grid[newRow][newCol] == '1'
                            and (newRow, newCol) not in visited):
                                stack.append((newRow, newCol))

        return islands
        