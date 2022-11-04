
def main():
    print(convert())

def convert():
   ask = input("How do you feel today? ").replace(':)', '🙂').replace(':(', '🙁')
   return  ask



main()