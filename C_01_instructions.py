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

# Main routine goes here

make_statement("2D Shape Calculator", "🔷🔶🔷", 1)

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()
print("program continues...")
