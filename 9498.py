# 시험 점수 받아
# 만약 90 <= S 이면 A
# 80 <= S 이면 B 
# 70 <= S 이면 C
# 60 <= S 이면 D 
# else F

S = int(input())

if S >= 90:
    print("A")
elif S >= 80:
    print("B")
elif S >= 70:
    print("C")
elif S >= 60:
    print("D")
else:
    print("F")