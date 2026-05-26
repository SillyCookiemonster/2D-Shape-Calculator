import math

# Functions
def string_check(question, valid_ans_list=('yes', 'no')):
    """Checks that the users enter the full word
    or the first letter of a word from a list of valid responses"""

    if valid_ans_list == ('yes', 'no'):
        err = f"Please enter yes / no (y / n)"
    else:
        err = f"Please choose a valid answer from {valid_ans_list}"

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check the response is the entire word
            if response == item:
                return item

            # check the response is the first letter
            if response == item[0]:
                return item

        print(err)

def num_check(question, num_type, exit_code=None):
    """Checks the user enters an integer above 0"""

    if num_type == "int":
        error = "Error. Please enter an integer above 0."
        change_to = int
    else:
        error = "Error. Please enter a number above 0."
        change_to = float

    while True:
        response = input(question)

        if response == exit_code:
            return response

        try:
            response = change_to(response)
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def circle_calculator():

    radius = num_check("Radius: ", "float")

    # calculate diameter, perimeter and area
    diameter = 2*radius
    perimeter = f"{diameter}π OR {math.pi*diameter}"
    area = f"{radius**2}π OR {math.pi*radius**2}"

    return radius, diameter, perimeter, area




# Main code
# Looping for testing purposes
while True:
    calculations = circle_calculator()

    # output results
    print(f"Radius: {calculations[0]} units | Diameter: {calculations[1]} units")
    print(f"Perimeter: {calculations[2]} units | Area: {calculations[3]} units^2\n")





