import random
from PIL import Image
import os

shadow_scripts = ['#MURDERGANG', '#GOBLINHACKERSOCIETY', '#SCRIPTWIZARDSINC', '#BLOODMOON', '#WEKILLEDTHEANCIENTGODS']
print('PROPERTY OF EVIL SHADOW SCRIPTS >:) {random.choice(shadow_scripts}')

# specify the path of the folder containing the PNG files to be replaced
folder_path = r'C:\Users\Campbell\AppData\Roaming\.minecraft\resourcepacks\emilio\assets\minecraft\textures\block'

# specify the path of the new image that will replace the PNG files
new_image_path = r'C:\Users\Campbell\Downloads\emilio2.png'
print('GOT PATHS {random.choice(shadow_scripts)}')
try:
    # open the new image and get its dimensions
    new_image = Image.open(new_image_path)
    new_width, new_height = new_image.size
except IOError as e:
    print(f"Error: {e}")
    exit()

# loop through each file in the folder
for filename in os.listdir(folder_path):
    # check if the file is a PNG file
    if filename.endswith('.png'):
        try:
            # open the PNG file and get its dimensions
            png_path = os.path.join(folder_path, filename)
            png_image = Image.open(png_path)
            png_width, png_height = png_image.size

            print('{filename} {random.choice(shadow_scripts)}')
            # calculate the new dimensions based on the aspect ratio of the PNG file
            if png_width > png_height:
                new_height = int((png_height/png_width)*new_width)
            else:
                new_width = int((png_width/png_height)*new_height)

            # resize the new image to the calculated dimensions and save it as the PNG file
            new_image_resized = new_image.resize((new_width, new_height))
            new_image_resized.save(png_path)
        except IOError as e:
            print(f"Error processing file {filename}: {e}")

print('EVIL SHADOW IMAGE SCRIPT COMPLETE')