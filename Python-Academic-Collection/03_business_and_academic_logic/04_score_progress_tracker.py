def main():
    try:
        s1 = int(input("Masukkan nilai semester 1: "))
        s2 = int(input("Masukkan nilai semester 2: "))
        if not (0 <= s1 <= 100 and 0 <= s2 <= 100):
            print("Error: Scores must be between 0 and 100.")
            return

        if s2 >= 90:
            print("Excellent Score")
        elif s2 >= 70:
            print("Good Score")
        elif s2 >= 50:
            print("Adequate Score")
        elif s2 >= 30:
            print("Poor Score")
        else:
            print("Fail")

        diff = s2 - s1
        if diff >= 10:
            print("Major Improvement")
        elif diff >= 1:
            print("Good Improvement")
        elif diff == 0:
            print("Consistent & Great effort")
        elif diff >= -9:
            print("Need More Effort")
        else:
            print("Declining Progress, Need Improvement")
    except ValueError:
        print("Error: Invalid numerical input.")

if __name__ == "__main__":
    main()
