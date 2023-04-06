#n입력, int로 변환
#1~n까지 더하기 반복
#   a = a+i

n = int(input())

a = 0
for i in range(1,n+1):
    a = a + i
    # a += i 

print(a)