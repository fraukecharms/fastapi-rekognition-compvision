from fastapi import FastAPI, UploadFile, File

from fastapi import HTTPException
from fastapi.responses import StreamingResponse
import numpy as np

import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox


# from fastapi.responses import FileResponse
import uvicorn
import boto3
import io

# from PIL import Image, ImageDraw

# from PIL import ExifTags, ImageColor

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello there ... append '/docs' to the URL to interact with the API"}


@app.post("/predict2")
async def lookup2(photo: UploadFile = File(...)):
    """upload image"""

    client = boto3.client("rekognition")

    response = client.detect_labels(Image={"Bytes": photo.file.read()})

    return response


@app.post("/predict3")
async def lookup3(photo: UploadFile = File(...)):
    """upload image"""

    # client = boto3.client("rekognition")

    # response = client.detect_labels(Image={'Bytes': photo.file.read()})

    # Read image as a stream of bytes
    image_stream = io.BytesIO(photo.file.read())

    # Start the stream from the beginning (position zero)
    image_stream.seek(0)

    return StreamingResponse(image_stream, media_type="image/jpeg")


@app.post("/predict")
def prediction(file: UploadFile = File(...)):

    # 1. VALIDATE INPUT FILE
    filename = file.filename
    fileExtension = filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not fileExtension:
        raise HTTPException(status_code=415, detail="Unsupported file provided.")

    # 2. TRANSFORM RAW IMAGE INTO CV2 image

    # Read image as a stream of bytes
    image_stream = io.BytesIO(file.file.read())

    # Start the stream from the beginning (position zero)
    image_stream.seek(0)

    # Write the stream of bytes into a numpy array
    file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)

    # Decode the numpy array as an image
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # 3. RUN OBJECT DETECTION MODEL

    # yolov3tiny = "yolov3-tiny"
    # yolov3 = "yolov3"

    # Run object detection
    bbox, label, conf = cv.detect_common_objects(image, model="yolov3")

    # Create image that includes bounding boxes and labels
    output_image = draw_bbox(image, bbox, label, conf)

    # Save it in a folder within the server
    cv2.imwrite(f"images_uploaded/{filename}", output_image)

    # 4. STREAM THE RESPONSE BACK TO THE CLIENT

    # Open the saved image for reading in binary mode
    file_image = open(f"images_uploaded/{filename}", mode="rb")

    # Return the image as a stream specifying media type
    return StreamingResponse(file_image, media_type="image/jpeg")


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
