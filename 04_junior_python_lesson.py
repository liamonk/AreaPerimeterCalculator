valid = False
while not valid:
    response = float(input("Enter a number: "))

    if response>0:
        valid = True

    else:
        print("Please enter a number that is more than zero")
        print()


## width = int(input("What is the width of your rectangle?"))
## length = int(input("What is the length of your rectange?"))
## area = width*length