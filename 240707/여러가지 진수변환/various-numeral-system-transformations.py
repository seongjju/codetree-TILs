n,b = map(int,input().split())

arr=[]
if b ==4:
    while True:
        if n==0 or n==1 or n ==2 or n== 3:
            arr.append(n)
            break
        if n%4==1:
            arr.append(1)
            n=n//4
        elif n%4==2:
            arr.append(2)
            n=n//4
        elif n%4==3:
            arr.append(3)
            n=n//4
        else:
            arr.append(0)
            n=n//4    
else:
    while True:
        if n==0 or n==1 or n ==2 or n== 3 or n==4 or n ==5 or n== 6 or n==7:
            arr.append(n)
            break
        if n%8==1:
            arr.append(1)
            n=n//8
        elif n%8==2:
            arr.append(2)
            n=n//8
        elif n%8==3:
            arr.append(3)
            n=n//8
        elif n%8==4:
            arr.append(4)
            n=n//8 
        elif n%8==5:
            arr.append(5)
            n=n//8  
        elif n%8==6:
            arr.append(6)
            n=n//8              
        elif n%8==7:
            arr.append(7)
            n=n//8  
        else:
            arr.append(0)
            n=n//8  
for i in arr[::-1]:
    print(i,end = '')