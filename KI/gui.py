import tkinter as tk
from neuronal_test import start_neuronal_network


root = tk.Tk()


buttons = []
counter = []

colors = {0:"#000000",0.1:"#1A1A1A",0.2:"#343434",0.3:"#4E4E4E",0.4:"#686868",0.5:"#828282",0.6:"#9C9C9C",0.7:"#B6B6B6",0.8:"#D0D0D0",0.9:"#FFFFFF"}

#draw digit

def change_color_ten(i):

    counter[i] = round(counter[i] + 0.1, 1)


    if counter[i] == 1:

        counter[i] = 0


    print(counter[i])

    buttons[i].configure(bg=colors[counter[i]])

def change_color(i):

    if counter[i] == 0:
        buttons[i].configure(bg="white") 

        counter[i] = 1

        print("on" + str(i))

    elif counter[i] == 1:
        buttons[i].configure(bg="black") 

        counter[i] = 0

        print("off" + str(i))



x = -10

y = 10

for i in range(256):
    
    counter.append(0)
    buttons.append(tk.Button(root, command=lambda i=i: change_color_ten(i))) 

    


    x += 20

    if x >= 330:

        y += 20

        x = 10

    buttons[i].place(x=x, y=y, width=20, height = 20)

    buttons[i].configure(bg="black")


expec_number_field = tk.Entry(root)

expec_number_field.pack()


start_button = tk.Button(root, text="Start", command=lambda: start_neuronal_network(counter, 8, 2, int(expec_number_field.get())))

start_button.pack()





root.mainloop()