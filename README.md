<div align="center">

[![Github Actions](https://github.com/fraukecharms/fastapi_compvision/actions/workflows/main.yml/badge.svg)](https://github.com/fraukecharms/fastapi_compvision/actions/workflows/main.yml) 
![Badge](https://codebuild.eu-west-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZGx5M0JnZXNLL3NqcXpoN0xoZ1pLVURFT0U5Tmcwb3plQzU5NXBBVUE1Q1lpMHJxZHFtNTIya1BscU1EK1RkRlp2TnFUV0huUFkwKzBvdG56a1BGcDg0PSIsIml2UGFyYW1ldGVyU3BlYyI6Indva1F2ZlZuS3VlMGdWOEEiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

</div>

# Create an Object Detection Demo 

You can use this repo to quickly create a live public(!) demo website for object detection. The prediction requests are sent to AWS' built-in Rekognition service. If you are looking for a solution that sends requests to your own Sagemaker endpoint, check out [this repo](https://github.com/fraukecharms/fastapi-sagemaker-compvision) instead.

## Before You Start
Make sure that you do all your work in a region where App Runner is available (e.g. `eu-west-1` if you are based in Europe).

## Walk-Through Screen Recording
[Here](https://www.youtube.com/watch?v=y6bNoQvozu8) is an example of setting up a Cloud9 environment for your repo. Once that is up and running, feel free to follow along here:


## Docker Instructions

```sh
docker build --tag visiondemo-rekognition .
```
```sh
docker run -p 127.0.0.1:8080:8080 -v $HOME/.aws/:/root/.aws:ro -e \
    AWS_PROFILE=default visiondemo-rekognition
```

## Push to ECR


<img width="1335" alt="Screenshot 2022-11-07 at 10 15 38" src="https://user-images.githubusercontent.com/3386410/200273869-9d23277e-b70f-47c4-8967-efd02882786b.png">



## App Runner Permissions


```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "tasks.apprunner.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

```


## (Optional) Run without Docker


```sh
make install
python main.py
```

## (Optional) Automated Testing with Github Actions

If you are interested in automated testing, check out the `main.yml` file in `.github/workflows/`. You can set this up by configuring OpenID Connect in AWS and creating an IAM role for your repo. You can read more about it [here](https://github.com/aws-actions/configure-aws-credentials) and [here](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services). However, this is optional and not required for the demo to work.


## Learning Material

* [Deep Learning For Computer Vision](https://web.eecs.umich.edu/~justincj/teaching/eecs498/WI2022/) very similar to CS231n; pytorch assignments in Google Colab
* [Building Cloud Computing Solutions at Scale](https://www.coursera.org/specializations/building-cloud-computing-solutions-at-scale) inspiration for this repo
* [AWS Technical Essentials](https://www.coursera.org/learn/aws-cloud-technical-essentials)
* [Introduction to Machine Learning in Production](https://www.coursera.org/learn/introduction-to-machine-learning-in-production)
