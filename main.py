from fastapi import FastAPI, UploadFile, File

# from fastapi import HTTPException
from fastapi.responses import StreamingResponse

# from fastapi.responses import FileResponse
import uvicorn
import boto3
import io

from PIL import Image, ImageDraw

# from PIL import ExifTags, ImageColor

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello there ... append '/docs' to url"}


def lookuptest():

    client = boto3.client("rekognition")

    with open("testpic/pug.png", "rb") as photo:
        response = client.detect_labels(Image={"Bytes": photo.read()})

    print(response.keys())

    return response


def lookuptest2():

    client = boto3.client("rekognition")

    # with open("testpic/pug.png", "rb") as photo:

    photo = open("testpic/pug.png", "rb")
    response = client.detect_labels(Image={"Bytes": photo.read()})

    # print(response.keys())
    boxes = []

    print("Detected labels")
    print()
    for label in response["Labels"]:
        print("Label: " + label["Name"])
        print("Confidence: " + str(label["Confidence"]))
        print("Instances:")
        for instance in label["Instances"]:
            print("  Bounding box")
            print("    Top: " + str(instance["BoundingBox"]["Top"]))
            print("    Left: " + str(instance["BoundingBox"]["Left"]))
            print("    Width: " + str(instance["BoundingBox"]["Width"]))
            print("    Height: " + str(instance["BoundingBox"]["Height"]))
            print("  Confidence: " + str(instance["Confidence"]))
            print()

            btop = instance["BoundingBox"]["Top"]
            bleft = instance["BoundingBox"]["Left"]
            bwidth = instance["BoundingBox"]["Width"]
            bheight = instance["BoundingBox"]["Height"]

            box = (btop, bleft, bwidth, bheight)
            boxes.append(box)

        print("Parents:")
        for parent in label["Parents"]:
            print("   " + parent["Name"])
        print("----------")
        print()

    image_stream = io.BytesIO(photo.read())

    # Start the stream from the beginning (position zero)
    image_stream.seek(0)

    return boxes
    # return StreamingResponse(image_stream, media_type="image/jpeg")


def lookuptest3():

    # boxes = lookuptest2()

    with Image.open("testpic/pug.png") as im:

        imgWidth, imgHeight = im.size
        # draw = ImageDraw.Draw(im)
        ImageDraw.Draw(im)
        # might want to include inline matplotlib???
        # im.show()

    print(imgWidth)
    print(imgHeight)


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


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
