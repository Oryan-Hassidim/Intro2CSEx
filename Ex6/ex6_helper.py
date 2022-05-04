##############################################################################
# FILE: ex6_helper.py
# EXERCISE: Intro2cs ex6 2021-2022
# WRITER: Intro2CS 1 2021-2022 staff
# DESCRIPTION:A helper file for ex6 that masks handling with images
##############################################################################

##############################################################################
#                                   Imports                                  #
##############################################################################
from PIL import Image as PILImage
from copy import deepcopy
from typing import List, Union

##############################################################################
#                                   Typing                                   #
##############################################################################
SingleChannelImage = List[List[int]]
ColoredImage = List[List[List[int]]]
Image = Union[ColoredImage, SingleChannelImage]
Kernel = List[List[float]]


##############################################################################
#                                 CONSTANTS                                  #
##############################################################################
GREYSCALE_CODE = "L"
RGB_CODE = "RGB"

##############################################################################
#                              Helper Functions                              #
##############################################################################
def load_image(image_filename: str) -> Image:
    """
    Loads the image stored in the path image_filename and return it as a list
    of lists.
    :param image_filename: a path to an image file. If path doesn't exist an
    exception will be thrown.
    :return: a multi-dimensional list representing the image in the format
    rows X cols X channels. The list is 2D in case of a grayscale image and 3D
    in case it's colored.
    """
    img = PILImage.open(image_filename).convert(RGB_CODE)
    image = __lists_from_pil_image(img)
    return image


def show_image(image: Image) -> None:
    """
    Displays an image.
    :param image: an image represented as a multi-dimensional list of the
    format rows X cols X channels.
    """
    __pil_image_from_lists(image).show()


def save_image(image: Image, filename: str) -> None:
    """
    Converts an image represented as lists to an Image object and saves it as
    an image file at the path specified by filename.
    :param image: an image represented as a multi-dimensional list.
    :param filename: a path in which to save the image file. If the path is
    incorrect, an exception will be thrown.
    """
    if not filename.endswith('.png'):
        filename = f'{filename.split(".")[0]}.png'

    __pil_image_from_lists(image).save(filename)


def __lists_from_pil_image(image: PILImage) -> Image:
    """
    Converts an Image object to an image represented as lists.
    :param image: a PIL Image object
    :return: the same image represented as multi-dimensional list.
    """
    width, height = image.size
    pixels = list(image.getdata())
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    if type(pixels[0][0]) == tuple:
        for i in range(height):
            for j in range(width):
                pixels[i][j] = list(pixels[i][j])
    return pixels


def __pil_image_from_lists(image_as_lists: Image) -> PILImage:
    """
    Creates an Image object out of an image represented as lists.
    :param image_as_lists: an image represented as multi-dimensional list.
    :return: the same image as a PIL Image object.
    """
    image_as_lists_copy = deepcopy(image_as_lists)
    height = len(image_as_lists_copy)
    width = len(image_as_lists_copy[0])

    if type(image_as_lists_copy[0][0]) == list:
        for i in range(height):
            for j in range(width):
                image_as_lists_copy[i][j] = tuple(image_as_lists_copy[i][j])
        im = PILImage.new(RGB_CODE, (width, height))
    else:
        im = PILImage.new(GREYSCALE_CODE, (width, height))

    for i in range(width):
        for j in range(height):
            im.putpixel((i, j), image_as_lists_copy[j][i])
    return im

