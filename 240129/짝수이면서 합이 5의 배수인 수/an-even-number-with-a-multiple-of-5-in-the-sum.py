n=int(input())
def fa(a):
    a1=a%10
    a2=a//10
    if a%2 ==0 and (a1+a2)%5==0:
        print("Yes")

    else:
        print("No")

fa(n)