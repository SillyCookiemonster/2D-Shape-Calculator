import math
import pandas
from tabulate2 import tabulate

# Functions go here
def string_check(question, valid_ans_list=('yes', 'no'), exit_code=None, check_first=True):
    """Checks that the users enter the full word
    or the first letter of a word from a list of valid responses"""

    # sets error message
    if valid_ans_list == ('yes', 'no'):
        error = f"Please enter yes / no (y / n)"
    else:
        # Set error message from the list of valid responses
        error = f"Please choose a valid answer from these options: "

        # adding each available option to the string in a presentable way
        # by making it a list that is easier to read not python's variable list
        for item in valid_ans_list:
            error += f"{item}, "

        # remove last 2 characters (", ") from the error string
        error = error.removesuffix(", ")

    # Loop until valid answer
    while True:

        # gets users answer to the question (and making it lowercase to check if its valid easier)
        response = input(question).lower()

        # Exit when user requests to
        if response == exit_code:
            return response

        for item in valid_ans_list:

            # check the response is the entire word
            if response == item:
                return item

            # check the response is the first letter
            if check_first and response == item[0]:
                return item

        # If it wasn't an option in the list, print error and restart loop
        print(error)


def make_statement(statement, decoration, amount=3):
    """Emphasises headings by adding decoration
    at the start and end a custom amount of times"""

    print(f"{decoration*amount} {statement} {decoration*amount}")


def instructions():
    """prints instructions for how to use the calculator"""

    print()
    make_statement("Instructions", "ℹ️")

    print('''
This program will..

- Ask for a basic 2D shape you want to calculate 
    the perimeter and area for. The valid shapes are: 
    square, rectangle, circle, and triangle
    (Tip! You only need to enter the first letter
    of a shape to enter it).
    
- Ask to clarify if base and height or sides are known 
    if triangle was preciously selected.
    
- Ask for the measurements of the selected shape.

- Output the area and perimeter of the shapes 
    along with the given information in a table.
    
Once you have finished using the calculator, 
  enter "xxx" during shape selection.

    ''')


def num_check(question, num_type="float", exit_code=None):
    """Checks the user enters a number above 0"""

    # sets error message for what requirements the user is required to meet (integer or float)
    if num_type == "int":
        error = "Error. Please enter an integer above 0."
        change_to = int
    else:
        error = "Error. Please enter a number above 0."
        change_to = float

    # Loops to make sure a number is indeed entered
    while True:
        # Ask user for number using the question
        response = input(question)

        # Check if user requests exit and exit if so
        if response == exit_code:
            return response

        try:
            # Check if the response can be changed into the expected answer format
            response = change_to(response)

            # Check if the user enters a valid length
            # Lengths must always be larger than zero
            if response > 0:
                # Return when given answer passed all checks and is valid
                return response

            # Answer isn't a valid length even if in correct format (is not larger than zero)
            else:
                print(error)

        # If converting answer format fails, print error and loop again
        except ValueError:
            print(error)


def rectangle_calculator(square_or_rectangle):
    """Gets the perimeter and area of a rectangle using given measurements."""

    # Ask for length
    length = num_check("Length: ")

    # get height of non-square rectangle
    if square_or_rectangle == "rectangle":
        height = num_check("Height: ")

    # set height to length when shape is square
    else:
        height = length

    # calculate perimeter and area
    perimeter = 2*length + 2*height
    area = length*height

    # Returns given lengths and calculated perimeter and area,
    # all for later output
    return length, height, perimeter, area


def circle_calculator():
    """Gets the perimeter and area of a circle using given measurements."""

    radius = num_check("Radius: ")

    # calculate diameter, perimeter and area  incl. 2 dp
    diameter = 2*radius
    perimeter = f"{diameter}π / {(math.pi * diameter):.2f}"
    area = f"{radius**2}π / {(math.pi * radius**2):.2f}"

    # Returns given radius and calculated diameter, perimeter and area,
    # all for later output
    return radius, diameter, perimeter, area


