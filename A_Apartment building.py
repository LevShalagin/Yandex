import sys

n, m, x, y = map(int, sys.stdin.readline().split())
threshold = (x * y + 1) // 2

grid = []
for _ in range(n * x):
    line = sys.stdin.readline().strip()
    grid.append(line)

count = 0

for floor in range(n):
    for apartment in range(m):
        start_row = floor * x
        start_col = apartment * y
        x_count = 0
        for i in range(start_row, start_row + x):
            row = grid[i]
            substring = row[start_col:start_col + y]
            x_count += substring.count('X')
        if x_count >= threshold:
            count += 1

print(count)