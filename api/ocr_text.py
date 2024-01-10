"""
Perform Optical Character Recognition (OCR) on a Region of Interest (ROI) image.

Args:
    roi_image (numpy.ndarray): The input ROI image.

Returns:
    List[str]: A list of detected texts in the ROI.

Raises:
    HTTPException: If there is an error during OCR processing.

Note:
    The OCRProcessor class uses the EasyOCR library to perform OCR on the provided ROI image.
    It initializes with a specified language (default is 'en').
"""





from fastapi import HTTPException
import easyocr
import logging


class OCRProcessor:
    def __init__(self, language='en'):
        self.reader = easyocr.Reader([language])

    def ocr_text(self, roi_image):
        try:
            result = self.reader.readtext(roi_image)
            return [detection[1] for detection in result]
        except Exception as e:
            logging.error(f"Error in OCR: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error in OCR: {str(e)}")
