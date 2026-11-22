class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            
            visited.add((r, c))
            
            dirs = [
                (-1, 0),
                (1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if (nr in range(rows) and
                nc in range(cols) and
                (nr, nc) not in visited and
                grid[nr][nc] == "1"):
                    bfs(nr, nc)
        result = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if ((r, c) not in visited and
                grid[r][c] == "1"):
                    bfs(r, c)
                    result += 1
        return result


