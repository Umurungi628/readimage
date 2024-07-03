
#'/Users/User/PycharmProjects/readimage/instances_default.json'
import os
import json
from PIL import Image  # or use `import cv2`

# Path to the JSON file
json_file_path = '/Users/User/PycharmProjects/readimage/instances_default.json'

# Load the JSON file
with open(json_file_path, 'r') as f:
    data = json.load(f)

# Debug print to check the structure of the JSON data
print(data)

# Iterate over all image paths in the JSON file
for image_info in data['images']:
    print(image_info)  # Print the individual image info to check its structure

    # Extract the image path from the dictionary
    if 'path' in image_info:
        image_path = image_info['path']

        # Check if the file exists
        if os.path.exists(image_path):
            # Open and read the image
            with Image.open(image_path) as img:
                # Do something with the image
                img.show()  # This will display the image
                # img.save('new_path')  # To save the image to a new path
        else:
            print(f"Image not found: {image_path}")
    else:
        print(f"Key 'path' not found in: {image_info}")