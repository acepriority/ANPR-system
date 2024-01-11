"""
Endpoint to predict object coordinates in an uploaded image and provide visualizations.

Parameters:
    - file (UploadFile): The uploaded image file.

Returns:
    dict: A dictionary containing base64-encoded images and OCR results.

Notes:
    - The 'original_image' is the uploaded image in its original form.
    - The 'normalized_image' is the preprocessed image suitable for object detection.
    - The 'normalized_image_with_bbx' includes bounding boxes drawn around detected objects.
    - The 'original_copy_with_bbx' is the original image with bounding boxes added.
    - The 'roi_image' represents the Region of Interest extracted based on detected objects.
    - 'ocr_results' contains a list of texts detected in the Region of Interest using OCR.

Raises:
    HTTPException: If there is an issue with file handling, image processing, or object detection.
"""





from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import base64
import cv2
import logging


from ocr_text import OCRProcessor
from extract_roi import ROIExtractor
from draw_bounding_box import BoundingBoxDrawer
from object_detection import ObjectDetector
from read_image import ImageReader
from process_image_pil import PILImageProcessor
from load_model import ModelLoader
from constants import Constants


constants = Constants(
    model_path=r'"C:\Users\HP\Desktop\saved_model\sys_model.h5"',
    image_shape=(224, 224),
    original_image_path="original_image.png",
    normalized_image_path="normalized_image.png",
    normalized_image_with_bbx_path="normalized_image_bbx.png",
    original_image_with_bbx_path="original_image_bbx.png",
    roi_image_path="roi_image.png"
)


image_reader = ImageReader()
pil_image_processor = PILImageProcessor(image_shape=constants.image_shape)
model_loader = ModelLoader(model_path=constants.model_path)
model = model_loader.load_model()
object_detector = ObjectDetector(model=model)
bounding_box_drawer = BoundingBoxDrawer()
roi_extractor = ROIExtractor()
ocr_processor = OCRProcessor()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup():
    app.state.model = model_loader.load_model()


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        pil_image = image_reader.read_image(await file.read())
        original_image, normalized_image = pil_image_processor.process_image_pil(pil_image)

        coords = object_detector.object_detection(normalized_image)

        normalized_image_with_bbx = bounding_box_drawer.draw_bounding_box(normalized_image.copy(), coords)
        original_image_with_bbx = bounding_box_drawer.draw_bounding_box(original_image.copy(), coords)

        roi_image = roi_extractor.extract_roi(original_image_with_bbx, coords)

        ocr_result = ocr_processor.ocr_text(roi_image)

        logging.info(f"Input Image size: {pil_image.size}")
        logging.info(f"Input original image with bbx: {original_image_with_bbx.size}")
        logging.info(f"Input ROI Image size: {roi_image.size}")
        logging.info(f"OCR Result: {ocr_result}")

        """
        cv2.imwrite(constants.original_image_path, cv2.cvtColor(original_image, cv2.COLOR_RGB2BGR))
        cv2.imwrite(constants.normalized_image_path, cv2.cvtColor(normalized_image, cv2.COLOR_RGB2BGR))
        cv2.imwrite(constants.normalized_image_with_bbx_path, cv2.cvtColor(normalized_image_with_bbx, cv2.COLOR_RGB2BGR))
        cv2.imwrite(constants.original_image_with_bbx_path, cv2.cvtColor(original_image_with_bbx, cv2.COLOR_RGB2BGR))
        cv2.imwrite(constants.roi_image_path, cv2.cvtColor(roi_image, cv2.COLOR_RGB2BGR))
        """

        original_image_base64 = base64.b64encode(cv2.imencode('.png', original_image)[1].tobytes()).decode('utf-8')
        normalized_image_base64 = base64.b64encode(cv2.imencode('.png', normalized_image)[1].tobytes()).decode('utf-8')
        normalized_image_with_bbx_base64 = base64.b64encode(cv2.imencode('.png', normalized_image_with_bbx)[1].tobytes()).decode('utf-8')
        original_copy_with_bbx_base64 = base64.b64encode(cv2.imencode('.png', original_image_with_bbx)[1].tobytes()).decode('utf-8')
        roi_image_base64 = base64.b64encode(cv2.imencode('.png', roi_image)[1].tobytes()).decode('utf-8')

        return {
            "original_image": original_image_base64,
            "normalized_image": normalized_image_base64,
            "normalized_image_with_bbx": normalized_image_with_bbx_base64,
            "original_copy_with_bbx": original_copy_with_bbx_base64,
            "roi_image": roi_image_base64,
            "ocr_results": ocr_result
        }
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
