"""
Read and decode the uploaded image.

Args:
    image_encoded (bytes): Encoded image data.

Returns:
    PIL.Image.Image: Decoded PIL Image.

Raises:
    HTTPException 404: If the file is not found.
    HTTPException 400: If there is an error reading the image.

Notes:
    - This class is designed to read and decode images for further processing.
    - Ensure that the provided image data is in the correct format.
    - Handle the returned decoded image accordingly based on your application requirements.
"""





from fastapi import HTTPException
import cv2
import PIL
from PIL import Image
from io import BytesIO
import logging

class ImageReader:
    def __init__(self):
        pass

    def read_image(self, image_encoded):
        try:
            pil_image = Image.open(BytesIO(image_encoded))
            return pil_image
        except FileNotFoundError as e:
            logging.error(f"File not found: {str(e)}")
            raise HTTPException(status_code=404, detail="File not found")
        except (PIL.UnidentifiedImageError, cv2.error) as e:
            logging.error(f"Error reading image: {str(e)}")
            raise HTTPException(status_code=400, detail="Invalid image format")

            ww_r4UWn5@%2z4A
