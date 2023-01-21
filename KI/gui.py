import tkinter as tk
from neuronal_test import start_neuronal_network


root = tk.Tk()


buttons = []
counter = []

#draw digit

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
    buttons.append(tk.Button(root, command=lambda i=i: change_color(i))) 

    


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