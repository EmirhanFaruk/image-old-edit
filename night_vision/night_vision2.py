
# Modification date: Wed Jan  5 00:01:02 2022

# Production date: Sun Sep  3 15:43:46 2023

from PIL import Image
import random
import math

img_list = ["Sc1.png", "Sc2.png", "Sc3.png", "Sc4.png", "Sc5.png"]

dissortion_list = ["bright", "dark"]
for i in range(18):
	dissortion_list.append("normal")


for i in range(len(img_list)):
	image = Image.open(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit\\night_vision\\night_vision\\{img_list[i]}")
	
	width, height = image.size
	
	for w in range(width):
		for h in range(height):
			rgb = image.getpixel((w, h))
			rgbs = rgb[0] + rgb[1] + rgb[2]
			da_choice = random.choice(dissortion_list)
			origin_x = width // 2
			origin_y = height // 2
			curr_x = w - origin_x
			curr_y = h - origin_y


			radius = width // 9
			point_distance = math.sqrt((abs(curr_x)**2) + (abs(curr_y)**2))
			probability_circle = [False]
			for j in range(4):
				probability_circle.append(True)
				continue
			if point_distance <= radius:
				if random.choice(probability_circle):
					dans_le_cercle = True
				else:
					dans_le_cercle = False
			else:
				dans_le_cercle = False
			


			if point_distance < radius + 3 and not dans_le_cercle:
					if 2 == random.randint(1, 3):
						dans_le_cercle = True
			if point_distance < radius + 5 and not dans_le_cercle:
				if 2 == random.randint(1, 4):
					dans_le_cercle = True
			if point_distance < radius + 7 and not dans_le_cercle:
				if 2 == random.randint(1, 5):
					dans_le_cercle = True
			if point_distance < radius + 9 and not dans_le_cercle:
				if 2 == random.randint(1, 6):
					dans_le_cercle = True

			if point_distance < radius + 11 and not dans_le_cercle:
				if 2 == random.randint(1, 7):
					dans_le_cercle = True

			if point_distance < radius + 13 and not dans_le_cercle:
				if 2 == random.randint(1, 8):
					dans_le_cercle = True



			radius_petit = width // 10
			point_distance_petit = math.sqrt((abs(curr_x)**2) + (abs(curr_y)**2))
			#dans_le_petit_cercle = radius_petit >= point_distance_petit
			if point_distance_petit > radius_petit:
				dans_le_petit_cercle = False
			else:
				dans_le_petit_cercle = True
			
			#print(f"{w}, {h}  dans_le_petit_cercle = {dans_le_petit_cercle}, dans_le_cercle = {dans_le_cercle}")

			green = rgb[1]
			
			if dans_le_petit_cercle:   #w > width//3 and w < (width//3)*2 and h > height//3 and h < (height//3)*2:
				if da_choice == "normal":
					rgb2 = (0, rgbs, 0)
					image.putpixel((w, h), rgb2)
				elif da_choice == "dark":
					if rgbs - 40 <= 0:
						green = random.randint(0, rgbs)
					else:
						green = random.randint(rgbs - 40, rgbs)
					rgb2 = (0, green, 0)
					image.putpixel((w, h), rgb2)
				elif da_choice == "bright":
					if rgbs >= 255:
						rgbs = 255
					elif rgbs + 40 >= 255:
						green = random.randint(rgbs, 255)
					else:
						green = random.randint(rgbs, rgbs + 40)
					rgb2 = (0, green, 0)
					image.putpixel((w, h), rgb2)
			elif dans_le_cercle:
				if da_choice == "normal":
					rgb2 = (0, rgbs, 0)
					image.putpixel((w, h), rgb2)
				elif da_choice == "dark":
					if rgbs - 40 <= 0:
						green = random.randint(0, rgbs)
					else:
						green = random.randint(rgbs - 40, rgbs)
					rgb2 = (0, green, 0)
					image.putpixel((w, h), rgb2)
				elif da_choice == "bright":
					if rgbs >= 255:
						rgbs = 255
					elif rgbs + 40 >= 255:
						green = random.randint(rgbs, 255)
					else:
						green = random.randint(rgbs, rgbs + 40)
					rgb2 = (0, green, 0)
					image.putpixel((w, h), rgb2)
			else:
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
					if green >= 255:
						green = 255
					elif rgb[1] + 40 >= 255:
						green = random.randint(rgb[1], 255)
					else:
						green = random.randint(rgb[1], rgb[1] + 40)
					rgb2 = (0, green, 0)
					image.putpixel((w, h), rgb2)
	
	image.save(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit\\night_vision\\night_vision\\Sc{i + 1}_edit3.png", "png")
	print(f"Image {img_list[i]} is saved as Sc{i + 1}_edit3.png")

print("All done!")