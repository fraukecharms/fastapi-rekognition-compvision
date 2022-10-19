from fastapi import FastAPI, UploadFile, File

from fastapi import HTTPException
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


@app.post("/labels")
async def label_objects(photo: UploadFile = File(...)):
    """upload image"""

    client = boto3.client("rekognition")

    response = client.detect_labels(Image={"Bytes": photo.file.read()})

    return response


@app.post("/draw_box")
async def draw_bounding_box(photo: UploadFile = File(...)):
    """upload image"""

    filename = photo.filename
    fileExtension = filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not fileExtension:
        raise HTTPException(status_code=415, detail="Unsupported file provided.")

    photobytes = bytearray(photo.file.read())

    client = boto3.client("rekognition")
    response = client.detect_labels(Image={"Bytes": photobytes})
    boxes = process_response(response)
    

    image_stream = io.BytesIO(photobytes)
    image_stream.seek(0)
    photo2 = Image.open(image_stream)
    
    imgwbox = drawboundingboxes2(photo2, boxes[0])

    imgwbox2 = imgwbox.convert("RGB")
    imstream = io.BytesIO()
    imgwbox2.save(imstream, "jpeg")

    imstream.seek(0)

    return StreamingResponse(imstream, media_type="image/jpeg")


#uncomment to show example pic with bounding box
#@app.get("/showimage")
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


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
