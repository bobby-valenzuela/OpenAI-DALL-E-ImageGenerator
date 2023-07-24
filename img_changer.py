#!/usr/bin/python3

from dotenv import dotenv_values
import os,sys
from utils import *

# Read API key from .env file
config = dotenv_values('.env');
openai.api_key = config["OPENAI_API_KEY"]

# Verify file passed in
img_path = ""

if len(sys.argv) == 1:
    img_path = input("Enter the path of your image: ")
else:
    img_path = sys.argv[1]


# Verify file exists
if not os.path.isfile(img_path):
    print(img_path)
    print("File not found. Exiting.")
    exit()

# Where to saved images
image_dir_name = "changed_images"
image_dir = os.path.join(os.curdir,image_dir_name)

# Make dir if necessary
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)


size = input("Enter a size for your changed file (S,M,L): ")
get_image_variation(img_path,size,image_dir)
