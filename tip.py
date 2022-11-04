def main():
    dollars = dollars_to_float(input("How much was the meal? ").lstrip('$'))
    percent = percent_to_float(input("What percentage would you like to tip? ").rstrip('%'))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(n):
    return float(n)


def percent_to_float(n):
    return float(n) / 100


main()