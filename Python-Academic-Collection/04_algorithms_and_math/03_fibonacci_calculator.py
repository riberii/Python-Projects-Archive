def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def main():
    try:
        n = int(input("Masukkan nilai n: "))
        if n < 0:
            print("Error: Input must be a non-negative integer.")
            return

        print(f"Fibonacci ke-{n} adalah {fibonacci(n)}")
    except ValueError:
        print("Error: Invalid numerical input.")

if __name__ == "__main__":
    main()
