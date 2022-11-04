def main():
    print("E =", einstein())

def einstein():
    m = int(input("Type mass in kg: "))
    c = int(pow(300000000,2))

    return m * c

main()