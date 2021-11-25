# if type(input) == int:
#     print(input,"adalah string")
  
# else:
#     angka = int(input)
#     if (angka % 2 == 0):
#         res = angka / 2
#         print(res)
#     else:
#         res = (angka + 5) / 2
#         print(res)

word = input("Masukan sebuah kata/kalimat : ")
char = input("Masukan karakter yang ingin disisipkan : ")

def sisip():
    x = word.upper()
    y = word.title()
    print(char.join(list(x)))
    print(char.join(y.split()))

sisip()