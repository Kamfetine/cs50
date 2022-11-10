def main():
    ask = input("What's the answer to the Great Question? ").strip().lower()

    match ask:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

main()