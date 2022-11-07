<div align="center">

[![Github Actions](https://github.com/fraukecharms/fastapi_compvision/actions/workflows/main.yml/badge.svg)](https://github.com/fraukecharms/fastapi_compvision/actions/workflows/main.yml) 
![Badge](https://codebuild.eu-west-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZGx5M0JnZXNLL3NqcXpoN0xoZ1pLVURFT0U5Tmcwb3plQzU5NXBBVUE1Q1lpMHJxZHFtNTIya1BscU1EK1RkRlp2TnFUV0huUFkwKzBvdG56a1BGcDg0PSIsIml2UGFyYW1ldGVyU3BlYyI6Indva1F2ZlZuS3VlMGdWOEEiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

</div>

# Create An Object Detection Demo 

using AWS Rekognition + FastAPI + AWS App Runner


## Docker Instructions

```sh
docker build --tag visiondemo .
docker run -p 127.0.0.1:8080:8080 visiondemo
```

## ECR Instructions


<img width="1335" alt="Screenshot 2022-11-07 at 10 15 38" src="https://user-images.githubusercontent.com/3386410/200273869-9d23277e-b70f-47c4-8967-efd02882786b.png">



## Permissions


## Run without Docker


```sh
make install
python main.py
```

## Run Docker container locally in Cloud9

```sh
docker build --tag visiondemo-rekognition .
docker run -p 127.0.0.1:8080:8080 -v $HOME/.aws/:/root/.aws:ro -e AWS_PROFILE=default visiondemo-rekognition
```

## Learning Material

* [Deep Learning For Computer Vision](https://web.eecs.umich.edu/~justincj/teaching/eecs498/WI2022/) very similar to CS231n; pytorch assignments in Google Colab
* [Building Cloud Computing Solutions at Scale](https://www.coursera.org/specializations/building-cloud-computing-solutions-at-scale)
* [AWS Technical Essentials](https://www.coursera.org/learn/aws-cloud-technical-essentials)
* [Introduction to Machine Learning in Production](https://www.coursera.org/learn/introduction-to-machine-learning-in-production)
