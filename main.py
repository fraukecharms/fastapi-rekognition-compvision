from fastapi import FastAPI, UploadFile, File
#from fastapi import HTTPException
from fastapi.responses import StreamingResponse
#from fastapi.responses import FileResponse
import uvicorn
import boto3
import io

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello there ... append '/docs' to url"}




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
