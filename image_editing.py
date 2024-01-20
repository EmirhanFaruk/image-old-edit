
# Modification date: Sat Oct 14 00:03:59 2023

# Production date: Sun Sep  3 15:43:45 2023

import os
from PIL import Image
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from clear_screen import clear#clear()
from datetime import datetime
import random



def paths():

    prefixes = str(input("Enter the prefix of the edited images: "))

    if prefixes == "" or prefixes == "conda activate imgedit":
        prefixes = "file_name_"
    else:
        prefixes = prefixes + "_"

    print(f"Using the prefix: {prefixes}")

    the_name_of_the_file = input("Enter the name of the source file: ")


    if the_name_of_the_file == "" or the_name_of_the_file == "conda activate imgedit":
        the_name_of_the_file = "\\sources\\images"
    else:
        the_name_of_the_file = "\\" + the_name_of_the_file

    print("Using the file: " + the_name_of_the_file[1:])
    #print(the_name_of_the_file.split("\\"))
    the_name_of_the_file2 = the_name_of_the_file.split("\\")[1]

    #\\the_edited_images
    the_destination_file = input("Enter the destination file: ")

    if the_destination_file == "" or the_destination_file == "conda activate imgedit":
        the_destination_file = "\\destinations\\the_edited_images"
    else:
        the_destination_file = "\\" + the_destination_file
    
    print("Using the destination file: " + the_destination_file[1:])

    print(f"\n\n\nUsing the prefix: {prefixes}\nUsing the file: {the_name_of_the_file[1:]}\nUsing the destination file: {the_destination_file[1:]}")
    the_answer = input("\nAre those paths good? (y for yes, put anything but y to reenter)\n: ")
    if the_answer == "y":  
        return the_name_of_the_file, the_destination_file, the_name_of_the_file2, prefixes
    else:
        clear()
        return paths()

the_name_of_the_file, the_destination_file, the_name_of_the_file2, prefixes = paths()


arr = os.listdir("C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit" + the_name_of_the_file)

larr = len(arr)
for i in range(larr):
    arr[i] = f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\Python\\image_old_edit{the_name_of_the_file}\\" + arr[i]

sussy_file_name = f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\Python\\image_old_edit{the_name_of_the_file}\\"
"""
for i in range(len(arr)):
        arr[i] = "C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\Python\\image_old_edit\\the_images\\" + arr[i]
        os.rename(arr[i], f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\Python\\image_old_edit\\the_images\\sc_{i + 1}.png")
"""

start_time = datetime.now()
start_time2 = time.time()
start_time3 = datetime.now()
start_time = [start_time.year, start_time.month, start_time.day, start_time.hour, start_time.minute, start_time.second]
#start_time[3] + start_time[4] + start_time[5] for h/m/s


# Loading bar. Returns the start of the time of the image as [hour, minute, second].
def load_bar(delta_time, start_time, photos_done, total_photos, arr, i):
    clear()
    print("Using the folder: " + the_name_of_the_file[1:])
    print(f"The loop started at {start_time[0]}/{start_time[1]}/{start_time[2]}, {start_time[3]}:{start_time[4]}:{start_time[5]}")
    print(f"Last image done in {delta_time[0]} hours, {delta_time[1]} minutes and {delta_time[2]} seconds.")
    print(f"Image {i + 1} of {total_photos}")
    print(f"The file: {str(arr[i]).split(sussy_file_name)[1]}")
    green_bars_num = int((((photos_done) / len(arr)) * 100))
    green_bars = " " * green_bars_num
    white_bars = " " * (100 - green_bars_num)
    print(Back.GREEN + green_bars + Back.RED + white_bars)
    the_image_time = datetime.now()
    the_image_time = [the_image_time.hour, the_image_time.minute, the_image_time.second]
    return the_image_time



line = []
with open("C:\\Users\\emirh\\Desktop\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit\\The_Try.txt", "r") as f:
    line = f.readlines()
f.close()
n_try = int(line[0])
with open("C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit\\The_Try.txt", "w") as f:
    line = f.write(str(n_try + 1))
f.close()


