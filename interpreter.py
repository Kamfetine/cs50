def main():
    expr = input("Type in an arithmetic expression to be calculated: ").strip()
    x, y, z = expr.split(" ")
    if y == "+":
        result = add(int(x), int(z))
        print("{:.1f}".format(result))

    elif y == "/":
        result = delete(int(x), int(z))
        print("{:.1f}".format(result))

    elif y == "-":
        result = substr(int(x), int(z))
        print("{:.1f}".format(result))

    elif y == "*":
        result = mult(int(x), int(z))
        print("{:.1f}".format(result))

    else:
        print("Unknown operation")

def add(n, i):
    return float(n + i)

def substr(n, i):
    return float(n - i)

def mult(n, i):
    return float(n * i)

def delete(n, i):
    return float(n / i)

main()
