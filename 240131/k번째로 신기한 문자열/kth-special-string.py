n,k,t=input().split()
n=int(n)
k=int(k)
arr=[]
for _ in range(n):
    string=input()
    # string=list(string)
    if t[0] == string[0] and t[1] == string[1]:
        arr.append(string)


arr.sort()
print(arr[k-1])