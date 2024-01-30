n,k,t=input().split()
n=int(n)
k=int(k)
arr=[]
for _ in range(n):
    string=input()
    # string=list(string)
    if t in string:
        arr.append(string)


arr.sort()
print(arr[k-1])