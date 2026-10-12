import os
import random
import time
# print("="*30)
# print(f'{"Hello world":^30}{"Saya gamer":^30}')
# print("="*60)
# print(f'{"welcome to my world!":<25}\n{"this is my playground":<25}')
# print("="*30)
# print("{:>30} | {:<15}".format("welcome to my world!", "Hello World"))
# print("="*30)

# print(f'{"[Menu Warung Sedap]":^39}')
# print(f'\n{"="*13}\n|{"Dimakan":^11}|\n{"="*39}')
# print(f'|1| {"Nasgor Jawa":<23} {"|Rp.26,000|"}')
# print(f'|2| {"Mie Goreng":<23} {"|Rp.19,000|"}')
# print(f'|3| {"Sate Manis":<23} {"|Rp.7,000 |"}')
# print(f'|4| {"Rawon":<23} {"|Rp.18,000|"}')
# print(f'|5| {"Sop Merah":<23} {"|Rp.14,000|"}')
# print(f'{"="*39}\n\n{"="*13}\n|{"Diminum":^11}|\n{"="*39}')
# print(f'|1| {"Teh":<23} {"|Rp.6,000 |"}')
# print(f'|2| {"Jahe":<23} {"|Rp.10,000|"}')
# print(f'|3| {"Sinom":<23} {"|Rp.7,000 |"}')
# print(f'|4| {"Air Mineral":<23} {"|Rp.4,000 |"}')
# print(f'|5| {"Soda Gembira":<23} {"|Rp.12,000|"}')
# print(f'{"="*39}')

# print(f'{"*"*1:^30}\n{"*"*3:^30}\n{"*"*5:^30}\n{"*"*7:^30}\n{"*"*9:^30}')
# print(f'{"*":^30}\n{"*":^30}\n{"*":^30}')

# variabel = input("Masukanlah nama! ")

# if variabel.lower() == "marquis":
# if variabel.strip() or variabel.lower() == "marquis":
#   print("benar")
# else:
#   print("salah")

# print(
#     " 1. Penjumlahan (+)\n 2. Pengurangan (-)\n 3. Perkalian (x)\n 4. Pembagian (:)"
# )
# operator = input("Pilih operator! ")
# x = int(input("Masukan angka pertama! "))
# y = int(input("Masukan angka kedua! "))
# if (operator == "+" or operator == "1" or operator.lower() == "penjumlahan"):
#   z = x + y
# elif (operator == "-" or operator == "2" or operator.lower() == "pengurangan"):
#   z = x - y
# elif (operator == "*" or operator == "3" or operator.lower() == "perkalian"):
#   z = x * y
# elif (operator == "/" or operator == "4" or operator.lower() == "pembagian"):
#   z = x / y
# else:
#   print("Error")
#   exit()
# print("Hasilnya adalah ", z)

# def nilai(a):
#   if a > 100 or a < 0:
#     return True
#   else:
#     return False

# def hitung():
#   mat = int(input("Masukan nilai matematika = "))
#   if nilai(mat):
#     hitung()

#   bio = int(input("Masukan nilai biologi = "))
#   if nilai(bio):
#     hitung()

#   c = (mat + bio) / 2

#   c = int(c)
  
#   print("Nilai rata-rata kamu adalah", c)
#   exit()

# hitung()

# def nilai(a):
#   if a > 100 or a < 0:
#     return True
#   else:
#     return False

# def start():
#   print()
  
#   bin = int(input("Nilai Bahasa Indonesia: "))
#   if nilai(bin):
#     print("Error, please retry again!")
#     start()
  
#   big = int(input("Nilai Bahasa Inggris: "))
#   if nilai(big):
#     print("Error, please retry again!")
#     start()
#   mand = int(input("Nilai Bahasa Mandarin: "))
#   if nilai(mand):
#     print("Error, please retry again!")
#     start()
#   baja = int(input("Nilai Bahasa Jawa: "))
#   if nilai(baja):
#     print("Error, please retry again!")
#     start()
#   pak = int(input("Nilai Agama: "))
#   if nilai(pak):
#     print("Error, please retry again!")
#     start()
#   ipa = int(input("Nilai IPA: "))
#   if nilai(ipa):
#     print("Error, please retry again!")
#     start()
#   ips = int(input("Nilai IPS: "))
#   if nilai(ips):
#     print("Error, please retry again!")
#     start()
#   mat = int(input("Nilai Matematika: "))
#   if nilai(mat):
#     print("Error, please retry again!")
#     start()
#   ppkn = int(input("Nilai PPKN: "))
#   if nilai(ppkn):
#     print("Error, please retry again!")
#     start()
#   tik = int(input("Nilai TIK: "))
#   if nilai(tik):
#     print("Error, please retry again!")
#     start()
#   seni = int(input("Nilai Kesenian: "))
#   if nilai(seni):
#     print("Error, please retry again!")
#     start()
#   mus = int(input("Nilai Music: "))
#   if nilai(mus):
#     print("Error, please retry again!")
#     start()

