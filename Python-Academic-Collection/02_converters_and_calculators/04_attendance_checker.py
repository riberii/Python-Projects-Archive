def main():
    try:
        attended = int(input("Total kehadiran siswa: "))
        absent = int(input("Total ketidakhadiran siswa: "))
        total_classes = attended + absent

        if total_classes == 0:
            print("Error: Total class sessions cannot be zero.")
            return

        percentage = (attended / total_classes) * 100
        print(f"Persentase kehadiran siswa: {int(percentage)}%")
        if percentage >= 75:
            print("Siswa boleh mengikuti ujian")
        else:
            print("Siswa tidak boleh mengikuti ujian")
    except ValueError:
        print("Error: Invalid numerical input.")

if __name__ == "__main__":
    main()
