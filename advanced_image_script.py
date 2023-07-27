from PIL import Image
import os
import random

# Set the directory paths to the textures/block folder in Minecraft
directory_paths = r'C:\Users\Campbell\AppData\Roaming\.minecraft\resoursepacks\MasonTroyAdams\assets\minecraft\textures\block',
                   
# Set the image paths to the five different images
image_paths =  r'C:\Users\Campbell\Downloads\the simpsons\pngs\masontroyadams.png'

# Loop through each directory
for directory_path in directory_paths:

    # Get the first image in the directory
    first_image = None
    for filename in os.listdir(directory_path):
        random_int = random.randint(0, 5)
        if filename.endswith('.png'):
            first_image = Image.open(os.path.join(directory_path, image_paths))
            break

    if not first_image.mode.endswith('a'):
        first_image = first_image.convert('RGBA')

    # Loop through each file in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.png'):
            # Select a random image from the image paths
            first_image_path = os.path.join(directory_path, image_paths)
            first_image = Image.open(first_image_path)

            if not first_image.mode.endswith('a'):
                first_image = first_image.convert('RGBA')

            # Select a random image from the image paths
            image_path = random.choice(image_paths)
            image = Image.open(image_path)

            if image.mode != first_image.mode:
                image = image.convert(first_image.mode)
            if not image.mode.endswith('A'):
                alpha = Image.new('L', image.size, 512)
                image.putalpha(alpha)
            image = image.resize(first_image.size)
            image.paste(first_image, (0, 0), first_image)
            image.save(os.path.join(directory_path, filename))
