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


def triangle_calculator():

    known_lengths = string_check("Side lengths or the base and height lengths? ", ('sides', 'base and height'))

    # calculations if sides are known
    if known_lengths == "sides":
        triangle_type = "Sides"

        side_1 = num_check("First side: ", "float")
        side_2 = num_check("Second side: ", "float")
        side_3 = num_check("Third side: ", "float")

        base_or_sides = f"{side_1}, {side_2}, {side_3}"
        height = "N/A"
        perimeter = side_1+side_2+side_3

        # implement herons law
        semi_perimeter = perimeter/2
        # sqrt(s*(s - a)*(s - b)*(s - c))
        area_unrooted = semi_perimeter*(semi_perimeter-side_1)*(semi_perimeter-side_2)*(semi_perimeter-side_3)
        area = f"√{area_unrooted} OR {math.sqrt(area_unrooted)}"

    # calculations if base and height lengths are known
    else:
        triangle_type = "Base"

        base_or_sides = num_check("Base: ", "float")
        height = num_check("Height: ", "float")

        # calculate perimeter and area
        perimeter = "N/A"
        area = (1/2)*base_or_sides*height

    return triangle_type, base_or_sides, height, perimeter, area




# Main code
# Looping for testing purposes
while True:
    calculations = triangle_calculator()

    # output results
    print(f"{calculations[0]}: {calculations[1]} units | Height: {calculations[2]} units")
    print(f"Perimeter: {calculations[3]} units | Area: {calculations[4]} units^2\n")





