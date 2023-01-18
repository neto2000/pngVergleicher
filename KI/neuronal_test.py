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

        self.activision = 0

        self.backpropagated_activisions = []

        self.backpropagated_weigths = []

        self.weight = []

        for i in range(len(self.input)):

            self.weight.append(rnd.randint(-10 , 10))
            self.backpropagated_weigths.append(0)


        self.bias = 0

    
    def output(self):

        if len(self.input) == len(self.weight):

            temp_list = []

            ergebnis = 0

            for i in range(len(self.input)):

                temp_list.append(self.input[i] * self.weight[i])

            for i in range(len(temp_list)):

                ergebnis = ergebnis + temp_list[i]

            ergebnis = ergebnis + self.bias

            sig_ergebnis = sigmoid(ergebnis)

            self.activision = sig_ergebnis

            return  sig_ergebnis

        else:

            print("invalid weight")

    def change_weight(self, position, value):

        self.weight[position] = value

    def change_bias(self, position, value):

        self.bias[position] = value





def backpropagation_of_weigth_OutLayer(output_neuron, weigth_pos, expected_output):

    # Ziel: den Einfluss eines weigths auf die cost FUnktion berechnen (Ableitung von der Cost Function mit dem Parameter w (das weigth))
    #
    # Kettenregel (alle zwischen funktionen die zu der ableitung der Cost Function führen auch ableiten und multiplizieren)
    # C = sum( (a_j - y_j)^2 ), j = 1 to n       # j ist die nummer des jetzigen neurons im output layer, n ist die Anzahl der Neuronen im output Layer, a_j ist der Output des j Neurons im output Layer, y_j ist der gewünschte Ouput des j Neuron    
    #
    # w = das weigth von dem man den Einfluss auf die Cost function berechnen will

    # z = w_1 * a_1^(L-1) + w_2 * a_2(L-1) + .... + b_1   # a_1^(L-1) ist der Outputs des Neurons im vorherigen Layer, welches per weigth mit dem aktuellen Neuron im output layer verbunden ist, b_1 ist das bias vom aktuellen Output Neuron

    # a = sig(z)  # ist der output des aktuellen Neurons, dieser wird berechnet indem man z in die sigmoid function reintut 

    # d         d         d          d
    # -  C   =  -  z  *   -  a   *   -   C
    # dw        dw        dz         da


    print("that is backpropagation")

    dz = output_neuron.weigth[weigth_pos]

    da = sigmoid_ableitung(dz)

    dC_a = (da - expected_output) * 2

    dC_w = dz * da * dC_a

    print(dC_w)

    output_neuron.backpropagated_weigths[weigth_pos] = dC_w

    return dC_w



def activision_backpropagation_of_layer(layer):

    


    # go through all avtivations of the layer
    for i in len(neurons[layer]):

        # go through all avtivations of the next layer
        for j in len(neurons[layer-1]):

            if layer < -1:

                print("backpropagate with the BPed activisions of previous layer")

            elif layer == -1:

                print("backpropagate from output layer to this layer")





def backpropagation_of_weigths(layer, weigth_pos, Neuron_pos):

    print("test")




    

root = tk.Tk()


buttons = []
counter = []

neurons = []
neuron_outputs = []

def start_neuronal_network(start_value, neuron_count, layers, expected_number):

    print(start_value)

    print(expected_number)


    input_value = start_value

    for i in range(layers):

        temp_value = []

        neurons.append([])
        neuron_outputs.append([])

        for j in range(neuron_count):

            neurons[i].append(Neuron(input_value)) 

            

            temp_value.append(neurons[i][j].output())

            neuron_outputs[i].append(neurons[i][j].output())

            

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


    backpropagation_of_weigth_OutLayer(neurons[-1][0], 0, 1)





      

    


    
    
    
    

    


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
