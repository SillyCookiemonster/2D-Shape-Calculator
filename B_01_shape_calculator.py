import math
import pandas
from tabulate import tabulate

# Functions go here
def string_check(question, valid_ans_list=('yes', 'no')):
    """Checks that the users enter the full word
    or the first letter of a word from a list of valid responses"""

    if valid_ans_list == ('yes', 'no'):
        err = f"Please enter yes / no (y / n)"
    else:
        err = f"Please choose a valid answer from {valid_ans_list}"

    while True:

        response = input(question).lower()

        if response == "xxx":
            return "end"

        for item in valid_ans_list:

            # check the response is the entire word
            if response == item:
                return item

            # check the response is the first letter
            if response == item[0]:
                return item

        print(err)


def make_statement(statement, decoration, amount=3):
    """Emphasises headings by adding decoration
    at the start and end a custom amount of times"""

    print(f"{decoration*amount} {statement} {decoration*amount}")


def instructions():
    print()
    make_statement("Instructions", "ℹ️")

    print('''
This program will..

- Ask for he basic 2D shape you want to calculate 
    the perimeter and area for. The valid shapes are 
    square, rectangle, circle, and triangle
    (Tip! You only need to enter the first letter
    of a shape to enter it).
    
- Ask to clarify if base and height or sides are known 
    if triangle was preciously selected.
    
- Ask for the measurements of the selected shape.

- Output the area and perimeter of the shapes 
    along with the given information in a table.

    ''')


def num_check(question, num_type, exit_code=None):
    """Checks the user enters a number above 0"""

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


def rectangle_calculator(square_or_rectangle):
    """Gets the perimeter and area of a rectangle"""

    # Ask for length
    length = num_check("Length: ", "float")

    # get height of non-square rectangle
    if square_or_rectangle == "rectangle":
        height = num_check("Height: ", "float")

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
    """Gets the perimeter and area of a circle"""

    radius = num_check("Radius: ", "float")

    # calculate diameter, perimeter and area  incl. 2 dp
    diameter = 2*radius
    perimeter = f"{diameter}π / {(math.pi * diameter):.2f}"
    area = f"{radius**2}π / {(math.pi * radius**2):.2f}"

    # Returns given radius and calculated diameter, perimeter and area,
    # all for later output
    return radius, diameter, perimeter, area


def triangle_calculator():
    """Gets the perimeter and area of a triangle,
    reliant on which type of triangle is chosen"""

    # Get which lengths are known (Lengths of the base & height or the sides)
    known_lengths = string_check("Side lengths or the base and height lengths? ",
                                 ('sides', 'base and height'))

    # calculations if sides are known
    if known_lengths == "sides":

        # Get side lengths
        side_1 = num_check("First side: ", "float")
        side_2 = num_check("Second side: ", "float")
        side_3 = num_check("Third side: ", "float")

        base_or_sides = f"{side_1}, {side_2}, {side_3}"
        height = "N/A"
        perimeter = side_1+side_2+side_3

        # implement herons law
        semi_perimeter = perimeter / 2
        # sqrt(s*(s - a)*(s - b)*(s - c)) inc. 2 dp
        area_unrooted = (semi_perimeter * (semi_perimeter - side_1) * (semi_perimeter - side_2)
                         * (semi_perimeter - side_3))
        area = f"√{area_unrooted} / {math.sqrt(area_unrooted):.2f}"

    # calculations if base and height lengths are known
    else:

        # get length of the base and height
        base_or_sides = num_check("Base: ", "float")
        height = num_check("Height: ", "float")

        # calculate perimeter and area
        perimeter = "N/A"
        area = f"{(base_or_sides * height) / 2:.2f}"

    # Returns given lengths and calculated perimeter and area,
    # all for later output
    return base_or_sides, height, perimeter, area, known_lengths


# Main routine goes here

# Title and instructions

make_statement("2D Shape Calculator", "🔷🔶🔷", 1)

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

# lists for panda
all_shapes = []
all_base = []
all_height = []
all_perimeter = []
all_area = []

# Panda dictionary
shape_dict = {
    "Shape" : all_shapes,
    "Side Length(s) /\nDiameter" : all_base,
    "Height /\nRadius" : all_height,
    "Perimeter" : all_perimeter,
    "Area" : all_area
}

# Loop until exit
while True:
    print()

    # Get shapes
    shape = string_check("What shape do you want to calculate? ",
                         ('square', 'rectangle', 'circle', 'triangle'))

    # run shape calculations per each shape
    if shape == "square":
        data = rectangle_calculator(shape)
    elif shape == "rectangle":
        data = rectangle_calculator(shape)
    elif shape == "circle":
        data = circle_calculator()
    elif shape == "triangle":
        data = triangle_calculator()
        # Change shape title depending on which type of triangle
        if data[4] == "sides":
            shape += " (sides)"
        else:
            shape += " (base & height)"

    # exit when requested
    else:
        break

    # storing shape in list
    all_shapes.append(shape.title())
    all_base.append(data[0])
    all_height.append(data[1])
    all_perimeter.append(data[2])
    all_area.append(data[3])

# Make pandas
shape_frame = pandas.DataFrame(shape_dict)

table_string = tabulate(shape_frame, headers='keys', tablefmt='psql', showindex=False,
                         colalign=("left", "right", "right", "right", "right"), headersglobalalign= 'left')

print(table_string)
