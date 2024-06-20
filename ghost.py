#!/usr/bin/env python3

"""
Stanford CS106A Ghost Project
"""
import math
import os
import sys

# This line imports SimpleImage for use here
# This depends on the Pillow package
from simpleimage import SimpleImage

#Calculate
def color_dist2(color1, color2):
    """
    Returns the square of the color distance between two color tuples.
    >>> color_dist2((255, 255, 255) , (0, 0, 0))
    441.6729559300637
    >>> color_dist2((100, 100, 100) , (10, 10, 10))
    155.88457268119896
    >>> color_dist2((10, 10, 10) , (10, 10, 10))
    0.0
    """

    x_difference = color1[0] - color2[0]
    y_difference = color1[1] - color2[1]
    z_difference = color1[2] - color2[2]
    return math.sqrt(abs(x_difference ** 2) + abs(y_difference ** 2) + abs(z_difference ** 2)) #abs on everyone for math assurment


#Average from list of tuples
def average_color(colors):
    """
    >>> average_color([(1, 1, 1), (2, 2, 2), (3, 3, 3), (0, 4, 2)])
    (1.5, 2.5, 2.0)
    >>> average_color([(1, 1, 1), (1, 1, 1), (28, 28, 28)])
    (10.0, 10.0, 10.0)

    """


    #Associate it with a value
    Sum_red=0
    Sum_green=0
    Sum_blue=0
    for color in colors:
        Sum_red += color[0]
        Sum_green += color[1]
        Sum_blue += color[2]
    #Averages
    avg_red = Sum_red/len(colors)
    avg_green = Sum_green/len(colors)
    avg_blue = Sum_blue/len(colors)
    return avg_red, avg_green, avg_blue


def best_color(colors):
    """
    Given a list of 1 or more color tuples, return the best color.
    >>> best_color([(1, 1, 1), (1, 1, 1), (28, 28, 28)])
    (1, 1, 1)
    >>> best_color([(1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1)])
    (1, 1, 1)
    >>> best_color([(1, 5, 2), (1, 5, 2), (28, 28, 28)])
    (1, 5, 2)
    """
    average = average_color(colors)
    return min(colors, key=lambda color: color_dist2(color, average))


#Best on good-apple
def good_apple_color(colors):
    """
    Given a list of 2 or more color tuples, return the best color
    according to the good-apple strategy.
    >>> good_apple_color([(18, 18, 18), (0, 2, 0), (19, 23, 18), (19, 22, 18), (19, 22, 18), (1, 0, 1)])
    (19, 23, 18)
    """
  #average color once before sorting.
    sorted_apples = sorted(colors, key=lambda color: color_dist2(color, average_color(colors)))
    pos_half = len(sorted_apples) // 2
    return sorted_apples[pos_half]


#list of color tuples at that position for each image
def colors_at_xy(images, x, y):
    color_list = []
    for image in images:
        if image.in_bounds(x, y): #Check True if inbound
            color = image.get_color_tuple(x, y)
            color_list.append(color)
    return color_list


def solve(images, mode):
    """
    Given a list of image objects and mode,
    compute and show a Ghost solution image based on these images.
    Mode will be None or '-good'.
    There will be at least 3 images and they will all be
    the same size.
    """
    #None or '-good'
    width = images[0].width
    height = images[1].height
    solution = SimpleImage.blank(width, height)
    for y in range(solution.height):     #Next section, best color?
        for x in range(solution.width):
            #Set the solution image to use the computed best color for each x,y
            colors = colors_at_xy(images, x, y)
            if mode == '-good':
                choose_color = good_apple_color(colors)
            else:
                choose_color = best_color(colors)
            solution.set_color_tuple(x, y, choose_color)
    solution.show()


def jpgs_in_dir(dir):
    """
    (provided)
    Given the name of a directory
    returns a list of the .jpg filenames within it.
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided)
    Given a directory name, reads all the .jpg files
    within it into memory and returns them in a list.
    Prints the filenames out as it goes.
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print(filename)
        image = SimpleImage.file(filename)
        images.append(image)
    return images


def main():
    # (provided)
    args = sys.argv[1:]
    # Command line args
    # 1 arg:  dir-of-images
    # 2 args: -good dir-of-images
    if len(args) == 1:
        images = load_images(args[0])
        solve(images, None)

    if len(args) == 2 and args[0] == '-good':
        images = load_images(args[1])
        solve(images, '-good')


if __name__ == '__main__':
    main()
