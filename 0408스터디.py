a, d, n = map(int, input().split()) # 시작값, 등차, 몇 번째인지 입력
result = a + (n - 1) * d # n번째 수(result) = 시작값 + (n-1) * 등차
print(result) # n번째 수(result) 출력


a, d, n = map(int, input().split()) # 시작값, 등차, 몇 번째인지 입력
i = 0
result = a
while i != n-1:
    result = result + d
    i += 1

print(result)


a, r, n = map(int, input().split())
result = a * r ** (n-1)

print(result)
    
a, r, n = map(int, input().split())
i = 0
result = a
while i != n-1:
    result = result * r
    i += 1

print(result)
