"""
Process the PIL image for object detection.

Args:
    pil_image (PIL.Image.Image): Input PIL image.

Returns:
    tuple: Tuple containing unchanged image and normalized image.

Raises:
    HTTPException 500: If there is an error processing the image.

Notes:
    - This class is designed to process PIL images for object detection.
    - Ensure that the provided PIL image is in the correct format.
    - Handle the returned unchanged and normalized images accordingly based on your application requirements.
"""





from fastapi import HTTPException
import cv2
import numpy as np
import logging


class PILImageProcessor:
    def __init__(self, image_shape):
        self.image_shape = image_shape

    def process_image_pil(self, pil_image):
        try:
            if pil_image.mode != "RGB":
                pil_image = pil_image.convert("RGB")

            input_image = np.array(pil_image)

            unchanged_image = np.copy(input_image)
            unchanged_image = np.array(unchanged_image, dtype=np.uint8)
            unchanged_image = cv2.resize(unchanged_image, self.image_shape)
            unchanged_image = cv2.cvtColor(unchanged_image, cv2.COLOR_RGB2BGR)

            image_for_norm = np.copy(input_image)
            image_for_norm = np.array(image_for_norm, dtype=np.uint8)
            image_for_norm = cv2.resize(image_for_norm, self.image_shape)
            image_for_norm = cv2.cvtColor(image_for_norm, cv2.COLOR_RGB2BGR)

            norm_image = cv2.normalize(image_for_norm, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

            return unchanged_image, norm_image
        except Exception as e:
            logging.error(f"Error processing image: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")

