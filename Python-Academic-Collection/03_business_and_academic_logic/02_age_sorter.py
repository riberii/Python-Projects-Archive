def main():
    ages = []
    try:
        for i in range(4):
            age = int(input(f"Masukkan umur ke-{i+1}: "))
            ages.append(age)

        ages.sort()
        print("Sorted Ages:", ages)
        print("Umur termuda:", ages[0])
    except ValueError:
        print("Error: Invalid numerical input.")

if __name__ == "__main__":
    main()
