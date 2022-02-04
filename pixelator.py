import cv2
from typing import NewType, Tuple


Pixel = NewType('Pixel', Tuple[int, int, int])


image_path = 'images/image.jpg'

image = cv2.imread(image_path)


def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized


def normalize_color(pixel: Pixel, color_step: int) -> Pixel:
    return (pixel[0] // color_step * color_step, pixel[1] // color_step * color_step, pixel[2] // color_step * color_step)
    

def pixelate(new_image, pixel_detail=256, color_step=64):
    old_size = new_image.shape[:2]
    new_image = image_resize(new_image, width=pixel_detail, inter=cv2.INTER_NEAREST)

    # Iterate over every pixel in the image
    for y in range(0, new_image.shape[0]):
        for x in range(0, new_image.shape[1]):
            pixel: Pixel = new_image[y,x]
            new_image[y,x] = normalize_color(pixel, color_step)

    # Resize the image back to its original size
    return image_resize(new_image, width=old_size[1], height=old_size[0], inter=cv2.INTER_NEAREST)


cv2.imshow('Original', image)

cv2.imshow('Pixelated (1024)', pixelate(image, pixel_detail=1024))
cv2.imshow('Pixelated (512)', pixelate(image, pixel_detail=512))
cv2.imshow('Pixelated (256)', pixelate(image, pixel_detail=256))
cv2.imshow('Pixelated (128)', pixelate(image, pixel_detail=128))
cv2.imshow('Pixelated (64)', pixelate(image, pixel_detail=64))
cv2.imshow('Pixelated (32)', pixelate(image, pixel_detail=32))
cv2.imshow('Pixelated (16)', pixelate(image, pixel_detail=16))
cv2.imshow('Pixelated (8)', pixelate(image, pixel_detail=8))
cv2.imshow('Pixelated (4)', pixelate(image, pixel_detail=4))
cv2.imshow('Pixelated (2)', pixelate(image, pixel_detail=2))
cv2.imshow('Pixelated (1)', pixelate(image, pixel_detail=1))


cv2.waitKey(0)
cv2.destroyAllWindows()

