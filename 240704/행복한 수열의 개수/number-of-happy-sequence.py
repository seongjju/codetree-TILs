a,b=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(a)]


def fun(a,b,arr):
    cnt=0
    for r in range(0,a):
        result = 1
        for c in range(1,a):
            if arr[r][c] == arr[r][c-(b-1)]:
                result +=1
            else:
                if result >= b:
                    cnt+=1
                result = 1
        if result >= b:
            cnt+=1

    for c in range(0,a):
        result = 1
        for r in range(1,a):
            if arr[r][c] == arr[r-(b-1)][c]:
                result +=1
            else:
                if result >= b:
                    cnt+=1
                result = 1
        if result >= b:
            cnt+=1

    return cnt

re = fun(a,b,arr)
print(re)