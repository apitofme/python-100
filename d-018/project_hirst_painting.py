"""
-=< 100 Days of Python >=-
-=[ Day 018 ]=-

Project - The Hirst Painting
"""
import random
import json
from turtle import Turtle, Screen
import colorgram
"""
L.136 - Part 1: How to extract RGB values from Images

For this part of the project you will need to install a package from PyPI
called "colorgram" which "is a Python library that lets you extract colors
from images" -- https://pypi.org/project/colorgram.py/

We will use this library to extract a selection of colours (from an image you
choose) to use as the colour palette in our Hirst style painting. So, once you
have installed colorgram in to your project, you will need to source an image.
You could search online for examples of Hirst dot paintings, or just find any
other image you like the colours of, then download/copy it in to your project
folder and rename it to "image.jpg". With this done you are ready to go ahead
and use the documentation and code examples on the colorgram project page to
see if you can work out how to extract 6 colours from your chosen image.
"""


def too_light(colour, limit=200):
    """Test each channel in an RGB colour Tuple against the limit value.
    Returns Boolean"""
    if not isinstance(colour, tuple):
        colour = tuple(colour)
    red, green, blue = colour
    if red > limit and green > limit and blue > limit:
        print(f"[NOTICE]: Too LIGHT! - Discarding colour '{colour}'")
        return True
    return False


def too_dark(colour, limit=25):
    """Test each channel in an RGB colour Tuple against the limit value.
    Returns Boolean"""
    if not isinstance(colour, tuple):
        colour = tuple(colour)
    red, green, blue = colour
    if red < limit and green < limit and blue < limit:
        print(f"[NOTICE]: Too DARK! - Discarding colour '{colour}'")
        return True
    return False


def extract_palette(image_file, number_of_colours):
    """Uses colorgram to extract a number of colours from an image file
    Returns a List of Tuples containing RGB values - i.e. (r,g,b)"""
    print(f"Extracting {number_of_colours} colours from source image:")
    if isinstance(image_file, str):
        print(f' - File: "{image_file}"')
    source = colorgram.extract(image_file, number_of_colours)
    palette = []
    for colour in source:
        if too_light(colour.rgb) or too_dark(colour.rgb):
            continue
        palette.append(colour.rgb)
        # NOTE: RGB is a named tuple, so values can be accessed as properties.
        # Ref: https://pypi.org/project/colorgram.py/

    print(f"...{len(palette)} colours successfully extracted.")
    # print(palette)
    return palette


def save_palette(palette, json_file):
    """Save a colour palette (a List of RGB Tuples) to a JSON file."""
    print(f"Saving colour palette to JSON file: {json_file}")
    with open(json_file, "w", encoding="utf-8") as jf:
        # NOTE: "indent=2" is not needed, but makes the file human-readable
        # if the data is nested
        json.dump(palette, jf, indent=2)
    print("...success!")


def update_palette(img_file, number_of_colours, json_file, save=True):
    """Uses colorgram to extract a number of colours from an image file,
    and serializes the resulting List of RGB Tuples to a JSON file."""
    print("Updating colour palette...")
    palette = extract_palette(img_file, number_of_colours)
    if save:
        save_palette(palette, json_file)
    return palette


def get_palette(
    json_file="palette.json",
    img_file="image.jpg",
    number_of_colours=10,
    save=True,
):
    """Retrieve a list of RGB Tuples (r,g,b) to use as colour palette.
    Either from a JSON file (if available), or from a source image file.

    - json_file [str]
        The filename of the local JSON file retrieve a palette from.

    When JSON file does NOT exist:
    - img_file [str]
        The filename of a local image to extract colours from.
    - number_of_colours [int]
        The number of colours to attempt to extract from the given image file.
    - save [bool]
        (Flag) Whether to save the retrieved palette back to the JSON file.
    """
    # palette = None
    print("Obtaining colour palette...")
    try:
        with open(json_file, "r", encoding="utf-8") as jf:
            print(f"Loading palette from JSON file: {json_file}")
            source = json.load(jf)
            # NOTE: JSON does not distinguish between Tuples and Lists, they
            # are all just 'Arrays', so the data returned is a list of Lists!
            # Refs:
            # - https://docs.python.org/3.12/library/json.html#json.load
            # - https://docs.python.org/3.12/library/json.html#json-to-py-table
            palette = [tuple(lst) for lst in source]
            print("...success!")
    except FileNotFoundError:
        palette = extract_palette(img_file, number_of_colours)
        if save:
            save_palette(palette, json_file)
    return palette


