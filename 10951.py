
# N번 반복
#     A, B 입력 및 int로 변환
#     입력 값이 없다면
#         break  
#     print(A + B)

while True:
    try:
        A, B = list(map(int, input().split()))
        print(A + B)
    except EOFError:
        break
    # EOF (End of file)