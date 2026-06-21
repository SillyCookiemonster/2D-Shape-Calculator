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

def num_check(question, num_type="float", exit_code=None):
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
    """Gets the perimeter and area of a triangle using the given measurements,
    including which type of triangle it is (if base & height are known or the side lengths)."""

    # Get which lengths are known (Lengths of the base & height or the sides)
    known_lengths = string_check("Side lengths or the base and height lengths? ",
                                 ('sides', 'base and height'))

    # calculations if sides are known
    if known_lengths == "sides":

        # Get side lengths
        side_1 = num_check("First side: ")
        side_2 = num_check("Second side: ")
        side_3 = num_check("Third side: ")

        base_or_sides = f"{side_1}, {side_2}, {side_3}"

        # Checks if the triangle is real and returning if not
        if (side_1+side_2<side_3) or (side_2+side_3<side_1) or (side_3+side_1<side_2):
            return "not real"

        # Height is incalculable
        height = "N/A"

        # Calculate perimeter from side lengths
        perimeter = side_1+side_2+side_3

        # implement herons law to find area
        semi_perimeter = perimeter / 2
        # where s = half of the perimeter
        # sqrt(s*(s - a)*(s - b)*(s - c))   |   incl. 2 dp
        area_unrooted = (semi_perimeter * (semi_perimeter - side_1) * (semi_perimeter - side_2)
                         * (semi_perimeter - side_3))
        area = f"√{area_unrooted} / {math.sqrt(area_unrooted):.2f}"

    # calculations if base and height lengths are known
    else:

        # get length of the base and height
        base_or_sides = num_check("Base: ")
        height = num_check("Height: ")

        # calculate perimeter and area
        perimeter = "N/A"
        area = f"{(base_or_sides * height) / 2:.2f}"

    # Returns given lengths and calculated perimeter and area,
    # all for later output
    return base_or_sides, height, perimeter, area, known_lengths




# Main code
# Looping for testing purposes
while True:
    calculations = triangle_calculator()

    if calculations == "not real":
        print("This triangle is not real (side lengths can't form a triangle).")
    else:
        # output results
        print(f"{calculations[4]}: {calculations[0]} units | Height: {calculations[1]} units")
        print(f"Perimeter: {calculations[2]} units | Area: {calculations[3]} units^2\n")





