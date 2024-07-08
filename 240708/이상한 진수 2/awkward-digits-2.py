arr = input().strip()  # 입력된 문자열을 양쪽 공백을 제거
a = [int(char) for char in arr]  # 각 문자를 정수로 변환하여 리스트에 저장


maxs=0
n=0
for i in range(len(a)):
    # for j in range(i+1,len(a)):
    if a[i]==0:
        a[i] = 1
        break
arr2=''
for i in a:
    arr2 = arr2+str(i)
x=int(arr2)
int_x=int(x)
sums=0
for i in range(len(arr2)):
    sums = sums*2 + int(a[i])

print(sums)