FROM public.ecr.aws/lambda/python:3.8
# the following works as well but results in larger image
#FROM python:3


RUN mkdir -p /app
COPY . main.py /app/
WORKDIR /app
RUN pip install --upgrade pip &&\
		pip install -r requirements.txt
EXPOSE 8080
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]
 
 
 
 
 