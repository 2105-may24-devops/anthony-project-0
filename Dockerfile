
#Isolated processes
# Create container image, aka Docker Image
# Containers are ephemeral (created and destroyed as needed)
# images are immutable: templates used to make new containers.
# To create an image, you build a Dockerfile: Recipes to build an image layer by layer.
# Docker Host follows the Dockerfile's instruction.
# Instructions are executed in containers of their own.

# You get images from docker registries. Default is docker hub. docker.io
# Two things we want from a base images.
    # 1. As much of the dependencies of our app as possible.
    # 2. Officially supported/well maintained with updates
# Instead of using multiple run commands, use '&&' to separate RUN statements to create a singe layer for similar tasks.
# Less layers are generally more performant.

# If I use 3, it will use the image that is the newest. However if I specific 3.9, it will only use 3.9 image.


FROM python:3.9

WORKDIR /app

# COPY requirements.txt /app
COPY requirements.txt .

#set up virtual environment
RUN python3 -m venv venv

#install requirements
RUN venv/bin/python3 -m pip install -r requirements.txt

COPY . .

# THIS is just metadata on the image - what command will execute to start each container.
CMD ["venv/bin/python3", "data_zero.py"]
# can override the CMD with asecond argument to docker un

#make sure to include a .dockerignore to ignore things that might change. Take advantage of the build cache to optimize docker file.
# Or change the order.
