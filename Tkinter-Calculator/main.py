import tkinter as tk
import random
import time

# words = [
#     'function', 'variable', 'python', 'snake', 'codehs', 'karel', 'dog',
#     'turtle', 'tracy'
# ]
# word = random.choice(words)

# def cetak():
    # '''fungsi ini akan dipanggil oleh tombol'''
    # pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, salam kenal!"
    # pesan = "Halo " + nmdepan.get() + " " + nmbelakang.get() + ", salam kenal!"
    # showinfo(title="Halo Bro!",message=pesan)
    # lblresult.configure(text=pesan)

# root.resizable(False,False)

# nmdepan = tk.StringVar()
# nmbelakang = tk.StringVar()

# label_left = tk.Label(frame, text="Left")
# label_left.grid(row=0, column=0, sticky="w")

# lf01 = tk.Label(frame,text='Text', justify="left", anchor="w")
# lf01.grid(row=0,column=0,padx=0, pady=20)

# lblnamadepan = tk.Label(frame, text="Nama Depan:", bg="ivory")
# lblnamadepan.grid(row=1, column=0, sticky = "w")
# lblnamadepan.place(x=75, y=80)

# namadepan = tk.Entry(frame, bg = "ghostwhite", width = 18, textvariable = nmdepan)
# namadepan.grid(row=1,column=1)

# lblnamabelakang = tk.Label(frame, text="Nama Belakang:", bg="ivory")
# lblnamabelakang.grid(row=2, column=0, sticky = "w")
# lblnamabelakang.place(x=75, y=80)

# namabelakang = tk.Entry(frame, bg = "ghostwhite", width = 18, textvariable = nmbelakang)
# namabelakang.grid(row=2,column=1)
# def cetak():
#   hasil = nomor1.get() + nomor2.get()
#   pesan = f"Jumlah dari {nomor1.get()} + {nomor2.get()} = {hasil}"
#   lblresult.configure(text=pesan)

def plus():
  hasil = nomor1.get() + nomor2.get()
  pesan = f"Jumlah dari {nomor1.get()} + {nomor2.get()} = {hasil}"
  lblresult.configure(text=pesan)
  New_Window()
def minus():
  hasil = nomor1.get() - nomor2.get()
  pesan = f"Jumlah dari {nomor1.get()} - {nomor2.get()} = {hasil}"
  lblresult.configure(text=pesan)
def multiply():
  hasil = nomor1.get() * nomor2.get()
  pesan = f"Jumlah dari {nomor1.get()} * {nomor2.get()} = {hasil}"
  lblresult.configure(text=pesan)
def divide():
  hasil = nomor1.get() / nomor2.get()
  pesan = f"Jumlah dari {nomor1.get()} / {nomor2.get()} = {hasil}"
  lblresult.configure(text=pesan)
def hitung():
    if operator.get() == 1:
        hasil = int(nomor1.get()) + int(nomor2.get()) 
    elif operator.get() == 2:
        hasil = int(nomor1.get()) - int(nomor2.get()) 
    elif operator.get() == 3:
        hasil = int(nomor1.get()) * int(nomor2.get()) 
    elif operator.get() == 4:
        hasil = int(nomor1.get()) / int(nomor2.get()) 
    lblresult.configure(text=hasil)
    
    
  
root = tk.Tk(screenName=None, baseName=None, className='Kalkulasi')
root.geometry('500x500')
root.configure(bg="white")

nomor1 = tk.IntVar()
nomor2 = tk.IntVar()
operator = tk.IntVar()
operator_void = tk.IntVar()

frame = tk.Frame(root, height=500, width=500)
# frame.geometry('900x900')
frame.configure(bg="ivory")
frame.grid()

lblnomor1 = tk.Label(frame, text="Angka 1:", bg="ivory")
lblnomor1.grid(row=1, column=0, sticky = "w")
# lblnomor1.place(x=5, y=5)
lblnomor1 = tk.Entry(frame, bg = "ghostwhite", width = 18, textvariable = nomor1)
lblnomor1.grid(row=1,column=1)
# lblnomor1.place(x=30, y=5)
lblnomor2 = tk.Label(frame, text="Angka 2:", bg="ivory")
lblnomor2.grid(row=2, column=0, sticky = "w")
# lblnomor2.place(x=5, y=30)
lblnomor2 = tk.Entry(frame, bg = "ghostwhite", width = 18, textvariable = nomor2)
lblnomor2.grid(row=2,column=1)
# lblnomor2.place(x=30, y=30)

