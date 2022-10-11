from fastapi import FastAPI, UploadFile, File

# from fastapi import HTTPException
from fastapi.responses import StreamingResponse

# from fastapi.responses import FileResponse
import uvicorn
import boto3
import io

from helper_rekognition import process_response, drawboundingboxes2
from PIL import Image

# from PIL import Image, ImageDraw

# from PIL import ExifTags, ImageColor

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello there ... append '/docs' to the URL to interact with the API"
    }


@app.post("/predict2")
async def lookup2(photo: UploadFile = File(...)):
    """upload image"""

    client = boto3.client("rekognition")

    response = client.detect_labels(Image={"Bytes": photo.file.read()})

    return response


@app.get("/showimage")
async def showfoxes():

    testpic = "testpic/pic3.jpg"

    client = boto3.client("rekognition")

    photo = open(testpic, "rb")

    response = client.detect_labels(Image={"Bytes": photo.read()})

    boxes = process_response(response)

    photo2 = Image.open(testpic)

    imgwbox = drawboundingboxes2(photo2, boxes[0])

    imgwbox2 = imgwbox.convert("RGB")
    imstream = io.BytesIO()
    imgwbox2.save(imstream, "jpeg")

    imstream.seek(0)

    return StreamingResponse(imstream, media_type="image/jpeg")


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


@app.post("/predict4")
async def lookup4(photo: UploadFile = File(...)):
    """upload image"""

    # client = boto3.client("rekognition")

    # response = client.detect_labels(Image={'Bytes': photo.file.read()})

    # Read image as a stream of bytes
    image_stream = io.BytesIO(photo.file.read())

    # Start the stream from the beginning (position zero)
    image_stream.seek(0)

    return StreamingResponse(image_stream, media_type="image/jpeg")


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
