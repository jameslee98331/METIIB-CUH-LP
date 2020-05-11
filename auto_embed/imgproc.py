import numpy as np
from collections import namedtuple
import matplotlib.pyplot as plt
import cv2


def view_img(img: np.ndarray) -> None:
    plt.imshow(img)
    plt.show()


def crop(img: np.ndarray, corner: namedtuple) -> np.ndarray:
    """
    Args:
        img (np.ndarray): array of the image with RGB values to be cropped
        corner (namedtuple): named tuple in the format namedtuple('rect', 'start, finish')
                             rect.start represents the top left corner of a cropping frame
                             rect.finish represents the bottom right corner of a cropping frame
    Returns:
        np.ndarray: array of the image with RGB values cropped with limits from corner (namedtuple)
    """

    return img[corner.start[0]:corner.end[0], corner.start[1]:corner.end[1]]


def bounding_box(hsv_img: np.ndarray) -> tuple:
    # create NumPy arrays from the red color boundaries [H, S, V]
    lower = np.array([0, 30, 30], dtype="uint8")
    upper = np.array([255, 255, 255], dtype="uint8")

    # find the colors within the specified boundaries and apply the mask
    mask = cv2.inRange(hsv_img, lower, upper)
    output = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)

    ret, thresh = cv2.threshold(mask, 40, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0:
        # draw in blue the contours that were founded
        cv2.drawContours(output, contours, -1, 255, 3)

        # find the biggest contour (c) by the area
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return x, y, w, h, output
