n=int(input())

for i in range(n):
    direction,dis = map(int,input().split())

if direction =='W':
    nx,ny = x-1,y

elif direction =='S':
    nx,ny = x,y-1


elif direction =='N':
    nx,ny = x,y+1
 
else:
    nx,ny = x+1,y
 

dir_num = 2 # 주어진 방향이 서쪽인 경우
x, y = 1, 5 # 현재 위치가 (1, 5)인 경우

if dir_num == 0:
    nx, ny = x + 1, y
elif dir_num == 1:
    nx, ny = x, y - 1
elif dir_num == 2:
    nx, ny = x - 1, y
else:
    nx, ny = x, y + 1


dir_num = 2 
x, y = 1, 5
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

nx, ny = x + dx[dir_num], y + dy[dir_num]