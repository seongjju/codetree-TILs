def fun():
    n=input()
    intn=int(n)
    if intn%2==0 and (intn%10 + intn//10)%5==0:
        return "Yes"
    else:
        return "No"

print(fun())