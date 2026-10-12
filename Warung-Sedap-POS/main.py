daftar = []
total = 0

def menu():
  print(f'{"Soto babat":^15}')
  print("\n",f'{"[Menu Warung Sedap]":^39}')
  print(f'\n{"="*13}\n|{"Dimakan":^11}|\n{"="*40}')
  print(f'|1 | {"Nasgor Jawa":<23} {"|Rp.26,000|"}')
  print(f'|2 | {"Mie Goreng":<23} {"|Rp.19,000|"}')
  print(f'|3 | {"Sate Manis":<23} {"|Rp.7,000 |"}')
  print(f'|4 | {"Rawon":<23} {"|Rp.18,000|"}')
  print(f'|5 | {"Sop Merah":<23} {"|Rp.14,000|"}')
  print(f'{"="*40}\n\n{"="*13}\n|{"Diminum":^11}|\n{"="*40}')
  print(f'|6 | {"Teh":<23} {"|Rp.6,000 |"}')
  print(f'|7 | {"Jahe":<23} {"|Rp.10,000|"}')
  print(f'|8 | {"Sinom":<23} {"|Rp.7,000 |"}')
  print(f'|9 | {"Air Mineral":<23} {"|Rp.4,000 |"}')
  print(f'|10| {"Soda Gembira":<23} {"|Rp.12,000|"}')
  print(f'{"="*40}',"\n")
#   time.sleep(1)
  start()

def pilih():
    global daftar
    num = (input("Pilih nomor menu yang ingin dipilih! "))
    if num == "1":
        daftar.append(["Nasgor Jawa", 26000])
    elif num == "2":
        daftar.append(["Mie Goreng", 19000])
    elif num == "3":
        daftar.append(["Sate Manis", 7000])
    elif num == "4":
        daftar.append(["Rawon", 18000])
    elif num == "5":
        daftar.append(["Sop Merah", 14000])
    elif num == "6":
        daftar.append(["Teh", 6000])
    elif num == "7":
        daftar.append(["Jahe", 10000])
    elif num == "8":
        daftar.append(["Sinom", 7000])
    elif num == "9":
        daftar.append(["Air Mineral", 4000])
    elif num == "10":
        daftar.append(["Soda Gembira", 12000])
    else:
        print("Error")
        pilih()
    print("Pesanan anda berhasil dipilih.\n",daftar,"\n")
    start()

def hapus():
    global daftar
    print(daftar)
    indeks = int(input("Masukan nomor pesanan yang ingin dihapus! "))
    if indeks == 1:
        del daftar[indeks - 1]
    else:
        print("Error")
        hapus()
        
    print("\nPesanan anda berhasil dihapus.\n",daftar,"\n")
    start()

def view():
    global daftar
    for x in range(len(daftar)):
        nomor = x + 1
        print(str(nomor)+".", daftar)

def bayar():
    global daftar, total
    # print(daftar)
    for x in range(len(daftar)):
        nomor = x + 1
        # nama = daftar[x][0]
        # harga = str(daftar[x][1])
        # # word = f'{daftar[x][0], "| Rp.", str(daftar[x][1]):^40}'
        # word = ({:^20}"|")
        print(str(nomor)+".", "{:<20}|{:>20}.format(daftar[x][0], str(daftar[x][1])")
        total += daftar[x][1]
    print("\nTotal pesanan mu adalah", total,".")

def start():
  print("1. Daftar Pesanan \n2. Pilih Pesanan \n3. Hapus Pesanan \n4. Lihat Pesananku \n5. Bayar \n6. Keluar")
  choice = input("Masukan angka dari opsi diatas: ")
  if choice == "1":
    menu()
  elif choice == "2":
    print()
    pilih()
  elif choice == "3":
    print()
    hapus()
  elif choice == "4":
    view()
    # print("\n",daftar,"\n")
    start()
  elif choice == "5":
    print()
    bayar()
  elif choice == "6":
    print("Terima kasih telah mengunjungi kami.")
    exit()
  else:
      print("Error\n")
      start()
start()