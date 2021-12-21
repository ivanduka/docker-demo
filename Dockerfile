# Base image
FROM python:3.10.1-bullseye

# Set the working directory INSIDE of the linux machine
WORKDIR /usr/src/app

# Install Ghostscript
RUN apt update && apt install ghostscript python3-tk ffmpeg libsm6 libxext6 -y

# Install the dependencies
COPY requirements.txt ./
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copy all file from the current folder to the working folder in linux machine
COPY . .

# The command to run when the container starts
CMD [ "python3", "./main.py" ]
