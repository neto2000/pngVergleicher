import tkinter as tk
from PIL import Image



root = tk.Tk()

#get screensize
screensizeY = root.winfo_screenheight()

screensizeX = root.winfo_screenwidth()

#divide screensize by 2
minScreenSizeY = int(screensizeY/2)
minScreenSizeX = int(screensizeX/2)

#set minimal screensize
root.minsize(minScreenSizeX, minScreenSizeY)

#the two pictures
picture1 = "D:/Dateien/GitHub/pngVergleicher/test1.png"

picture2 = "D:/Dateien/GitHub/pngVergleicher/test2.png"


#convert a png file to an array
def Convert_PNG_file(file_location):
    start_image = Image.open(file_location, "r")

    #get the size of the picture
    start_image_width = start_image.size[0]
    start_image_height = start_image.size[1]

    #set the list for the pixel colors
    pixel_list = [[0] * start_image_height for i in range(start_image_width)]

    #write the list with the colors of the pixels
    for y in range(0, start_image_height):
        for x in range(0, start_image_width):

            really = x ,y

            pixel_list[y][x] = start_image.getpixel((x, y))

    return pixel_list


#schaut ob das bild im anderem exestiert
def Compare_Pics_11(pic1, pic2):
    print("hello!")


pic1_pixels = Convert_PNG_file(picture1)

pic2_pixels = Convert_PNG_file(picture2)

print(pic1_pixels)
print(pic2_pixels)


root.mainloop()