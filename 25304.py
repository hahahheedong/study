# X 입력 및 int로 변환
# N 입력 및 int로 변환
# c_list  생성
# N반복
#     a, b 입력 및 int 변환, split
#     a * b 를 계산후 c에 할당, 
#     a * b의 총액 합산 (리스트 내 모든 값 더하기)
# if문으로 출력문 작성


X = int(input())
N = int(input())

c_list = []
for i in range(N):
    s_list = list(map(int, input().split()))
    
    a = s_list[0]
    b = s_list[1]

    c = a * b
    c_list.append(c)
    
    total = 0
    for j in range(len(c_list)):
        total = total + c_list[j]
    # c_list = [100000, 60000, 60000, 40000]
    # for cost in c_list:
    #     total += cost

if total == X:
    print("Yes")
else:
    print("No")


"""
cost = int(input()) # 총 금액
c = int(input()) # 총 구매 개수

for i in range(c):
    a, b = map(int,input().split())
    cost -= a*b
print("Yes" if cost == 0 else "No" )
"""


"""
import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
result = 0

for _ in range(N):
    temp1, temp2 = map(int, sys.stdin.readline().split())
    result += temp1 * temp2

if(result == X):
    print("Yes")
else:
    print("No")
"""