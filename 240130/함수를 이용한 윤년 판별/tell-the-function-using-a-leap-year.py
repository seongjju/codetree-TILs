def yoon(n):
    if n%4==0 and n%100 ==0 and n%400 ==0:
        return True
    elif n%4==0 and n%100 ==0:
        return False
    elif n%4==0:
        return True
    else:
        return False



x=int(input())
if yoon(x)==True:
    print("true")
else:
    print("false")