lblresult = tk.Label(frame, text="", bg="ivory")
lblresult.grid(row=4, column=0, sticky = "w")

def New_Window():
  window = tk.Toplevel()
  window.geometry('150x100')
  if operator.get() == 1:
        hasil = int(nomor1.get()) + int(nomor2.get()) 
  elif operator.get() == 2:
        hasil = int(nomor1.get()) - int(nomor2.get()) 
  elif operator.get() == 3:
        hasil = int(nomor1.get()) * int(nomor2.get()) 
  elif operator.get() == 4:
        hasil = int(nomor1.get()) / int(nomor2.get()) 
  label2 = tk.Label(window, text = hasil)
  label2.grid(row=0,column=0)

# tombol = tk.Button(frame, text="+", command=plus)
# # tombol.place(x=0, y=60)
# tombol.grid(row=5, column=0)
# tombol = tk.Button(frame, text="-", command=minus)
# # tombol.place(x=50, y=60)
# tombol.grid(row=5, column=1)
# tombol = tk.Button(frame, text="*", command=multiply)
# # tombol.place(x=100, y=60)
# tombol.grid(row=5, column=2)
# tombol = tk.Button(frame, text="/", command=divide)
# # tombol.place(x=150, y=60)
# tombol.grid(row=5, column=3)

rbplus = tk.Radiobutton(frame, text="+", variable=operator, value=1)
rbplus.grid(row=6, column=0)
rbplus = tk.Radiobutton(frame, text="-", variable=operator, value=2)
rbplus.place(x=90, y=67)
rbplus = tk.Radiobutton(frame, text="*", variable=operator, value=3)
rbplus.place(x=140, y=67)
rbplus = tk.Radiobutton(frame, text="/", variable=operator, value=4)
rbplus.place(x=190, y=67)

equal = tk.Button(frame, text="=", command=New_Window)
equal.grid(row=9, column=0)



# cbplus = tk.Checkbutton(frame, text="+", variable=operator, onvalue=1, offvalue=0)
# cbplus.grid(row=8, column=0)
# cbplus = tk.Checkbutton(frame, text="-", variable=operator, onvalue=2, offvalue=0)
# cbplus.grid(row=8, column=1)
# cbplus = tk.Checkbutton(frame, text="*", variable=operator, onvalue=3, offvalue=0)
# cbplus.grid(row=8, column=2)
# cbplus = tk.Checkbutton(frame, text="/", variable=operator, onvalue=4, offvalue=0)
# cbplus.grid(row=8, column=3)

#untuk head tabel ke bawah
# for i in range(10):
#   text1 = tk.Label(text = i+1 ,fg = "red")
#   text1.grid(row = i+1, column = 0)
#   #untuk head tabel ke kanan
#   text2 = tk.Label(text = i+1 ,fg = "blue")
#   text2.grid(row = 0, column = i+1)
# #untuk isi tabel
# for i in range(10):
#   for j in range(10):
#     text3 = tk.Label(text = (i+1)*(j+1) ,fg = "purple")
#     text3.grid(row = i+1, column = j+1)

# for i in range(10):
#   text1 = tk.Label(text = i+1 ,fg = "red")
#   text1.grid(row = i+1, column = 0)
#   #untuk head tabel ke kanan
#   text2 = tk.Label(text = i+1 ,fg = "blue")
#   text2.grid(row = 0, column = i+1)
# #untuk isi tabel
# for i in range(10):
#   for j in range(10):
#     text3 = tk.Label(text = round((i+1)/(j+1),1) ,fg = "purple")
#     text3.grid(row = i+1, column = j+1)

# task pakai radio button untuk menampilkan tabel penjumlahan, pengurangan, 
# perkalian * pembagian
# tabel tampilkan dalam GUI baru

# def New_Window():
#   window = tk.Toplevel()
#   window.geometry('150x100')
  
#   label2 = tk.Label(window, text = 'this is second window')
#   label2.grid(row=0,column=0)

# button = tk.Button(root, text="Click ME", command=New_Window)
# button.grid(row=0,column=0)

# label2 = tk.Label(root, text = 'this is first window')
# label2.grid(row=1,column=0)

root.mainloop()