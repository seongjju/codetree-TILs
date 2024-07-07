n= input()
arr=[]
for i in range(len(n)):
    arr.append(n[i])
num=0
for i in range(len(n)):
    num = num *2 + int(arr[i])

num *=17 #323

li=[]
while True:
    if num == 1 or num == 0:
        li.append(num)
        break
    if num%2 ==0:
        li.append(0)
        num= num//2
    else:
        li.append(1)
        num= num//2

for i in li[::-1]:
    print(i, end='')