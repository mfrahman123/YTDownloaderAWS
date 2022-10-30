# Set base image (host OS)
FROM python:3.8-alpine

# By default, listen on port 5000
EXPOSE 5000/tcp

RUN mkdir -p /app

COPY static /app/static
COPY templates /app/templates
COPY app.py /app
COPY requirements.txt /app

# Set the working directory in the container
WORKDIR /app


# Install any dependencies
RUN pip install -r requirements.txt

ENV IN_DOCKER_CONTAINER Yes


# Copy the content of the local src directory to the working directory


# Specify the command to run on container start
CMD [ "python", "./app.py" ]