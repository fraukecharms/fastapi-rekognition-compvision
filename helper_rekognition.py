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


def draw_bounding_box(image, box, label=None):

    imgWidth, imgHeight = image.size
    draw = ImageDraw.Draw(image, mode="RGBA")

    linewidth = max(int((imgWidth + imgHeight) // 300), 2)
    linewidth_textbox = max(int(linewidth // 3), 1)
    textsize = linewidth * 4

    # shift is used to add margins around text bounding box below
    shift = (
        -3 * linewidth_textbox,
        -3 * linewidth_textbox,
        3 * linewidth_textbox,
        3 * linewidth_textbox,
    )

    left = imgWidth * box["Left"]
    top = imgHeight * box["Top"]
    width = imgWidth * box["Width"]
    height = imgHeight * box["Height"]
    right = left + width
    bottom = top + height

    points = [(left, top), (right, bottom)]

    draw.rectangle(points, outline="#c73286", width=linewidth)

    if label:

        font = ImageFont.truetype("font/OpenSans-Regular.ttf", textsize)

        textanchor = (left + 2 * linewidth, top + 2 * linewidth)
        draw.text(textanchor, label, font=font, anchor="lt")

        textbb = draw.textbbox(textanchor, label, font=font, anchor="lt")

        # text bounding box with margins
        spaceybox = [sum(x) for x in zip(textbb, shift)]

        draw.rectangle(spaceybox, width=linewidth_textbox, fill=(255, 255, 255, 128))
        # draw.rectangle(textbb, width = linewidth//2 + 1)

    return image
