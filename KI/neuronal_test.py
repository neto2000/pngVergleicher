import tkinter as tk
import random as rnd


def sigmoid(i):
    

    e = 2.718281

    one = e**-i

    two = 1 + one

    three = 1 / two

    return three

class Neuron:
    def __init__(self, value):

        self.input = value

        

        

        self.weight = []

        for i in range(len(self.input)):

            self.weight.append(rnd.randint(-10 , 10))

        self.bias = 0

    
    def output(self):

        if len(self.input) == len(self.weight):

            temp_list = []

            ergebnis = 0

            for i in range(len(self.input)):

                temp_list.append(self.input[i] * self.weight[i])

            for i in range(len(temp_list)):

                ergebnis = ergebnis + temp_list[i]

            ergebnis = ergebnis - self.bias

            sig_ergebnis = sigmoid(ergebnis)

            return  sig_ergebnis

        else:

            print("invalid weight")

    def change_weight(self, weight):

        self.weight = weight

    def change_weight(self, bias):

        self.bias = bias



root = tk.Tk()


buttons = []
counter = []

def start_neuronal_network(start_value, neuron_count, layers):

    print(start_value)

    neurons = []

    input_value = start_value

    for i in range(layers):

        neurons.append([])

        for j in range(neuron_count):

            neurons[i].append(Neuron(input_value)) 

            temp_value = []

            temp_value.append(neurons[i][j].output())

        input_value = temp_value

    finish_layer = []

    for i in range(10):
        finish_layer.append(Neuron(input_value))

        print(finish_layer[i].output())

        
        
    print(neurons[0][0].weight)
    
    

    




def change_color(i):

    if counter[i] == 0:
        buttons[i].configure(bg="white") 

        counter[i] = 1

        print("on" + str(i))

    elif counter[i] == 1:
        buttons[i].configure(bg="black") 

        counter[i] = 0

        print("of" + str(i))



x = -90

y = 10

for i in range(64):
    
    counter.append(0)
    buttons.append(tk.Button(root, command=lambda i=i: change_color(i))) 

    


    x += 100

    if x >= 810:

        y += 100

        x = 10

    buttons[i].place(x=x, y=y, width=100, height = 100)

    buttons[i].configure(bg="black")


start_button = tk.Button(root, text="Start", command=lambda: start_neuronal_network(counter, 8, 2))

start_button.pack()





root.mainloop()
