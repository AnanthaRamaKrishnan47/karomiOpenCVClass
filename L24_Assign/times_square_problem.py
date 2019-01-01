import cv2
import numpy as np
import sys


# noinspection PyUnresolvedReferences


def mouse_handler(event, x, y,flags, data):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(data['im'], (x, y), 3, (0, 0, 255), 5, 16)
        cv2.imshow("Image", data['im'])
        if len(data['points']) < 4:
            data['points'].append([x, y])


# noinspection PyUnresolvedReferences


def get_four_points(im):
    # Set up data to send to mouse handler
    data = {}
    data['im'] = im.copy()
    data['points'] = []

    # Set the callback function for any mouse event
    cv2.imshow("Image", im)
    cv2.setMouseCallback("Image", mouse_handler, data)
    cv2.waitKey(0)

    # Convert array to np.array
    points = np.vstack(data['points']).astype(float)

    return points


# noinspection PyUnresolvedReferences


if __name__ == '__main__':
    # Read source image.
    # noinspection PyUnresolvedReferences
    im_src = cv2.imread(r'C:\Users\arkma\PycharmProjects\karomiOpenCVClass\Resources\Images\batWarp.jpg')
    size = im_src.shape

    # Create a vector of source points.
    pts_src = np.array(
        [
            [0, 0],
            [size[1] - 1, 0],
            [size[1] - 1, size[0] - 1],
            [0, size[0] - 1]
        ], dtype=float
    )

    # Read destination image
    # noinspection PyUnresolvedReferences
    im_dst = cv2.imread(r'C:\Users\arkma\PycharmProjects\karomiOpenCVClass\Resources\Images\times-square.jpg')

    # Get four corners of the billboard
    # noinspection PyUnresolvedReferences
    print ('Click on four corners of a billboard and then press ENTER')
    pts_dst = get_four_points(im_dst)

    # Calculate Homography between source and destination points
    # noinspection PyUnresolvedReferences
    h, status = cv2.findHomography(pts_src, pts_dst)

    # Warp source image
    # noinspection PyUnresolvedReferences
    im_temp = cv2.warpPerspective(im_src, h, (im_dst.shape[1], im_dst.shape[0]))

    # Black out polygonal area in destination image.
    # noinspection PyUnresolvedReferences
    cv2.fillConvexPoly(im_dst, pts_dst.astype(int), 0, 16)

    # Add warped source image to destination image.
    im_dst = im_dst + im_temp

    # Display image.
    # noinspection PyUnresolvedReferences
    cv2.imshow("Image", im_dst)
    # noinspection PyUnresolvedReferences
    cv2.waitKey(0)
