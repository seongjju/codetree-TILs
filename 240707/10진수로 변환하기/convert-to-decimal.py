n=input()
arr=[]
for i in range(len(n)):
    arr.append(n[i])

# arr = 11101
num=0
for i in range(len(n)):
    num = num*2 + int(arr[i])

print(num)