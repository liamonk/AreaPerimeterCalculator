
## function that asks for a number, checks it is more than zero, and returns the number
from tkinter.messagebox import YES


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


print()
print("***** Area and Perimeter Calculator *****")
print()
keep_going = ""
while keep_going =="":

        print()
        width = num_check("Width?")
        height = num_check("Height?")

        area = width*height
        print("The area is {:.4f} square units" .format(area))
        perimeter = 2*width+2*height
        print("The perimeter is {:.4f} units" .format(perimeter))
        print()

        keep_going = input("Press <enter> to keep going or press any key to quit")
        

print("Thanks for using the calculator!")



