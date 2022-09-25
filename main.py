from fastapi import FastAPI
from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn
from lambdatest import label_function
import boto3
import io

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello there ... append '/docs' to url"}

@app.post("/predict1")
async def lookup1(name: str):
    """label image in s3 bucket"""
    bucket = 'compvision-lambdatrigger-bucket'
    

    return label_function(bucket, name)
    
    
@app.post("/predict2")
async def lookup2(photo: UploadFile = File(...)):
    """upload image"""
    
    client = boto3.client("rekognition")

    response = client.detect_labels(Image={'Bytes': photo.file.read()})
        
    return response
    

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
