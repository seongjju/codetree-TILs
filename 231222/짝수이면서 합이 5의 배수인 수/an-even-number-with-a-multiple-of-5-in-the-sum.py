n=int(input())
a= n//10
b= n%10
def cal(n):
    if n%2 ==0 and (a+b)%5 ==0:
        return "Yes"
    else:
        return "No"
print(cal(n))