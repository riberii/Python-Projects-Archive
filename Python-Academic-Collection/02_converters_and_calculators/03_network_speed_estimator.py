def main():
    try:
        transfer_type = int(input("1. Download\n2. Upload\nPilihan: "))
        unit = int(input("1. MB\n2. GB\nPilihan: "))
        if transfer_type not in (1, 2) or unit not in (1, 2):
            print("Error: Invalid selection.")
            return

        file_size = float(input("Size file: "))
        if unit == 2:
            file_size *= 1000

        bits = file_size * 8
        speed_mbps = 20 if transfer_type == 1 else 5
        total_seconds = int(bits / speed_mbps)

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        print(f"Estimated Time: {hours:02}:{minutes:02}:{seconds:02}")
    except ValueError:
        print("Error: Invalid numerical input.")

if __name__ == "__main__":
    main()