f = open(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit\\the_logs.txt", "a")
f.write(f"\n\n\n---------------------------------------------------------------------\n\n\nTry {n_try}, using the folder {the_name_of_the_file[1:]} started at {start_time[0]}/{start_time[1]}/{start_time[2]}, {start_time[3]}:{start_time[4]}:{start_time[5]}\n\n\n")
f.close()

now_for_imgs = datetime.now()
delta_time = [0, 0, 0]
photos_done = 0
total_photos = larr
#1/80
will_black_line = [True]
for i in range(149):
    will_black_line.append(False)
#certain_black_line = False
black_line1 = 0
black_line2 = 0
blw = 0
#1/10
will_disorted = [True]
for i in range(19):
    will_disorted.append(False)

for i in range(len(arr)):
    now_for_imgs = datetime.now()
    dt_string1 = now_for_imgs.strftime("%d/%m/%Y %H:%M:%S")
    image = Image.open(arr[i])
    width, height = image.size
    
    the_image_time = load_bar(delta_time, start_time, photos_done, total_photos, arr, i)
    for w in range(width):
        random_number = random.randint(0,500)
        if random_number == 20:#random.choice(will_black_line):
            w1 = True
            """
            blh1 = random.randint(0, height)
            blh2 = random.randint(0, height)
            
            if blh1 >= blh2:
                temp = blh1
                blh1 = blh2
                blh2 = temp
       
            blh1 = 0
            blh2 = 0
            """
        else:
            w1 = False
        #time things
        now_for_imgs2 = datetime.now()
        dt_string2 = now_for_imgs2.strftime("%d/%m/%Y %H:%M:%S")
        img_break_time = time.time()
        current_running_time = int(img_break_time - start_time2)
        #print(f"%{int(((w) / (width)) * 100)} | Current time: {dt_string2}, the program has been running for {current_running_time// 60} minutes {current_running_time - (current_running_time // 60 * 60)} seconds.    ", end = "\r")
        
        for h in range(height):
            if w1:
                image.putpixel((w, h), (0, 0, 0))
            else:
                rgb = image.getpixel((w, h))
                #print(f"w = {w}, h = {h}, %{int(((w) / (width)) * 100)} | Current time: {dt_string2}, the program has been running for {current_running_time// 60} minutes {current_running_time - (current_running_time // 60 * 60)} seconds.    ", end = "\r")
                #1/3 of the screen will be blurred
                if True: #w > width//3 and w < (width//3) * 2 or h > height//3 and h < (height//3) * 2:
                    the_gray_tone = (rgb[0] + rgb[1] + rgb[2]) * 2 // 5
                else:
                    """
                    if w < width//3:
                        the_w_ratio = w / width//3
                    elif w > (width//3) * 2:
                        the_w_ratio = (width//3) * 2 / w 
                    if h < height//3:
                        the_h_ratio = h / height//3
                    elif h > (height//3) * 2:
                        the_h_ratio = (height//3) * 2 / h
                    """
                    if w < width:
                        the_w_ratio = w / (width//2)
                    else:
                        the_w_ratio = (width//2) / w
                    if h < height:
                        the_h_ratio = h / (height//2)
                    else:
                        the_h_ratio = (height//2) / h
                    the_ratio = (the_h_ratio + the_w_ratio) / 2
                    #print(f"{(the_h_ratio + the_w_ratio)} / 2 = {the_ratio}")
                    the_gray_tone = int(((rgb[0] + rgb[1] + rgb[2]) * 2 // 5) * the_ratio)
                    #print(f"{((rgb[0] + rgb[1] + rgb[2]) * 2 // 5)} * {the_ratio} = {the_gray_tone}")
                if random.choice(will_disorted):
                    da_tone = random.randint(0,30)
                    liste = ["brighter", "darker"]
                    if random.choice(liste) == "brighter":
                        if the_gray_tone + 5 <= 255 and random.choice([True, False]):
                            rgb2 = (the_gray_tone + da_tone, the_gray_tone + da_tone, the_gray_tone * 2 // 5)
                        else:
                            da_tone = random.randint(0, abs(254 - the_gray_tone) + 1)
                            rgb2 = (the_gray_tone + da_tone, the_gray_tone + da_tone, the_gray_tone * 2 // 5)
                    elif random.choice(liste) == "darker":
                        if the_gray_tone - 5 >= 0:
                            rgb2 = (the_gray_tone - da_tone, the_gray_tone - da_tone, the_gray_tone * 2 // 5)
                        else:
                            da_tone = random.randint(0, the_gray_tone + 1)
                            rgb2 = (the_gray_tone - da_tone, the_gray_tone - da_tone, the_gray_tone * 2 // 5)
                    else:
                        rgb2 = (the_gray_tone, the_gray_tone, the_gray_tone * 2 // 5)
                else:
                    rgb2 = (the_gray_tone, the_gray_tone, the_gray_tone * 2 // 5)
                image.putpixel((w, h), rgb2)
    path = f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit{the_destination_file}\\{prefixes}{str(str(arr[i]).split(sussy_file_name)[1])[:-3]}%#05d" % (i+1) + ".png"
    image.save(path, "png")
    image.close()
    photos_done += 1
    
    the_image_time_end = datetime.now()
    the_image_time_end = [the_image_time_end.hour, the_image_time_end.minute, the_image_time_end.second]
    delta_time = [the_image_time_end[0] - the_image_time[0], the_image_time_end[1] - the_image_time[1], the_image_time_end[2] - the_image_time[2]]
    if delta_time[2] < 0:
        delta_time[2] = delta_time[2] + 60
        delta_time[1] -= 1
    if delta_time[1] < 0:
        delta_time[1] = delta_time[1] + 60
        delta_time[0] -= 1
    f = open(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit\\the_logs.txt", "a")
    f.write(f"\n\nImage {i + 1} ({str(arr[i]).split(sussy_file_name)[1]}) from the folder {the_name_of_the_file[1:]} has been done in {delta_time[0]} hours, {delta_time[1]} minutes and {delta_time[2]} seconds.")
    f.close()



finish = time.time()

total_time = finish - start_time2

now2 = datetime.now()
# dd/mm/YY H:M:S
dt_string = start_time3.strftime("%d/%m/%Y %H:%M:%S")
print("Started at ", dt_string)	
# dd/mm/YY H:M:S
dt_string = now2.strftime("%d/%m/%Y %H:%M:%S")


f = open(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit\\the_logs.txt", "a")

f.write(f"\n\n\nTry {n_try}, using the folder {the_name_of_the_file[1:]}, all done in {int(total_time)} seconds({int(total_time/60)} minutes and {int(total_time % 60)} seconds). The program ended at {dt_string}")

f.close()

print("Ended at ", dt_string)	
print(f"All done in {total_time}")
