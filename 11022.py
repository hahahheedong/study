# T 입력 및 int로 변환
# T번 반복
#     A, B 입력 및 int로 변환
#     "Case #x: A + B = C" 해당 형식으로 출력

T = int(input())

# number = 0
for number in range(1,T+1):
    A, B = list(map(int, input().split()))
    C = A + B

    # number = number + 1

    print(f"Case #{number}: {A} + {B} = {C}")

    # print(f"Case #{i+1}: {a} + {b} = {a+b}")

# range
# range(a=0, b=T, c=1)
# a = 시작지점
# b = 종료지점
# c = 증가량
# 
# 열린구간 (), 닫힌구간 []
# (0, 10)
# [0, 10]
# (0, 10]
# [0, 10)