#   x = bin + big + pak + ipa + ips + mat + ppkn + mand + tik + seni + mus + baja
#   avg = x / 12

#   if avg > 90:
#     print("Nilai kamu adalah A")
#     exit()
#   elif avg > 80:
#     print("Nilai kamu adalah B")
#     exit()
#   elif avg > 70:
#     print("Nilai kamu adalah C")
#     exit()
#   elif avg > 60:
#     print("Nilai kamu adalah D")
#     exit()
#   elif avg > 50:
#     print("Nilai kamu adalah E")
#     exit()
#   else:
#     print("Nilai kamu adalah F")
#     exit()
    
# start()


# [PIZZA MAKER]

# value = 0
# size = input("Ukuran pizza? S / M / L ? ")
# if size.lower() == "s":
#   value += 5
# elif size.lower() == "m":
#   value += 9
# elif size.lower() == "l":
#   value += 13
# else:
#   print("Error")
#   exit()

# cheese = input("Cheese? Y / N ? ")
# if cheese.lower() == "y":
#   value += 3

# sausage = input("Sausage? Y / N ? ")
# if sausage.lower() == "y":
#   value += 3

# paperoni = input("Paperoni? Y / N ? ")
# if paperoni.lower() == "y":
#   value += 3

# pickle = input("Pickle? Y / N ? ")
# if pickle.lower() == "y":
#   value += 3

# jamur = input("Jamur? Y / N ? ")
# if jamur.lower() == "y":
#   value += 3

# print("Harga pizza kamu adalah", value, "k")


# for i in range(10):
#   if i != 0:
#     print(i)
#   time.sleep(1)

# print("10 \nStart!")

# time.sleep(5)
# print()

# x = 10
# while x > 0:
#   print(x)
#   x -= 1
#   time.sleep(1)
# print("Stop!")

# guessing game

# x = random.randint(1,10)
# y = -1
# c = 5
# print("Masukan angka dari 1 sampai 50. Setelah 5 kali salah angka akan di riset")
# while y != x and c != 0:
#   y = int(input("Masukan angka! "))
#   c -= 1
#   if y == x:
#     a = c + 5
#     print("Kamu benar! Kamu menggunakan", a , "kesempatam!")
#   elif y != x and c == 0:
#     print("Kamu gagal. Angka telah di riset")
#     c = 5
#     x = random.randint(1,50)
#   else:
#     if y > x:
#       print("Angka yang kamu masukan terlalu besar!   Kamu memiliki", c, "kesempatan lagi!")
#     elif y < x:
#       print("Angka yang kamu masukan terlalu kecil!   Kamu memiliki", c, "kesempatan lagi!")

# pengunaan continue nge skip angka ke 10
# num = 0
# while num < 20:
#   num += 1
#   if num == 10:
#     continue
#   print(num)

# 3 tipe for loop
# for k in range(7):
# for k in range(1, 7):
# for k in range(1, 9, 3):
  # print("="*k)
  # print(k)

# trapesium
# panjang = int(input("Masukan awal panjang! "))
# tinggi = int(input("Masukan tinggi! "))
# kemiringan = int(input("Masukan kemiringan! "))
# for x in range(panjang, tinggi, kemiringan):
#   print("*"*x)

# RPS
# print("1. Rock \n2. Paper \n3. Scissors")
# x = random.randint(1, 3)
# if x == 1:
#   z = "rock!"
# elif x == 2:
#   z = "paper!"
# elif x == 3:
#   z = "scissors!"
# else:
#   print("Error")
#   exit()
# y = int(input("Input your number of choice: "))
# if not 1 or 2 or 3:
#   print("Error")
#   exit()
# if x == y:
#   print("Tie! Computer choose", z)
# elif (x == 1 and y == 2) or (x == 2 and y == 3) or (x == 3 and y == 1):
#   print("You Win! Computer choose", z)
# else:
#   print("You Lose! Computer choose", z)

# print 7x
# for x in range(6):
#   print(psst)

# setelah print ke 7, berhenti
# x = 0
# while x < 10:
#   print("psst")
#   x += 1
#   if x == 7:
#     break
#   else:
#     continue

# square
# length = int(input("Masukan panjang persegi! "))
# for x in range(length):
#     print(" *" * length)

#blh tupat
# length = int(input("Masukan tinggi belah ketupat! "))
# length_a = int(length / 2 + 1)

# quantity = 1
# for x in range(length_a):
#     print(f'{"* "*quantity:^75}')
#     quantity += 2

# quantity -= 4
# for x in range(length_a):
#     print(f'{"* "*quantity:^75}')
#     quantity -= 2

for x in range(7):
    a = 7-x
    print(" "*a, "="*x, "="*x, " "*a)
for x in range(7):
    a = 7-x
    print(" "*x, "="*a, "="*a, " "*x)
