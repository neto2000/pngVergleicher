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
def Compare_Pics_11(picture1, picture2):

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


    #not yet debuged!
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


Compare_Pics_11(picture1, picture2)

#print(pic1_pixels)
#print(pic2_pixels)


root.mainloop()