import boto3
import io
from PIL import Image, ImageDraw, ImageColor


from fastapi import FastAPI, UploadFile, File
from fastapi import HTTPException
from fastapi.responses import StreamingResponse

from IPython.display import Image as ipImage
from IPython.display import display as ipdisplay


def lookuptest(testpic = "testpic/pug.png"):

    client = boto3.client("rekognition")

    with open(testpic, "rb") as photo:
        response = client.detect_labels(Image={"Bytes": photo.read()})

    print(response.keys())

    return response




def process_responsetest():
    
    testpic = "testpic/pug.png"

    client = boto3.client("rekognition")

    photo = open(testpic, "rb")
    
    response = client.detect_labels(Image={"Bytes": photo.read()})

    return process_response(response)
    

def process_response(response, verbose = False):


    # print(response.keys())
    boxes = []

    if verbose:
        print("Detected labels")
        print()
        
    for label in response["Labels"]:
        if verbose:
            print("Label: " + label["Name"])
            print("Confidence: " + str(label["Confidence"]))
            print("Instances:")
            
        for instance in label["Instances"]:
            if verbose:
                print("  Bounding box")
                print("    Top: " + str(instance["BoundingBox"]["Top"]))
                print("    Left: " + str(instance["BoundingBox"]["Left"]))
                print("    Width: " + str(instance["BoundingBox"]["Width"]))
                print("    Height: " + str(instance["BoundingBox"]["Height"]))
                print("  Confidence: " + str(instance["Confidence"]))
                print()

            box = instance["BoundingBox"]
            boxes.append(box)


    return boxes



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





def drawboundingboxes(testpic = "testpic/pic3.jpg"):

    image = Image.open(testpic)

    box = process_response(lookuptest(testpic = testpic))[0]

    imgWidth, imgHeight = image.size
    draw = ImageDraw.Draw(image)

    left = imgWidth * box["Left"]
    top = imgHeight * box["Top"]
    width = imgWidth * box["Width"]
    height = imgHeight * box["Height"]

    points = (
        (left, top),
        (left + width, top),
        (left + width, top + height),
        (left, top + height),
        (left, top),
    )
    draw.line(points, fill="#00d400", width=2)

    # alternatively can draw rectangle, no line width option though
    # draw.rectangle([left,top, left + width, top + height], outline='#00d400')

    # image.show()
    
    # displays image when run from a jupyter notebook; useful for debugging/experimenting
    # you can comment next line out for Swagger UI demo in browser
    ipdisplay(image)
    
    # save image with boxes to file
    outpath = "images_with_boxes/pic.png"
    image.save(outpath)


def drawboundingboxes2test():
    
    testpic = "testpic/pic3.jpg"

    client = boto3.client("rekognition")

    photo = open(testpic, 'rb')
    
    response = client.detect_labels(Image={"Bytes": photo.read()})

    boxes = process_response(response)
    
    photo2 = Image.open(testpic)
    
    imgwbox = drawboundingboxes2(photo2, boxes[0])
    
    outpath = "images_with_boxes/pic3_box.jpg"
    imgwbox.save(outpath)


def drawboundingboxes2test2():
    
    testpic = "testpic/pic3.jpg"

    client = boto3.client("rekognition")

    photo = open(testpic, 'rb')
    
    response = client.detect_labels(Image={"Bytes": photo.read()})

    boxes = process_response(response)
    
    photo2 = Image.open(testpic)
    
    imgwbox = drawboundingboxes2(photo2, boxes[0])
    
    imstream = io.BytesIO(imgwbox.tobytes())
    
    imstream.seek(0)
    
    return StreamingResponse(imstream, media_type="image/jpeg")

def drawboundingboxes2test3():
    
    testpic = "testpic/pic3.jpg"

    client = boto3.client("rekognition")

    photo = open(testpic, 'rb')
    
    response = client.detect_labels(Image={"Bytes": photo.read()})

    boxes = process_response(response)
    
    photo2 = Image.open(testpic)
    
    imgwbox = drawboundingboxes2(photo2, boxes[0])
    
    
    return StreamingResponse(imgwbox, media_type="image/jpeg")


def drawboundingboxes2(image, box):


    imgWidth, imgHeight = image.size
    draw = ImageDraw.Draw(image)

    left = imgWidth * box["Left"]
    top = imgHeight * box["Top"]
    width = imgWidth * box["Width"]
    height = imgHeight * box["Height"]

    points = (
        (left, top),
        (left + width, top),
        (left + width, top + height),
        (left, top + height),
        (left, top),
    )
    draw.line(points, fill="#00d400", width=2)

    # alternatively can draw rectangle, no line width option though
    # draw.rectangle([left,top, left + width, top + height], outline='#00d400')

    # image.show()
    
    # displays image when run from a jupyter notebook; useful for debugging/experimenting
    # you can comment next line out for Swagger UI demo in browser
    '''
    ipdisplay(image)
    
    # save image with boxes to file
    outpath = "images_with_boxes/pic.png"
    image.save(outpath)
    '''
    
    return image
