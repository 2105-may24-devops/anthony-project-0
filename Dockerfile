# Standard dockerfile, to take a python project and make an image using requirements, pip, and venv.

# The base for the image. Can use python:3, and docker will grab the newest stable release.
FROM python:3.9

# Hop into this directory, to keep things in on place in the image?.
WORKDIR /app

# Put requirements into the image.
COPY requirements.txt .

# Set up a python virtual environment.
RUN python3 -m venv venv

# Install requirements.
RUN venv/bin/python3 -m pip install -r requirements.txt

# Copy the the cwd into the image cwd.
COPY . .

# This is the metadata for how to run/create your container.
CMD ["venv/bin/python3", "data_zero.py"]