
## function that asks for a number, checks it is more than zero, and returns the number
def num_check(question):

    valid = False
    while not valid:
        
        error = "Please enter a number that is more than zero"

        try:
            response = float(input(question))


            if response>0:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)

width = num_check("Width?")
print(width)
height = num_check("Height?")
print(height)