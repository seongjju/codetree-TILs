m1, d1, m2, d2 = map(int,input().split())
num=0 # 몇번 등장하는지
cnt=0 
month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
a = input()
day = [ 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']

while True:
    if m1 == m2 and d1 == d2:
        break

    if d1 == month[m1]:
        m1+=1
        d1=0
    cnt+=1
    d1+=1


x=0
#월요일기준
# for i in range(len(day)):
    # if a == day[i]:
day_a=0
for i in range(len(day)):
    if a == day[i]:
        day_a = i

if cnt%7 >= day_a:
    x+=1

print(cnt//7 + x)

#화요일기준
day[cnt%7 + 1]

# count = 0
# for i in range(len(day)):
#     if a== day[i]:
#         count = cnt//7 
#         index = cnt%7 +i
# print(count)
# #월요일일때 횟수