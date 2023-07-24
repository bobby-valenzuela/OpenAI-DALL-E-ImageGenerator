#!/usr/bin/python3

from dotenv import dotenv_values
import os
from utils import *

# Read API key from .env file
config = dotenv_values('.env');
openai.api_key = config["OPENAI_API_KEY"]

# Where to saved images
image_dir_name = "images"
image_dir = os.path.join(os.curdir,image_dir_name)

# Make dir if necessary
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

input_text = input("Enter a prompt to find your images: ")
filename = input("Enter a name for your files: ")
size = input("Enter a size for your files (S,M,L): ")
get_image(input_text,filename,size,image_dir)
