"""
Extract the Region of Interest (ROI) from the original image using provided coordinates.

Args:
    image (numpy.ndarray): The original image.
    coords (numpy.ndarray): The object coordinates.

Returns:
    numpy.ndarray: The extracted ROI image.

Raises:
    HTTPException: If there is an error during ROI extraction.

Notes:
    - The coordinates are expected in the format (xmin, xmax, ymin, ymax).
    - The provided image is cropped to extract the Region of Interest.
    - Ensure that the coordinates are within the valid range of the image dimensions.
    - The extracted ROI image is returned for further processing or analysis.
"""





from fastapi import HTTPException
import logging


class ROIExtractor:
    def __init__(self):
        pass

    def extract_roi(self, image, coords):
        try:
            xmin, xmax, ymin, ymax = coords[0]
            roi = image[ymin:ymax, xmin:xmax]
            return roi
        except Exception as e:
            logging.error(f"Error extracting ROI: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error extracting ROI: {str(e)}")
