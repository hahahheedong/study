# 빈 리스트 생성
# 5번 반복
#     데이터 입력 및  str로 변환
#     각 문자열에 ",".join 
#     ","로 split
#     리스트 안에 넣기
# #<0 0, 1 0, 2 0, ...>순으로 출력하는 로직 생성
# i를 15번 반복
#     j를 5번 반복
#         글자가 없다면
#             pass
#     리스트[j][i] 출력


char = []
data = []

for num in range(5):
    d = str(input()) #  -> list("ABCDE")
    char.append(",".join(d)) # ["A,B,C,D,E", ]
    data.append(char[num].split(",")) # ["A", "B", "C", "D"]
    
print("실제데이터: ")
for row in data:
    print(row)

result = []

for i in range(15):
    for j in range(5):
        try:
            result.append(data[j][i])
        except IndexError:
            pass

print("결과: ")
print("".join(result))

