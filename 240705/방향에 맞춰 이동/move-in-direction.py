n=int(input())
x,y=0,0
dx = [1, -1,  0, 0]
dy = [0,  0, -1, 1]
for i in range(n):
    data =input().split()
    direction,dis = data[0], int(data[1])
    if direction == 'E':
        move_dir = 0
    elif direction == 'W':
        move_dir = 1
    elif direction == 'S':
        move_dir = 2
    else:
        move_dir = 3

    x += dx[move_dir] * dis
    y += dy[move_dir] * dis

print(x,y)