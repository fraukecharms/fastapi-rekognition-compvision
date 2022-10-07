[![Github Actions](https://github.com/fraukecharms/fastapi_compvision/actions/workflows/main.yml/badge.svg)](https://github.com/fraukecharms/fastapi_compvision/actions/workflows/main.yml)

![Badge]([<build badge URL>](https://codebuild.eu-west-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZGx5M0JnZXNLL3NqcXpoN0xoZ1pLVURFT0U5Tmcwb3plQzU5NXBBVUE1Q1lpMHJxZHFtNTIya1BscU1EK1RkRlp2TnFUV0huUFkwKzBvdG56a1BGcDg0PSIsIml2UGFyYW1ldGVyU3BlYyI6Indva1F2ZlZuS3VlMGdWOEEiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main))



# fastapi
FastAPI + AWS App Runner


## Instructions for docker

`docker build .`

`docker build --tag visiondemo .`

`docker run -p 127.0.0.1:8080:8080 visiondemo`


## run docker
`docker build .`

Note this is your container name use:  `docker image ls` to find:

`docker run -p 127.0.0.1:8080:8080 54a55841624f`

![fastapi-step1](https://user-images.githubusercontent.com/58792/131587003-f5667c28-7cbe-402e-8795-f32a6ca9a4d1.png)
![fastapi-step2](https://user-images.githubusercontent.com/58792/131587286-341e795c-76dc-46a1-8ee9-528134410935.png)
![fastapi-step3](https://user-images.githubusercontent.com/58792/131587004-198ad6d5-2197-4de5-a6dd-4eb3c41e675e.png)
![fastapi-step4](https://user-images.githubusercontent.com/58792/131587005-866b0974-63d7-4fed-abf2-9c634721669f.png)


## Verify Swagger Working


![fastapi-swagger](https://user-images.githubusercontent.com/58792/131587676-b22c5877-0e75-49e7-a1a6-b580ba922e67.png)


##
`python main.py`


## Learning Material

* Uni Michigan, more up to date version than the stanford course, great assignments
* coursera specialization by noah gift
* aws technical essentials, by nature a little bit boring but the instructors make it as fun as possible
* machine learning in production, quick overview of things to keep in mind
