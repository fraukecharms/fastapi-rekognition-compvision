<div align="center">

[![Github Actions](https://github.com/fraukecharms/fastapi_compvision/actions/workflows/main.yml/badge.svg)](https://github.com/fraukecharms/fastapi_compvision/actions/workflows/main.yml) 
![Badge](https://codebuild.eu-west-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZGx5M0JnZXNLL3NqcXpoN0xoZ1pLVURFT0U5Tmcwb3plQzU5NXBBVUE1Q1lpMHJxZHFtNTIya1BscU1EK1RkRlp2TnFUV0huUFkwKzBvdG56a1BGcDg0PSIsIml2UGFyYW1ldGVyU3BlYyI6Indva1F2ZlZuS3VlMGdWOEEiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

</div>

# Build A Computer Vision Demo 

using AWS Rekognition + FastAPI + AWS App Runner


## Docker Instructions

`docker build .`

`docker build --tag visiondemo .`

`docker run -p 127.0.0.1:8080:8080 visiondemo`


## ECR Instructions


<img alt="ECR push commands" width="525" src="https://user-images.githubusercontent.com/3386410/196132461-7cd7c53e-cd52-401e-972c-68fbec15937c.png">




## Testing without docker

`make install`

`python main.py`


## Learning Material

* Uni Michigan, more up to date version than the stanford course, great assignments
* coursera specialization by noah gift
* aws technical essentials, by nature a little bit boring but the instructors make it as fun as possible
* machine learning in production, quick overview of things to keep in mind
