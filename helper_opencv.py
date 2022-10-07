import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from IPython.display import Image, display


def detect_and_draw_box(model="yolov3", confidence=0.5):
    """Detects common objects on an image and creates a new image with bounding boxes.

    Args:
        filename (str): Filename of the image.
        model (str): Either "yolov3" or "yolov3-tiny". Defaults to "yolov3-tiny".
        confidence (float, optional): Desired confidence level. Defaults to 0.5.
    """
    filename = r"/root/fastapi_apprunner_compvision/testpic/pug.png"

    img = cv2.imread(filename)

    # Perform the object detection
    bbox, label, conf = cv.detect_common_objects(
        img, confidence=confidence, model=model
    )

    # Print current image's filename
    print(f"========================\nImage processed: {filename}\n")

    # Print detected objects with confidence level
    for l, c in zip(label, conf):
        print(f"Detected object: {l} with confidence level of {c}\n")

    # Create a new image that includes the bounding boxes
    output_image = draw_bbox(img, bbox, label, conf)

    # Save the image in the directory images_with_boxes
    cv2.imwrite(
        f"/root/fastapi_apprunner_compvision/images_with_boxes/pug.png", output_image
    )

    # Display the image with bounding boxes
    display(Image(f"/root/fastapi_apprunner_compvision/images_with_boxes/pug.png"))
