import os
import cv2

# Path to the directory containing images
image_folder_path = '/Users/User/PycharmProjects/readimage/cows_3'

# List all files in the directory
files = os.listdir(image_folder_path)

# Iterate over all files in the directory
for file in files:
    # Construct the full file path
    file_path = os.path.join(image_folder_path, file)

    # Check if the file is an image (you can add more image extensions if needed)
    if file_path.endswith('.jpg') or file_path.endswith('.jpeg') or file_path.endswith('.png'):
        # Open and read the image
        img = cv2.imread(file_path)
        if img is not None:
            # Do something with the image
            cv2.imshow('Image', img)  # This will display the image
            cv2.waitKey(0)  # Wait for a key press to close the window
            cv2.destroyAllWindows()  # Close the window
            # cv2.imwrite('new_path', img)  # To save the image to a new path