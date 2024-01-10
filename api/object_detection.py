"""
Perform object detection on the normalized image.

Args:
    model: The object detection model.

Returns:
    numpy.ndarray: Object coordinates.

Raises:
    HTTPException: If there is an error during object detection.

Notes:
    - The model should be a TensorFlow or compatible model for object detection.
    - The coordinates are returned in the format (xmin, xmax, ymin, ymax).
    - Ensure that the provided normalized image is suitable for the object detection model.
    - The object coordinates can be used for further analysis or visualization.
"""





from fastapi import HTTPException
import numpy as np
import logging


class ObjectDetector:
    def __init__(self, model):
        self.model = model

    def object_detection(self, norm_image):
        try:
            h, w, d = norm_image.shape
            image = norm_image.reshape(1, 224, 224, 3)
            coords = self.model.predict(image)

            denorm = np.array([w, w, h, h])
            coords = coords * denorm
            coords = coords.astype(np.int32)

            return coords
        except Exception as e:
            logging.error(f"Error in object detection: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error in object detection: {str(e)}")
