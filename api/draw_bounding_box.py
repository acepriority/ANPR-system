"""
Draw a bounding box on the image using provided coordinates.

Args:
    image (numpy.ndarray): The input image.
    coords (numpy.ndarray): The coordinates (xmin, xmax, ymin, ymax) of the object.

Returns:
    numpy.ndarray: The image with the bounding box drawn.

Raises:
    HTTPException: If there is an error during bounding box drawing.

Notes:
    - The bounding box is drawn using the provided coordinates on the input image.
    - The color of the bounding box is (0, 255, 0), representing green.
    - The line thickness of the bounding box is set to 3 pixels.
    - The provided image is modified in-place; if you want to keep the original, make a copy before calling this method.
"""





from fastapi import HTTPException
import logging
import cv2


class BoundingBoxDrawer:
    def __init__(self):
        pass

    def draw_bounding_box(self, image, coords):
        try:
            xmin, xmax, ymin, ymax = coords[0]
            pt1 = (xmin, ymin)
            pt2 = (xmax, ymax)
            return cv2.rectangle(image, pt1, pt2, (0, 255, 0), 3)
        except Exception as e:
            logging.error(f"Error drawing bounding box: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error drawing bounding box: {str(e)}")
