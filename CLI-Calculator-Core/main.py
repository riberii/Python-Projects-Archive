# print("Hello CodeSandbox!")
# Function
# 1. without parameter & return (void)
# 2. with parameter & without return
# 3. Function with parameter & with return
# 4. Function without parameter & with return

# var2 = "Marquis"
# var1 = 446

# def sapa():
#     global var2
#     var1 = 3456
#     print("Hallo")

# def siapa():
#     global var2, var1
#     print(var1)

# sapa()
# siapa()

# def Hitung(a, b, c):
#     print( a )
#     return False

# def Benar():
#     return True

# var = Benar()

# if var:
#     print("Benar")
# else:
#     print("Salah")



# adv Calculator
def start():
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. :")
    var = input("Pilih......")
    # return(input("Masukan operator: ")) # FIXED: Commented this out so it doesn't ask twice and ignore your 'var'
    return var

op = start()

def insert_num():
    num_1 = (input("Masukan angka pertama: "))
    num_2 = (input("Masukan angka kedua: "))
    return(int(num_1), int(num_2))

test = insert_num()
daftar = [1,2]
print(test, daftar)
print(test[0] + test[1])

def calculate(a, b, x):
    if x == "+" or x == "1":
        return(a + b)
    elif x == "-" or x == "2":
        return(a - b)
    elif x == "*" or x == "3":
        return(a * b)
    elif x == ":" or x == "4":
        return(a / b)
    else:
        print("Error")
        exit()

# FIXED: You built the calculate function but never called it! Added the execution here:
hasil = calculate(test[0], test[1], op)
print(f"\nHasil perhitungan: {hasil}")