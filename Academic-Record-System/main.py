class data:
    def __init__(self, nama, usia, jenis_kelamin, nilai_bahasa, nilai_matematika, nilai_fisika):
        self.nama = nama
        self.usia = usia
        self.jenis_kelamin = jenis_kelamin
        self.nilai_bahasa = nilai_bahasa
        self.nilai_matematika = nilai_matematika
        self.nilai_fisika = nilai_fisika

    def accept(self, nama, usia, jenis_kelamin, nilai_bahasa, nilai_matematika, nilai_fisika):
      insert = data(nama, usia, jenis_kelamin, nilai_bahasa, nilai_matematika, nilai_fisika)
      list.append(insert)

    def display(self, insert):
      print("Nama : ", insert.nama)
      print("Usia : ", insert.usia)
      print("Jenis Kelamin : ", insert.jenis_kelamin)
      print("Nilai Bahasa : ", insert.nilai_bahasa)
      print("Nilai Matematika : ", insert.nilai_matematika)
      print("Nilai Fisika : ", insert.nilai_fisika)
      print("\n")

    def search(self, nama):
      for i in range(len(list)):
        if(list[i].nama.lower() == nama.lower()):
          return i
      return None

    def delete(self, nama):
      i = insert.search(nama)
      if i is not None:
        del list[i]
        print("Data siswa berhasil dihapus")
      else:
        print("Siswa tidak ditemukan")

list = []
insert = data("", 0, "", 0, 0, 0)

while True:
  pil = input("\n1.Masukan data siswa\n2.Tunjukan data siswa\n3.Cari data siswa\n4.Hapus data siswa\n5.Revisi data siswa\n6.Keluar\n\nMasukan pilihan: ")
  if pil == "1":
    print("\nMasukan data siswa!")
    nama = input("Nama: ")
    while True:
      try:
        usia = int(input("Usia: "))
        break
      except:
        print("Invalid!")
    while True:
      jenis_kelamin = input("Jenis Kelamin (F / M): ")
      if jenis_kelamin.upper() == "F":
        jenis_kelamin = "Female"
        break
      elif jenis_kelamin.upper() == "M":
        jenis_kelamin = "Male"
        break
      else:
        print("Invalid!")
    while True:
      try:
        nilai_bahasa = int(input("Nilai Bahasa: "))
        if nilai_bahasa >= 0 and nilai_bahasa <= 100:
          break
        else:
          print("Invalid!")
      except:
        print("Invalid!")
    while True:
      try:
        nilai_matematika = int(input("Nilai Matematika: "))
        if nilai_matematika >= 0 and nilai_matematika <= 100:
          break
        else:
          print("Invalid!")
      except:
        print("Invalid!")
    while True:
      try:
        nilai_fisika = int(input("Nilai Fisika: "))
        if nilai_fisika >= 0 and nilai_fisika <= 100:
          break
        else:
          print("Invalid!")
      except:
        print("Invalid!")
    insert.accept(nama, usia, jenis_kelamin, nilai_bahasa, nilai_matematika, nilai_fisika)
    
  elif pil == "2":
    print("\nList of Students\n")
    if len(list) == 0:
        print("Tidak ada siswa yang terdaftar.")
    else:
        for i in range(len(list)):
            insert.display(list[i])
    input("Press any key to continue!")
    print("\n")
    
  elif pil == "3":
    nama = input("Nama : ")
    i = insert.search(nama)
    if i is not None:
      print("\nSiswa ditemukan:")
      insert.display(list[i])
    else:
      print("\nSiswa tidak ditemukan")
    input("Press any key to continue!")
    print("\n")
    
  elif pil == "4":
    nama = input("Nama : ")
    insert.delete(nama)
    
  elif pil == "5":
    pass
    
  elif pil == "6":
    exit()
    

#   # Function to create and append new student
#   def accept(self, Name, age, bahasa, fisika):
#     ob = Student(Name, age, bahasa, fisika)
#     ls.append(ob)

#   # Function to display student details
#   def display(self, ob):
#     print("Name : ", ob.name)
#     print("Age : ", ob.age)
#     print("Bahasa : ", ob.bahasa)
#     print("Fisika : ", ob.fisika)
#     print("\n")

#   def search(self, rn):
#     for i in range(len(ls)):
#       if(ls[i].name.lower() == rn.lower()):
#         return i

#   # Delete Function
#   def delete(self, rn):
#     i = obj.search(rn)
#     del ls[i]

#   # Update Function
#   def update(self, rn, name, age, bahasa, fisika):
#     i = obj.search(rn)
# # 		roll = name
#     ls[i].name = name
#     ls[i].age = age
#     ls[i].bahasa = bahasa
#     ls[i].fisika = fisika

# ls = []
# obj = Student("", 0, 0, 0)

# while True:
#     print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")
#     ch = int(input("Enter choice: "))
#     if(ch == 1):

#         print("Please fill!")
#         name = input("Name : ")
#         age = int(input("Age : "))
#         bahasa = int(input("Bahasa : "))
#         fisika = int(input("Fisika : "))
#         obj.accept(name, age, bahasa, fisika)
#         input("Data has been saved, press any key to continue!")
#         print("\n")
#         # obj.accept("B", 2, 90, 90)
#         # obj.accept("C", 3, 80, 80)

#     elif(ch == 2):
#         print("\n")
#         print("\nList of Students\n")
#         for i in range(len(ls)):
#           obj.display(ls[i])

#         input("Press any key to continue!")
#         print("\n")

#     elif(ch == 3):
#         name = input("Name : ")
#         print("\n Student Found, ")
#         s = obj.search(name)
#         obj.display(ls[s])

#         input("Press any key to continue!")
#         print("\n")

#     elif(ch == 4):
#         name = input("Name : ")
#         print("\n Student Found, ")
#         s = obj.search(name)
#         del(ls[s])

#     elif(ch == 5):
#         name = input("Name : ")
#         print("\n Student Found, ")
#         s = obj.search(name)
#         # obj.update(s)
#         del(ls[s])
#         print("Please fill!")
#         # name = input("Name : ")
#         age = int(input("Age : "))
#         bahasa = int(input("Bahasa : "))
#         fisika = int(input("Fisika : "))
#         obj.accept(name, age, bahasa, fisika)
#         input("Data has updated, press any key to continue!")
#         print("\n")

#     else:
#         print("Program Stopped")
#         break
#         exit()

# list = [1,2,3,4,7]
# for i in range(len(list)):