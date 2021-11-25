input = input("Masukan string : ")

# def result(input):
#     # if type(string) == str:
#     #     print(string[::-1])
#     num = int(input)
#     if num % 2 == 0:
#         res = input / 2
#         print(res)
#     else:
#         res = (num + 5) / 2
#         print(res)
# if type(result()) == int:
#     print(result())
# else:
#     print(input[::-1])

def rev(string):
    res = string[::-1]
    print(res)

if input is not str:
    rev(input)

else:
    if input % 2 == 0:
        print(input / 2)
    else:
        print((input + 5) / 2)

# if input in str: