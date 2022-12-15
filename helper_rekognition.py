from PIL import ImageDraw, ImageFont


def process_response(response, verbose=False):

    # print(response.keys())
    boxes = []
    labels = []

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
            labels.append(label["Name"])

    return boxes, labels


def draw_bounding_boxes(image, box):

    imgWidth, imgHeight = image.size
    draw = ImageDraw.Draw(image)

    left = imgWidth * box["Left"]
    top = imgHeight * box["Top"]
    width = imgWidth * box["Width"]
    height = imgHeight * box["Height"]
    right = left + width
    bottom = top + height


    # linewidth = int((imgWidth + imgHeight) // 200) + 2

    # draw.line(points, fill="#c73286", width=linewidth)

    points = [(left, top), (right, bottom)]

    draw.rectangle(points, outline="#c73286", width=4)

    size = 25

    font = ImageFont.truetype("font/OpenSans-Regular.ttf", size)
    label = "fox"

    draw.text((left, top), label, font=font, anchor="lt")

    # might also be able to do ImageDraw.textbbox(xy, text, font=None, anchor=None, ....
    # and avoid calculations, see documentation

    textbb = draw.textbbox((left, top), label, font=font, anchor="lt")

    draw.rectangle(textbb)

    # alternative
    # textbb = font.getbbox("fox")
    # draw.rectangle([textbb[0] + left, textbb[1] + top, textbb[2] + left, textbb[3] + top])

    return image
