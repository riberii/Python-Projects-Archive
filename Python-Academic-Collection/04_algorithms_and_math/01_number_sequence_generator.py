import time

def main():
    try:
        choice = int(input("Pilih Algoritma:\n1. -1 & +3\n2. +2 & +4\n3. *2 & *3\nPilihan: "))
        if choice not in (1, 2, 3):
            print("Error: Invalid selection.")
            return

        starting = int(input("Masukkan angka awal: "))
        sequence = []

        for _ in range(5):
            sequence.append(starting)
            print(sequence)
            time.sleep(0.2)

            if choice == 1:
                starting -= 1
            elif choice == 2:
                starting += 2
            elif choice == 3:
                starting *= 2

    except ValueError:
        print("Error: Invalid numerical input.")

if __name__ == "__main__":
    main()
