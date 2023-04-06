# 함수 생성 0 0이 들어올 때까지의 개수 세기
# 세로길이 만큼 반복 (A, B가 둘 다 0 일때 까지)
#     A, B 입력 및 int 로 변환
#     A + B 출력
#     A, B 둘 다 0일때, break 

def H(*args):
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0:
        # flag (플래그)
        return False
    print(a + b)
    # return None


# for i in ():
#     A, B = list(map(int, input().split()))
#     if A == 0 and B == 0:
#         break
#     print(f"{A+B}")

while True:
    # A, B = list(map(int, input().split()))
    # if A == 0 and B == 0:
    #     break
    # print(f"{A+B}")
    # := 왈루스 연산자 
    isContinue = H()
    if not isContinue:
        break

    # True is True = True
    # True is False  = not True
    # if (True, False)
    # if 1 is 2