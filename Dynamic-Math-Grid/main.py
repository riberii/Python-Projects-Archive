import tkinter as tk
from tkinter import messagebox

def show_table_window():
    op = operator.get()
    if op == 0:
        messagebox.showwarning("Peringatan", "Silakan pilih operasi matematika terlebih dahulu!")
        return
    window = tk.Toplevel(root)
    window.title("Tabel Matematika")
    window.configure(bg="ivory")
    window.geometry("450x350")
    if op == 1: symbol = "+"
    elif op == 2: symbol = "-"
    elif op == 3: symbol = "x"
    elif op == 4: symbol = "/"
    tk.Label(window, text=f"Tabel {symbol}", bg="ivory", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5)
    for i in range(1, 11):
        tk.Label(window, text=i, fg="red", bg="ivory", font=("Arial", 10, "bold")).grid(row=i, column=0, padx=5, pady=5)
        tk.Label(window, text=i, fg="blue", bg="ivory", font=("Arial", 10, "bold")).grid(row=0, column=i, padx=5, pady=5)
    for i in range(1, 11):
        for j in range(1, 11):
            if op == 1:
                hasil = i + j
            elif op == 2:
                hasil = i - j
            elif op == 3:
                hasil = i * j
            elif op == 4:
                hasil = round(i / j, 1) 
            tk.Label(window, text=hasil, fg="purple", bg="ivory").grid(row=i, column=j, padx=5, pady=5)
root = tk.Tk()
root.title("Aplikasi Tabel Matematika")
root.geometry('300x250')
root.configure(bg="white")
operator = tk.IntVar()
tk.Label(root, text="Pilih Operasi Matematika:", bg="white", font=("Arial", 12, "bold")).pack(pady=15)
frame_radio = tk.Frame(root, bg="white")
frame_radio.pack()
tk.Radiobutton(frame_radio, text="Penjumlahan (+)", variable=operator, value=1, bg="white").grid(row=0, column=0, sticky="w")
tk.Radiobutton(frame_radio, text="Pengurangan (-)", variable=operator, value=2, bg="white").grid(row=1, column=0, sticky="w")
tk.Radiobutton(frame_radio, text="Perkalian (*)", variable=operator, value=3, bg="white").grid(row=2, column=0, sticky="w")
tk.Radiobutton(frame_radio, text="Pembagian (/)", variable=operator, value=4, bg="white").grid(row=3, column=0, sticky="w")
btn_generate = tk.Button(root, text="Tampilkan Tabel", command=show_table_window, bg="lightblue", font=("Arial", 10, "bold"))
btn_generate.pack(pady=20)

root.mainloop()