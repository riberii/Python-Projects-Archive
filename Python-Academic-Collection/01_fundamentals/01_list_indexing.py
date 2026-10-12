def main():
    items = ["satu", "dua", "tiga", "empat", "lima"]
    try:
        index = int(input("Masukkan angka (1-5): "))
        if 1 <= index <= 5:
            print(items[index - 1])
        else:
            print("Input out of range.")
    except ValueError:
        print("Error: Invalid numerical input.")

if __name__ == "__main__":
    main()
