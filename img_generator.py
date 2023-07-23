#!/usr/bin/python3

import openai
from dotenv import dotenv_values
import json
import os
import base64

# Read API key from .env file
config = dotenv_values('.env');
openai.api_key = config["OPENAI_API_KEY"]

# Where to saved images
image_dir_name = "images"
image_dir = os.path.join(os.curdir,image_dir_name)

# Make dir if necessary
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

# FUNCS
def get_dimensions_from_size(size):
    dim = "256x256" 
    if size.upper() == "L":
        dim = "256x256" 
    elif size.upper() == "M":
        dim = "512x512" 
    return dim

def get_image(prompt,filename,size):

    dimension = get_dimensions_from_size(size)
    
    # Get images
    response = openai.Image.create(
                    prompt=prompt,
                    n=3,
                    size=dimension,
                    response_format="b64_json"
                )
    imgs = response.data
    # Note if you did not include response_format the default response would be to return a url which you can reference from response.data[index]['url']

    # Save images
    for idx,img in enumerate(imgs):
        file_path = os.path.join(image_dir,f"{filename}-{idx+1}.png")

        with open(file_path,"wb") as file:
            img_decoded = base64.b64decode(img['b64_json']) 
            file.write(img_decoded)


### MAIN PROGRAM ###

input_text = input("Enter a prompt to find your images: ")
filename = input("Enter a name for your files: ")
size = input("Enter a size for your files (S,M,L): ")
get_image(input_text,filename,size)
