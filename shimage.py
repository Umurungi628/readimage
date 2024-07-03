import os
import json
from PIL import Image


def load_json(json_file_path):
    """
    Load JSON file and return the data.
    """
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    return data


def display_images(image_list):
    """
    Display images given a list of image paths.
    """
    for image_info in image_list:
        print(image_info)  # Debug print to check the structure of each image info

        # Extract the image path from the dictionary
        image_path = image_info.get('path')

        if image_path:
            # Check if the file exists
            if os.path.exists(image_path):
                # Open and read the image
                img = Image.open(image_path)
                # Display the image
                img.show()
            else:
                print(f"Image not found: {image_path}")
        else:
            print("No 'path' key found in:", image_info)


if __name__ == "__main__":
    # Path to the JSON file
    json_file_path ='/Users/User/PycharmProjects/readimage/instances_default.json'

    # Load the JSON file
    data = load_json(json_file_path)

    # Display the images
    if 'images' in data:
        display_images(data['images'])
    else:
        print("No 'images' key found in the JSON file")