def dfs(l, y, x):
    try:
        if l[y-1][x] and y>0 == 1:
            print(x, y)
            print(1)
            dfs(l, y-1, x)
    except:
        pass
    try:
        if l[y][x+1] == 1:
            print(x, y)
            print(2)
            dfs(l, y, x+1)
    except:
        pass
    try:
        if l[y+1][x] == 1:
            print(x, y)
            print(3)
            dfs(l, y+1, x)
    except:
        pass
    try:
        if l[y][x-1] and x>0 == 1:
            print(x, y)
            print(4)
            dfs(l, y, x-1)
    except:
        pass
    return 0

n = int(input())
mapIndex = []

for i in range(n):
    mapLine = list(map(int, input()))
    mapIndex.append(mapLine)

for i in range(n):
    for j in range(n):
        dfs(mapIndex, i, j)


print(mapIndex)
