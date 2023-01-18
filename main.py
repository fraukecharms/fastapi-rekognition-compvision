from fastapi import FastAPI, UploadFile, File

from fastapi import HTTPException
from fastapi.responses import StreamingResponse

import uvicorn
import boto3
import io

from helper_rekognition import process_response, draw_bounding_box
from PIL import Image


app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello there ... append '/docs' to the URL to interact with the API"
    }


@app.post("/labels")
async def label_objects(photo: UploadFile = File(...)):
    """upload image"""

    client = boto3.client("rekognition")

    response = client.detect_labels(Image={"Bytes": photo.file.read()})

    return response


@app.post("/draw_box")
async def draw_box(photo: UploadFile = File(...)):
    """upload image"""

    filename = photo.filename
    file_ext = filename.split(".")[-1].lower()

    if file_ext == "jpg":
        file_ext = "jpeg"

    if not (file_ext in ("jpeg", "png")):
        raise HTTPException(status_code=415, detail="Unsupported file provided.")

    # convert image to bytearray
    photobytes = bytearray(photo.file.read())

    # send image to rekognition and extract labels and bounding boxes
    client = boto3.client("rekognition")
    response = client.detect_labels(Image={"Bytes": photobytes})
    boxes, labels = process_response(response)

    # convert bytearray to PIL image
    image_stream = io.BytesIO(photobytes)
    image_stream.seek(0)
    photo2 = Image.open(image_stream)

    imgwbox = draw_bounding_box(photo2, boxes[0], label=labels[0])

    # save PIL image to image stream
    imstream = io.BytesIO()
    imgwbox.save(imstream, file_ext)
    imstream.seek(0)

    return StreamingResponse(imstream, media_type="image/" + file_ext)


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
