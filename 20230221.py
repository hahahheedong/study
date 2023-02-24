# def sum(*a):
#     result = 0

#     def sample():
#         print(result)

#     for i in a:
#         sample()
#         result = result + i
    
#     return result


# # print("결과창")
# print(f"SUM이 리턴한 값은: {sum(5, 6, 7)}")


# def birth(my_list):
#     for i in my_list:
#         print(i)
#         if i == 94:
#             print(f"{i} 찾았습니다")
#             return "출생"
#     return "못찾았습니다"

# print(birth(range(0, 6)))


# def multiply(a=1, b=1):
#     return a * b

# print(multiply(4, 5))

# a = 1 
# def vartest(b):
#     global a
#     a = a +1 
#     return 

# vartest(a)
# print(a)

def sum(a, b):
    return a + b

print(sum(4, 5))

add = lambda a, b: a + b

print(add(5, 6))

print("Hello World!")