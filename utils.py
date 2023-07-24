import openai
import base64
import os
from PIL import Image
import imghdr
import requests

def get_dimensions_from_size(size):
    dim = "256x256" 
    if size.upper() == "L":
        dim = "1024x1024" 
    elif size.upper() == "M":
        dim = "512x512" 
    return dim

def get_image(prompt,filename,size,image_dir):

    dimension = get_dimensions_from_size(size)
    
    # Get images
    try:
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
    
        print(f"\nImages generated!\n")

    except Exception as e:
        print(f"An error ocurred: {e}")

def convert_to_png(img):
    img_type = imghdr.what(img)

    if img_type != 'png':
        im = Image.open(img)
        im.save('tmp.png')
        return True
    
    return False

def get_image_variation(file,size,image_dir):

    file_path = os.path.join(image_dir,f"changed.png")

    converted = convert_to_png(file)
    file_to_change = 'tmp.png' if converted else file
    print(f"Using...{file_to_change}")

    dimension = get_dimensions_from_size(size)

    # Get images
    response = openai.Image.create_variation(
                    image=open(file_to_change,"rb"),
                    n=3,
                    size=dimension
                )
    urls = response.data

    for i,url in enumerate(urls):
        img_url = url['url']
        img_content = requests.get(img_url)
        img_content = img_content.content

        new_filename = f"{file_path}-{i+1}.png" 
        with open(new_filename,"wb") as changed_file:
            changed_file.write(img_content)

    # Cleanup any tmp files made
    try:
        os.remove("tmp.png")
    except OSError:
        pass


    print("\nDone!\n")