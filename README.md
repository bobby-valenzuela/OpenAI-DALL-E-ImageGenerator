# OpenAI-DALL-E-ImageGenerator

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   cd OpenAI-DALL-E-ImageGenerator
   ```

4. Create a new virtual environment:

   ```bash
   python3 -m venv env && . env/bin/activate
   ```

5. Install the requirements:

   ```bash
   pip3 install -r requirements.txt
   ```

6. Create a .env file with your OpenAI api key

   ```bash
   echo "OPENAI_API_KEY={api_secret}" > .env 
   ```

<br />


## Create 3 new images based of of some provided text
Enter a prompt DALL-E can use to generate an image and three images will be generated based on the size of your choosing.

<br />

```bash
python3 img_generator.py
```

<br />

## Generate 3 variations of a provided image:
Provide the path to an image as an argument to the program and this program will use the DALL-E API to generate 3 variations of that image.
The DALL-E API requires images to be square, no larger than 4MB, and must be a PNG. I've added a bit in the script that will convert images to a png image if they aren't already.

<br />

Format:
```bash
python3 img_changer.py <img_path>
```

Example:  
```bash
python3 img_changer.py ./images/superman.png
```
