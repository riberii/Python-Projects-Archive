def main():
    try:
        number = int(input("Masukkan angka: "))
        if number % 2 == 0:
            print("Angka genap")
        else:
            print("Angka ganjil")
    except ValueError:
        print("Error: Invalid numerical input.")

if __name__ == "__main__":
    main()
