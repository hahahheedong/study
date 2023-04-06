# 바구니 N개(1~N까지 번호 있음)
# N개의 바구니 안에 각 1개의 공 (바구니 번호 = 공 번호)
# M번 반복
#     2개 바구니를 선택 후 서로 교환
# 각 바구니에 어떤 공이 들어 있는지 출력

# basket = N  
# B_dic = {basket1:ball1, basket2:ball2, basket3:ball3, ...}

# for c in range(5):
#     B_dic[i+1]


N, M = map(int,input().split()) # 1 2
# a = 1
# b = 2
# a, b = (1, 2)
# a, b = ######
# 제너레이터


dic = {}# 바구니 : 공 


for num in range(1,N+1):
    dic[num] = num

dic_i = {}
dic_j = {}
for _ in range(M):
    i, j = list(map(int, input().split()))
    dic_i[i] = dic[i] # dic_i  dic[i]
    dic_j[j] = dic[j]
    dic[i] = dic_j[j]
    dic[j] = dic_i[i]
    del dic_i[i]
    del dic_j[j]
    
    dic[i], dic[j] = dic[j], dic[i]

for f in dic.values():
    print(f, end =" ")
