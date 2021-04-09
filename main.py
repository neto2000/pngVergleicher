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
    start_image = Image.open(file_location)

    start_image_width = start_image.size[0]
    start_image_height = start_image.size[1]

    pixel_list = [[]] * start_image_width

    for x in range(0, start_image_width):
        for y in range(0, start_image_height):

            pixel_list[start_image_width, start_image_height] = start_image.getpixel(x,y )


    return pixel_list

test_array = Convert_PNG_file("test.png")

print(test_array)


root.mainloop()