# a, b = list(map(int, input().split()))

# A = []
# for i in input().split():
#     A.append(int())

# B = []
# for j in input().split():
#     B.append(int())
    
# print(A + B)

def extract_ints(my_str):
    result = []
    for c in my_str.split():
        result.append(int(c)) 
    return result

def asd(qwe):
    a = qwe[0]
    b = qwe[1]
     
    print(a + b)
    # return None
    

T = int(input())

for i in range(T):
    data = input()

    temp = extract_ints(data)

    asd(temp)

# '''
# Traceback (most recent call last):
#   File "C:\Users\문희정\Documents\python\10950.py", line 23, in <module>
#     for i in temp[0]:
# TypeError: 'int' object is not iterable

# Traceback (most recent call last):
#   File "C:\Users\문희정\Documents\python\10950.py", line 15, in <module>
#     for i in T:
# TypeError: 'int' object is not iterable

# object = 살아있는 객체
# 살아있다 = 프로그램 실행중에 저장된 데이터
# iterable = 반복할수 있는 (다음 값을 요청했을때 줄 수 있는가)
# '''

# 5
# 1 1
#       2
# 2 3
#       5
# 3 4
#       7
# 9 8
#       17
# 5 2
#       7