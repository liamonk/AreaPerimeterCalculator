
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
height = num_check("Height?")

area = width*height
print("The area is {} square units" .format(area))
perimeter = 2*width+2*height
print("The perimeter is {} units" .format(perimeter))