import tkinter as tk
import random as rnd


def sigmoid(i):
    

    e = 2.718281

    one = 1 / (1+ (e**-i))

    two = 1 + one

    three = 1 / two

    return three

def sigmoid_ableitung(i):

    one = 1 - sigmoid(i)

    two = sigmoid(i) * one


    return two



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

    def change_bias(self, bias):

        self.bias = bias



root = tk.Tk()


buttons = []
counter = []

def start_neuronal_network(start_value, neuron_count, layers, expected_number):

    print(start_value)

    print(expected_number)

    neurons = []

    input_value = start_value

    for i in range(layers):

        temp_value = []

        neurons.append([])

        for j in range(neuron_count):

            neurons[i].append(Neuron(input_value)) 

            

            temp_value.append(neurons[i][j].output())

            

        print(temp_value)

        input_value = temp_value

        



    #calculate cost

    expected_output_list = []

    for i in range(10):
        expected_output_list.append(0)

        if i == expected_number:
            expected_output_list[i] = 1

    finish_layer = []

    cost = 0

    for i in range(10):
        finish_layer.append(Neuron(input_value))

        output = finish_layer[i].output()

        print(output)

        add_cost = (output - expected_output_list[i]) ** 2

        cost = cost + add_cost


    print("cost: " + str(cost))







      

    


    
    print(neurons[0][0].weight)
    
    

    


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
