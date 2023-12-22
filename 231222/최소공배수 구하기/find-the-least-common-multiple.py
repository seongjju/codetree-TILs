a, b = map(int, input().split())
lists = []

for i in range(max(a, b), a * b + 1, max(a, b)):
    if i % a == 0 and i % b == 0:
        lists.append(i)

result = min(lists)
print(result)