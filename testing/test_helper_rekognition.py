import boto3
from helper_rekognition import process_response, draw_bounding_box
from PIL import Image, ImageDraw, ImageColor
from IPython.display import Image as ipImage
from IPython.display import display as ipdisplay
import os

def test_rekognition(testpic="testpics/pic4.png"):

    client = boto3.client("rekognition")

    with open(testpic, "rb") as photo:
        response = client.detect_labels(Image={"Bytes": photo.read()})

    print(response.keys())

    assert response['ResponseMetadata']['HTTPStatusCode'] == 200
    


def test_process_response():

    testpic = "testpics/pic4.png"

    client = boto3.client("rekognition")

    with open(testpic, "rb") as photo:
        response = client.detect_labels(Image={"Bytes": photo.read()})

    boxes, _ = process_response(response)
    
    assert len(boxes) > 0




def test_draw_bounding_box():

    testpic = "testpics/pic3.jpg"

    client = boto3.client("rekognition")

    with open(testpic, "rb") as photo:

        response = client.detect_labels(Image={"Bytes": photo.read()})

    boxes, _ = process_response(response)

    photo2 = Image.open(testpic)

    imgwbox = draw_bounding_box(photo2, boxes[0])
    
    if not os.path.exists('images_with_boxes'):
        os.mkdir('images_with_boxes')
    outpath = "images_with_boxes/pic3_box.jpg"
    imgwbox.save(outpath)
    
    assert os.path.exists(outpath)
