def main():
    try:
        total_seconds = int(input("Masukkan sekon: "))
        if total_seconds < 0:
            print("Error: Time cannot be negative.")
            return

        hours = total_seconds // 3600
        remaining_seconds = total_seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60

        print(f"{hours:02}:{minutes:02}:{seconds:02}")
    except ValueError:
        print("Error: Invalid numerical input.")

if __name__ == "__main__":
    main()
