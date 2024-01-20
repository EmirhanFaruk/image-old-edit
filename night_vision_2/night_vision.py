
# Modification date: Wed Jan  5 00:04:40 2022

# Production date: Sun Sep  3 15:43:46 2023

from PIL import Image
from random import choice
from random import randint
from random import *
import random

img_list = ["Sc1.png", "Sc2.png", "Sc3.png", "Sc4.png", "Sc5.png"]

dissortion_list = ["bright", "dark"]
for i in range(18):
	dissortion_list.append("normal")


for i in range(len(img_list)):
	image = Image.open(img_list[i])
	
	width, height = image.size
	
	for w in range(width):
		for h in range(height):
			rgb = image.getpixel((w, h))
			da_choice = random.choice(dissortion_list)
			if da_choice == "normal":
				rgb2 = (0, rgb[1], 0)
				image.putpixel((w, h), rgb2)
			elif da_choice == "dark":
				if rgb[1] - 40 <= 0:
					green = random.randint(0, rgb[1])
				else:
					green = random.randint(rgb[1] - 40, rgb[1])
				rgb2 = (0, green, 0)
				image.putpixel((w, h), rgb2)
			elif da_choice == "bright":
				if rgb[1] + 40 >= 255:
					green = random.randint(rgb[1], 255)
				else:
					green = random.randint(rgb[1], rgb[1] + 40)
				rgb2 = (0, green, 0)
				image.putpixel((w, h), rgb2)
	
	
	image.save(f"Sc{i + 1}_edit.png", "png")
	print(f"Image {img_list[i]} is saved as Sc{i + 1}_edit.png")

print("All done!")