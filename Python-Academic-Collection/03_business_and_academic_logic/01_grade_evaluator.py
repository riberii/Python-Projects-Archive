def evaluate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 20:
        return "D"
    else:
        return "E"

def main():
    try:
        score = float(input("Berapa nilaimu? "))
        if 0 <= score <= 100:
            print(f"Skormu adalah {evaluate_grade(score)}")
        else:
            print("Error: Score must be between 0 and 100.")
    except ValueError:
        print("Error: Invalid numerical input.")

if __name__ == "__main__":
    main()