colour_palette = get_palette(number_of_colours=30)
# print(colour_palette)

"""
L.137 - Part 2: Drawing the Dots

Now we have generated a colour palette it's time to work out how to create
our 'Hirstian' artwork...

The dot pattern should be created as a grid consisting of 10 x 10 dots, where
each dot has a size of 20, and they are all spaced 50 units apart.

-- IMPORTANT! --

NOTE: I have implemented functionality for the colour palette such that the
RGB values extracted from the image are cached to a static JSON file.
-- Please read the docstrings and study the functions to understand their use!

Summary of Functionality:

    get_palette()
        - Will attempt to retrieve the colour palette data from a JSON file
        [Default: 'palette.json']
        - If the JSON file does not exist, falls back to attempting to extract
        colours [Default: 10] from an image file [Default: 'image.jpg'].
        - If the colour palette is obtained from the image file, by default
        it will attempt to save colour palette to the JSON file. This can be
        overridden by adding the argument "save=False".

To update the colour palette either:
    - Call the `update_palette` function, passing the necessary arguments
    -- or --
    - Simply delete the JSON file and pass the desired image file as a
    parameter to `get_palette` (above).
"""
GRID_COLUMNS = 8
GRID_ROWS = 6
COLUMN_SPACE = 50
ROW_SPACE = 50
DOT_SIZE = 25
BORDER_RATIO = 0.25
# NOTE: Values for BORDER_RATIO can be between 0.1 and 1.0, however values
# between 0.1 and 0.5 generally work best!
# -- Larger borders for smaller grids, OR smaller borders for larger grids!

print("\nStarting draw operation...")
# Screen Configuration:
window = Screen()
window.colormode(255)
window.title("Hirstian Art for the Masses Baby!")
# - Calculate grid size:
grid_width = GRID_COLUMNS * COLUMN_SPACE
grid_height = GRID_ROWS * ROW_SPACE
# - Calculate window size
border_x = grid_width * BORDER_RATIO
border_y = grid_height * BORDER_RATIO
print(f"Border: {border_x} x {border_y}")
screen_width = grid_width + (2 * border_x)
screen_height = grid_height + (2 * border_y)
# print(f"Screen: {screen_width} x {screen_height}")
window.setup(
    width=screen_width,
    height=screen_height,
    startx=0,
    starty=0,
)

# canvas_x, canvas_y = window.screensize()
# print(f"Canvas size: {canvas_x} x {canvas_y}")
# NOTE: `window.screensize()` does not seem to return the actual canvas size,
# at least not at this point, so it is useless to calculate borders
# ... weird!

# - Calculate screen scale coordinates
lower_left_x = -border_x
lower_left_y = -(border_y / 2)
# NOTE: After some testing it seems halving the 'lower-y' coord works best?!
upper_right_x = grid_width + border_x
upper_right_y = grid_height + border_y
print(f"Coords:\n- Lower: {lower_left_x} x {lower_left_y}")
print(f"- Upper: {upper_right_x} x {upper_right_y}")
window.setworldcoordinates(
    lower_left_x,
    lower_left_y,
    upper_right_x,
    upper_right_y,
)
# Turtle configuration:
pen = Turtle()
pen.speed("fastest")
pen.up()  # <- Do NOT draw a line!
pen.hideturtle()

# Create a grid of coloured dots
for y in range(GRID_ROWS):
    y_position = (y+1) * ROW_SPACE
    # print(f"Line: {y + 1}")
    for x in range(GRID_COLUMNS):
        dot_colour = random.choice(colour_palette)
        if x % GRID_COLUMNS == 0:
            pen.goto(0, y_position)
        # print(f"[DOT {(y * 10) + x + 1}] Colour: {dot_colour}")
        pen.dot(DOT_SIZE, dot_colour)
        pen.forward(COLUMN_SPACE)

"""
>> Previous implementation: one loop for the total number of dots...

for n in range(100):
    dot = n+1
    dot_colour = random.choice(colour_palette)

    if n % 10 == 0:
        # print(f"Line: {(dot // 10)+1}")
        y_coord = DOT_SPACING * (dot // 10)
        pen.goto(0, y_coord)

    # print(f"[DOT {dot}] Colour: {dot_colour}")
    pen.dot(DOT_SIZE, dot_colour)
    pen.forward(DOT_SPACING)

"""
print("...done!")
# Keep the display window open until we click on it
window.exitonclick()
