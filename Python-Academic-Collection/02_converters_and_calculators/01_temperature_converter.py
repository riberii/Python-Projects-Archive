def convert_temperature(value, source_unit, target_unit):
    if source_unit == 1:
        celsius = value
    elif source_unit == 2:
        celsius = (value - 32) * 5 / 9
    elif source_unit == 3:
        celsius = value - 273.15
    else:
        raise ValueError("Invalid source unit selection.")

    if target_unit == 1:
        return celsius, "Celcius"
    elif target_unit == 2:
        return (celsius * 9 / 5) + 32, "Fahrenheit"
    elif target_unit == 3:
        return celsius + 273.15, "Kelvin"
    else:
        raise ValueError("Invalid target unit selection.")

def main():
    try:
        temp_val = float(input("Masukkan tinggi suhu: "))
        print("Pilih satuan asal:\n1. Celcius\n2. Fahrenheit\n3. Kelvin")
        source = int(input("Pilihan: "))

        print("Pilih satuan tujuan:\n1. Celcius\n2. Fahrenheit\n3. Kelvin")
        target = int(input("Pilihan: "))

        result, unit_name = convert_temperature(temp_val, source, target)
        print(f"Hasilnya adalah {int(result)} {unit_name.lower()}.")
    except ValueError as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main()
