import tkinter as tk
from PIL import Image

#counts how often pic2 appears in pic1
counter_of_true_figures = 0

#UI Farbe: c3c3c3ff

root = tk.Tk()

#get screensize
screensizeY = root.winfo_screenheight()

screensizeX = root.winfo_screenwidth()

#divide screensize by 2
minScreenSizeY = int(screensizeY/2)
minScreenSizeX = int(screensizeX/2)

#set minimal screensize
root.minsize(minScreenSizeX, minScreenSizeY)

root.configure(background="white")

root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.grid_rowconfigure(0, weight=0)

input1 = tk.Entry(root, bg="#ffffff", highlightbackground="#e0e0e0")
input2 = tk.Entry(root, bg="#ffffff", highlightbackground="#e0e0e0")

#

#the two pictures
picture1 = "D:/Dateien/GitHub/pngVergleicher/test1.png"

picture2 = "D:/Dateien/GitHub/pngVergleicher/test4.png"



#convert a png file to an array
def Convert_PNG_file(file_location):
    start_image = Image.open(file_location, "r")

    #get the size of the picture
    print(start_image.size[0])
    print(start_image.size[1])

    


    start_image_width = start_image.size[0]
    start_image_height = start_image.size[1]

    #set the list for the pixel colors
    pixel_list = [[0] * start_image_width for i in range(start_image_height)]


    #write the list with the colors of the pixels
    for y in range(0, start_image_height):
        for x in range(0, start_image_width):

            really = x ,y

            pixel_list[y][x] = start_image.getpixel((x, y))

    return pixel_list


#schaut ob das bild im anderem exestiert
def Compare_Pics_11(picture1, picture2):

    global counter_of_true_figures

    #get the pixels
    pic1_pixels = Convert_PNG_file(picture1)
    pic2_pixels = Convert_PNG_file(picture2)



    all_pixels_pic1 = len(pic1_pixels) * len(pic1_pixels[0])
    all_pixels_pic2 = len(pic2_pixels) * len(pic2_pixels[0])


    counter_x_pic1 = 0
    counter_y_pic1 = 0

    counter_x_pic2 = 0
    counter_y_pic2 = 0

    


    print(all_pixels_pic1)

    print(pic2_pixels)
    print(pic1_pixels)

    for i in range(0, all_pixels_pic1):
        
        #print(counter_y_pic1, counter_x_pic1, counter_y_pic2, counter_x_pic2)

        print("for schleife")

        if pic1_pixels[counter_y_pic1][counter_x_pic1] == pic2_pixels[0][0]:
            
            nd_counter_x_pic1 = counter_x_pic1
            nd_counter_y_pic1 = counter_y_pic1

            print("erste übereinstimmung")

            counter_x_pic2 = 0
            counter_y_pic2 = 0


            for j in range(0, all_pixels_pic2):

                
                print("for in dem 2. Bild")

               
                


                if pic1_pixels[nd_counter_y_pic1][nd_counter_x_pic1] == pic2_pixels[counter_y_pic2][counter_x_pic2]:
                    
                    counter_x_pic2 += 1

                    nd_counter_x_pic1 += 1

                    print("abfrage ob die anderen pixel richtig sind")
                    print(counter_x_pic2)

                    if counter_x_pic2 == len(pic2_pixels[0]):
                        counter_y_pic2 += 1
                        counter_x_pic2 = 0

                        print("zeilen umbruch")

                        nd_counter_x_pic1 = nd_counter_x_pic1 - len(pic2_pixels[0])
                        nd_counter_y_pic1 += 1

                        
                        #if nd_counter_y_pic1 == len(pic1_pixels):
                            #print("abfrage ob das 1. bild zu klein ist")

                            #break
                        
                   
                    
                    if counter_y_pic2 == len(pic2_pixels):
                        print("GLEICH 100")

                        counter_of_true_figures += 1

                        print(counter_of_true_figures)

                        counter_x_pic2 = 0
                        counter_y_pic2 = 0

                        nd_counter_x_pic1 = 0
                        nd_counter_y_pic1 = 0
                        

                    if nd_counter_y_pic1 == len(pic1_pixels):
                        print("abfrage ob das 1. bild zu klein ist")

                        break


                    if nd_counter_x_pic1 == len(pic1_pixels[0]):
                        print("abfrage ob das 1. bild zu klein ist X")
                        break

                    

        


         
        if counter_x_pic1 == len(pic1_pixels[0]) - 1:
            counter_y_pic1 += 1

            counter_x_pic1 = -1

        """if counter_x_pic2 == len(pic2_pixels[0]):
            counter_y_pic2 += 1

            counter_x_pic2 = 0

            counter_x_pic1 = counter_x_pic1 - len(pic2_pixels[0])
            counter_y_pic1 += 1"""


        """if counter_y_pic2 == len(pic2_pixels):
            print("100% gleich")

            counter_x_pic2 = 0
            counter_y_pic2 = 0"""


            

        counter_x_pic1 += 1

    # true_count = tk.Label(root, text = counter_of_true_figures)

    # counter_of_true_figures = 0

    # true_count.pack()





b1 = tk.Button(root, text = "pruefen", fg = "#000000", bg="#ffffff", activebackground="#e0e0e0", activeforeground="#000000", highlightbackground="#ffffff", command = lambda: Compare_Pics_11(input1.get(), input2.get()))

settings_image = tk.PhotoImage(file = "~/Documents/Scripts/GitHub/pngVergleicher/UI_pictures/settings.png")




settings = tk.Button(root, image = settings_image, fg = "#000000", bg="#ffffff", activebackground="#e0e0e0", activeforeground="#000000", highlightbackground="#ffffff", width = 20, height = 20) 

#Compare_Pics_11(picture1, picture2)

#print(pic1_pixels)
#print(pic2_pixels)

print("ergeb")

input1.grid(column = 1, row = 0, sticky = tk.W+tk.E)
input2.grid(column = 2, row = 0, sticky = tk.W+tk.E)
b1.grid(column = 1, row = 1, columnspan = 2, sticky = tk.W+tk.E)
settings.grid(column = 0, row = 0)

#true_count.pack()







root.mainloop()
