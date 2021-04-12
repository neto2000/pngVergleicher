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


#convert a png file to an array
def Convert_PNG_file(file_location):
    start_image = Image.open(file_location, "r")

    start_image_width = start_image.size[0]
    start_image_height = start_image.size[1]

    pixel_list = [[0] * start_image_height for i in range(start_image_width)]

    print(pixel_list)

    for y in range(0, start_image_height):
        for x in range(0, start_image_width):

            really = x ,y

            pixel_list[y][x] = start_image.getpixel((x, y))

    


    return pixel_list

test_array = Convert_PNG_file("D:/Dateien/GitHub/pngVergleicher/test.png")

print(test_array)


root.mainloop()