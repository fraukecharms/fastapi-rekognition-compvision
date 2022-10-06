import boto3
import io
from PIL import Image, ImageDraw, ImageColor


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


def show_faces(photo, bucket):

    client = boto3.client("rekognition")

    # Load image from S3 bucket
    s3_connection = boto3.resource("s3")
    s3_object = s3_connection.Object(bucket, photo)
    s3_response = s3_object.get()

    stream = io.BytesIO(s3_response["Body"].read())
    image = Image.open(stream)

    # Call DetectFaces
    response = client.detect_faces(
        Image={"S3Object": {"Bucket": bucket, "Name": photo}}, Attributes=["ALL"]
    )

    imgWidth, imgHeight = image.size
    draw = ImageDraw.Draw(image)

    # calculate and display bounding boxes for each detected face
    print("Detected faces for " + photo)
    for faceDetail in response["FaceDetails"]:
        print(
            "The detected face is between "
            + str(faceDetail["AgeRange"]["Low"])
            + " and "
            + str(faceDetail["AgeRange"]["High"])
            + " years old"
        )

        box = faceDetail["BoundingBox"]
        left = imgWidth * box["Left"]
        top = imgHeight * box["Top"]
        width = imgWidth * box["Width"]
        height = imgHeight * box["Height"]

        print("Left: " + "{0:.0f}".format(left))
        print("Top: " + "{0:.0f}".format(top))
        print("Face Width: " + "{0:.0f}".format(width))
        print("Face Height: " + "{0:.0f}".format(height))

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

    return len(response["FaceDetails"])
