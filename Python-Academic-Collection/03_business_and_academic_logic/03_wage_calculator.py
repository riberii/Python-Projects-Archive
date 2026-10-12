def main():
    try:
        gender = input("Jenis kelamin (M/F): ").strip().upper()
        if gender not in ("M", "F"):
            print("Error: Gender must be M or F.")
            return

        age = int(input("Umur: "))
        if not (18 <= age <= 40):
            print("Error: Age must be between 18 and 40.")
            return

        days = int(input("Jumlah hari bekerja: "))
        if days < 0:
            print("Error: Working days cannot be negative.")
            return

        rates = {
            "M": 700 if age < 30 else 750,
            "F": 800 if age < 30 else 850
        }

        pay = rates[gender] * days
        print(f"Upah yang harus dibayar: Rp.{pay}")
    except ValueError:
        print("Error: Invalid numerical input.")

if __name__ == "__main__":
    main()
