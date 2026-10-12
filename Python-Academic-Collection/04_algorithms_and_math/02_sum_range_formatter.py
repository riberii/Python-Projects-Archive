def main():
    try:
        n = int(input("Masukkan angka: "))
        if n < 1:
            print("Error: Number must be at least 1.")
            return

        numbers = list(range(1, n + 1))
        total = sum(numbers)
        expression = " + ".join(map(str, numbers))

        print(f"Jumlah dari {expression} adalah {total}")
    except ValueError:
        print("Error: Invalid numerical input.")

if __name__ == "__main__":
    main()
