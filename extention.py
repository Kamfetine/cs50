def main():
    name = input("Type in the name of a file: ").lower().strip()
    if name[-4:] == ".gif" or name[-4:] == ".png":
        print("image/", name[-3:], sep="")
    elif name[-4:] == ".pdf" or name[-4:] == ".zip":
        print("application/", name[-3:], sep="")
    elif name[-5:] == ".jpeg" or name[-4:] == ".jpg":
        print("image/jpeg")
    elif name[-4:] == ".txt":
        print("text/plain")
    else:
        print("application/octet-stream")

main()