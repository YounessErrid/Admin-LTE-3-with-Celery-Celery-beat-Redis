# Setup Server
# start with a base python image chosen from [dockerhub] https://hub.docker.com/_/python/
FROM python:3.11-slim-bullseye

# show python logs as they occur
ENV PYTHONUNBUFFERED=1

# set the working directory or project root folder to /code
WORKDIR /app

# copy the requirements file to the working directory /code
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the project code to the working directory /code
COPY . .