def triangle_calculator():
    """Gets the perimeter and area of a triangle using the given measurements,
    including which type of triangle it is (if base & height are known or the side lengths)."""

    # Get which lengths are known (Lengths of the base & height or the sides)
    known_lengths = string_check("Do you have the side lengths or the base and height lengths? ",
                                 ('sides', 'base and height'))

    # calculations if sides are known
    if known_lengths == "sides":

        # Get side lengths
        side_1 = num_check("First side: ")
        side_2 = num_check("Second side: ")
        side_3 = num_check("Third side: ")

        base_or_sides = f"{side_1}, {side_2}, {side_3}"

        # Checks if the triangle is real and returning if not
        if (side_1+side_2<=side_3) or (side_2+side_3<=side_1) or (side_3+side_1<=side_2):
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
        area = f"√{area_unrooted:.2f} / {math.sqrt(area_unrooted):.2f}"

    # calculations if base and height lengths are known
    else:

        # get length of the base and height
        base_or_sides = num_check("Base length: ")
        height = num_check("Height: ")

        # calculate perimeter and area
        perimeter = "N/A"
        area = f"{(base_or_sides * height) / 2:.2f}"

    # Returns given lengths and calculated perimeter and area,
    # all for later output
    return base_or_sides, height, perimeter, area, known_lengths


# Main routine goes here

# Title and instructions

make_statement("Ezra's 2D Shape Calculator", "🔷🔶🔷", 1)

print()
want_instructions = string_check("Do you want to see the instructions? ")

# Ask if users want to know how to use the calculator
if want_instructions == "yes":
    instructions()

# Setup lists to be used for data storage to be put into Pandas
all_shapes = []
all_base = []
all_height = []
all_perimeter = []
all_area = []

# Dictionary for Pandas
shape_dict = {
    "Shape" : all_shapes,
    "Side Length(s) /\nRadius" : all_base,
    "Height /\nDiameter" : all_height,
    "Perimeter" : all_perimeter,
    "Area" : all_area
}

# Loop until users request exit
while True:
    print()

    # Get the shape the user wants to calculate for
    shape = string_check("What shape do you want to calculate? ",
                         ('square', 'rectangle', 'circle', 'triangle'), "xxx")

    # run shape calculations per each shape
    if shape == "square":
        data = rectangle_calculator(shape)
    elif shape == "rectangle":
        data = rectangle_calculator(shape)
    elif shape == "circle":
        data = circle_calculator()
    elif shape == "triangle":
        data = triangle_calculator()
        if data == "not real":
            print("This triangle is not real (side lengths can't form a triangle).")
            continue
        # Change shape title depending on which type of triangle
        if data[4] == "sides":
            shape += " (sides)"
        else:
            shape += " (base & height)"

    # exit when requested
    else:
        break

    units = string_check("What unit of measurement are you using for this shape? ", ("mm", "cm", "m", "km"), None, False)

    # storing shape in list for data to be output in Pandas
    all_shapes.append(shape.title())
    all_base.append(f"{data[0]:.2f} {units}")
    all_height.append(f"{data[1]:.2f} {units}")
    all_perimeter.append(f"{data[2]:.2f} {units}")
    all_area.append(f"{data[3]:.2f} {units}²")

# If the user didn't enter any shapes there is no need to print a table
if len(all_shapes)  == 0:
    print()
    print("You didn't enter any shapes to calculate")

else:
    # Form Pandas with the data
    shape_frame = pandas.DataFrame(shape_dict)

    # Representing the Pandas as a table with customised layout to make it look tidy
    table_string = tabulate(shape_frame, headers='keys', tablefmt='rounded_grid', showindex=False,
                             colalign=("l", "r", "r", "r", "r"), headersglobalalign="right")

    print()
    make_statement("Calculations (With Units to 2 Decimal Places)", "=", 5)
    print(table_string)

print()
make_statement("Thank you for using Ezra's 2D Shape Calculator!", "🔶🔷🔶", 1)
