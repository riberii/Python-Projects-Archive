def main():
    try:
        number = int(input("Masukkan nomor loker: "))
        if number < 1:
            print("Error: Locker number must be greater than 0.")
            return

        color_map = {
            0: "biru",
            1: "merah",
            2: "putih",
            3: "kuning"
        }
        print(f"Loker anda berwarna {color_map[number % 4]}.")
    except ValueError:
        print("Error: Invalid numerical input.")

if __name__ == "__main__":
    main()
