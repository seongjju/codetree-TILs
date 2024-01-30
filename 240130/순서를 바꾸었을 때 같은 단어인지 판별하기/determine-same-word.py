arr1 = input()
arr2 = input()

# 문자열을 리스트로 변환
arr1 = list(arr1)
arr2 = list(arr2)

# 리스트를 정렬
arr1.sort()
arr2.sort()

# 정렬된 리스트가 동일한지 확인
if arr1 == arr2:
    print("Yes")
else:
    print("No")