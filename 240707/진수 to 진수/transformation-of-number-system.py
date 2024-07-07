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
    if num < b:
        li.append(num)
        break   # num이 b보다 작으면 변환 완료, while문을 종료
    
    li.append(num % b)   # 나머지를 리스트에 추가
    num = num // b   # num을 b로 나눈 몫으로 업데이트
for i in li[::-1]:
    print(i, end='')