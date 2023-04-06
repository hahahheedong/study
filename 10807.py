#N입력, int로 변환
#N번 반복
#   data입력, int로 변환
#   data list로 변환
#   v입력, int로 변환 (리스트 x)
#   data_list에 v의 갯수  출력



# N = int(input())

# for i in range(N):
#     # data_list = []
#     # data_list.append(list(map(int, input().split())))
#     # print(data_list)
#     # 리스트 안에 리스트 형식으로 출력 ㅠㅠ
   
#     data_list = []
#     for c in input().split():
#         data_list.append(int(c))

#     v = int(input())
    
#     print(data_list.count(v))
#     break



"""
n = int(input())
n_list = list(map(int,input().split()))
v = int(input())

print(n_list.count(v))
"""



# N = int(input())

# for i in range(N):
#     N_list = list(map(int, input().split()))
#     print(N_list)

#     v = int(input())

#     print(N_list.count(v))
#     break

N = int(input())
N_list = list(map(int, input().split()))
v = int(input())
print(N_list.count(v))
