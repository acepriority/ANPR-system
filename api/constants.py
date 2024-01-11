"""
Constants for the object detection and image processing.

Attributes:
    model_path (str): The path to the saved model.
    image_shape (tuple): The shape of the images (height, width).
    original_image_path (str): Path to save the original image.
    normalized_image_path (str): Path to save the normalized image.
    normalized_image_with_bbx_path (str): Path to save the normalized image with bounding box.
    original_image_with_bbx_path (str): Path to save the original image with bounding box.
    roi_image_path (str): Path to save the Region of Interest (ROI) image.
"""





class Constants:
    def __init__(self, model_path, image_shape, original_image_path, normalized_image_path,
                 normalized_image_with_bbx_path, original_image_with_bbx_path, roi_image_path):
        self.model_path = model_path
        self.image_shape = image_shape
        self.original_image_path = original_image_path
        self.normalized_image_path = normalized_image_path
        self.normalized_image_with_bbx_path = normalized_image_with_bbx_path
        self.original_image_with_bbx_path = original_image_with_bbx_path
        self.roi_image_path = roi_image_path
