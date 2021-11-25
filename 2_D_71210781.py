input = input("Masukan string : ")

if type(input) == int:
    print(input,"adalah string")
  
else:
    angka = int(input)
    if (angka % 2 == 0):
        res = angka / 2
        print(res)
    else:
        res = (angka + 5) / 2
        print(res)