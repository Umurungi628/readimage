import os
import json
from PIL import Image

# Path to the JSON file
json_file_path = '/Users/User/PycharmProjects/readimage/instances_default.json'

# Load the JSON file
with open(json_file_path, 'r') as f:
    data = json.load(f)

# Iterate over all image paths in the JSON file
for image_info in data['images']:
    # Extract the image path from the dictionary
    image_path = image_info['path']

    # Check if the file exists
    if os.path.exists(image_path):
        # Open and read the image
        img = Image.open(image_path)
        # Display the image
        img.show()
    else:
        print(f"Image not found: {image_path}")