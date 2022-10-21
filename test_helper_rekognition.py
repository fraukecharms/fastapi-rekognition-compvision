import boto3
from helper_rekognition import process_response, draw_bounding_boxes
from PIL import Image, ImageDraw, ImageColor
from IPython.display import Image as ipImage
from IPython.display import display as ipdisplay

def lookuptest(testpic="testpics/pic4.png"):

    client = boto3.client("rekognition")

    with open(testpic, "rb") as photo:
        response = client.detect_labels(Image={"Bytes": photo.read()})

    print(response.keys())

    return response


def process_responsetest():

    testpic = "testpics/pic4.png"

    client = boto3.client("rekognition")

    photo = open(testpic, "rb")

    response = client.detect_labels(Image={"Bytes": photo.read()})

    return process_response(response)
    
    
def lookuptest3():

    # boxes = lookuptest2()

    # with Image.open("testpic/pug.png") as im:

    im = Image.open("testpic/pug.png")
    imgWidth, imgHeight = im.size
    draw = ImageDraw.Draw(im)
    # ImageDraw.Draw(im)

    ipdisplay(im)

    print("test0")
    ipdisplay(ipImage("testpic/pug.png"))

    print(imgWidth)
    print(imgHeight)
    print("test")


def drawboundingboxes2test():

    testpic = "testpic/pic3.jpg"

    client = boto3.client("rekognition")

    photo = open(testpic, "rb")

    response = client.detect_labels(Image={"Bytes": photo.read()})

    boxes = process_response(response)

    photo2 = Image.open(testpic)

    imgwbox = drawboundingboxes2(photo2, boxes[0])

    outpath = "images_with_boxes/pic3_box.jpg"
    imgwbox.save(outpath)


def drawboundingboxes2test2():

    testpic = "testpic/pic3.jpg"

    client = boto3.client("rekognition")

    photo = open(testpic, "rb")

    response = client.detect_labels(Image={"Bytes": photo.read()})

    boxes = process_response(response)

    photo2 = Image.open(testpic)

    imgwbox = drawboundingboxes2(photo2, boxes[0])

