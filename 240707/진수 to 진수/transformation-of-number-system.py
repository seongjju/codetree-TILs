a,b = map(int,input().split())
# 8 -> 10 -> 2
# 8->9 
n= input()
arr=[]
for i in range(len(n)):
    arr.append(n[i])
num=0
for i in range(len(n)):
    num = num *a + int(arr[i])

# 9->1001
li=[]
while True:
    if num <b:
        li.append(num)
        break
    for i in range(b):
        if num ==1:
            break
        if num%b ==i+1:
            li.append(i+1)
            num= num//b
        else:
            li.append(0)
            num = num//b
            
for i in li[::-1]:
    print(i, end='')