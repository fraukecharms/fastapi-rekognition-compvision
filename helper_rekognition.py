import boto3
import io
from PIL import Image, ImageDraw, ImageColor

from IPython.display import Image as ipImage
from IPython.display import display as ipdisplay


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

    # with Image.open("testpic/pug.png") as im:

    im = Image.open("testpic/pug.png")
    imgWidth, imgHeight = im.size
    draw = ImageDraw.Draw(im)
    #ImageDraw.Draw(im)
    # might want to include inline matplotlib???
    ipdisplay(im)
    
    print('test0')
    ipdisplay(ipImage("testpic/pug.png"))

    print(imgWidth)
    print(imgHeight)
    print("test")


def drawboundingboxes():

    image = Image.open("testpic/pug.png")

    box = lookuptest2()[0]

    imgWidth, imgHeight = image.size
    draw = ImageDraw.Draw(image)

    left = imgWidth * box[0]
    top = imgHeight * box[1]
    width = imgWidth * box[2]
    height = imgHeight * box[3]

    points = (
        (left, top),
        (left + width, top),
        (left + width, top + height),
        (left, top + height),
        (left, top),
    )
    draw.line(points, fill="#00d400", width=2)

    # Alternatively can draw rectangle. However you can't set line width.
    # draw.rectangle([left,top, left + width, top + height], outline='#00d400')

    image.show()
    ipdisplay(image)
