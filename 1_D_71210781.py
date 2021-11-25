input = input("Masukan string : ")

# if type(input) != str():
#     angka = int(input)
#     if (angka % 2 == 0):
#         res = angka / 2
#         print(res)
#     else:
#         res = (angka + 5) / 2
#         print(res)

# else:
#     print(input,"adalah string")

# def reverse(string): 
#     return string[::-1]

# def numeric(angka):
#     num = int(angka)
#     if num % 2 == 0:
#         res = num / 2
#         print(res)
#     else:
#         res = (num + 5) / 2
#         print(res)

# print(numeric(input))

def result(input):
    # if type(string) == str:
    #     print(string[::-1])
    num = int(input)
    if num % 2 == 0:
        res = input / 2
        print(res)
    else:
        res = (num + 5) / 2
        print(res)
if type(result()) == int:
    print(result())
else:
    print(input[::-1])