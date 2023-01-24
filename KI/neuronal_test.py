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




OUTPUT_LAYER_COUNT = 10






class Neuron:
    def __init__(self, value, IS_OUTPUT_LAYER=None):

        self.input = value

        self.IS_OUTPUT_LAYER = IS_OUTPUT_LAYER

        self.activision = 0

        self.backpropagated_activisions = []

        self.backpropagated_weigths = []

        self.weight = []

        for i in range(len(self.input)):

            self.weight.append(rnd.randint(-10 , 10))
            self.backpropagated_weigths.append(0)
            self.backpropagated_activisions.append(0)

        


        self.bias = 0




    # Ziel: den Einfluss eines weigths auf die cost FUnktion berechnen (Ableitung von der Cost Function mit dem Parameter w (das weigth))
    #
    # Kettenregel (alle zwischen funktionen die zu der ableitung der Cost Function führen auch ableiten und multiplizieren)

    # C ist die Cost function
    # C = sum( (a_j - y_j)^2 ), j = 1 to n       # j ist die nummer des jetzigen neurons im output layer, n ist die Anzahl der Neuronen im output Layer, a_j ist der Output des j Neurons im output Layer, y_j ist der gewünschte Ouput des j Neuron    
    #
    # w = das weigth von dem man den Einfluss auf die Cost function berechnen will

    # z ist die rohe activision ohne sigmoid
    # z = w_1 * a_1^(L-1) + w_2 * a_2(L-1) + .... + b_1   # a_1^(L-1) ist der Outputs des Neurons im vorherigen Layer, welches per weigth mit dem aktuellen Neuron im output layer verbunden ist, b_1 ist das bias vom aktuellen Output Neuron

    # a ist die activision
    # a = sig(z)  # ist der output des aktuellen Neurons, dieser wird berechnet indem man z in die sigmoid function reintut 

    # d         d         d          d
    # -  C   =  -  z  *   -  a   *   -   C
    # dw        dw        dz         da


    # def backpropagate_weigths(self, output_neuron_pos):

    #     for i in range(self.backpropagated_weigths[output_neuron_pos]):

    #         if self.IS_OUTPUT_LAYER:

    #             dz = self.activision

    #             da = sigmoid_ableitung(dz)

    #             dC_a = (da - expected_output_list[neurons[-1].index(self)]) * 2

    #             dC_w = dz * da * dC_a

    #             print(dC_w)

    #             self.backpropagated_weigths[output_neuron_pos][i] = dC_w

    #         else:



    # def backpropagate_activisions(self, output_neuron_pos):

    #     print("2")


    # def backpropagate_bias(self, output_neuron_pos):

    #     print("bias")

    
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









# def activision_backpropagation_of_layer(layer):

    


#     # go through all avtivations of the layer
#     for i in len(neurons[layer]):

#         # go through all avtivations of the next layer
#         for j in len(neurons[layer-1]):

#             #Output layer ist -1 alle layer danach sind in absteigender Reihenfolge sortiert. Nächster layer -2, danach -3 usw.
#             if layer < -1:

#                 print("backpropagate with the BPed activisions of previous layer")

#                 dz = neurons[layer][i].weigth[j]

#                 da = sigmoid_ableitung(dz)

#                 dC_aL_1 = dz * da * neurons[layer + 1][i].backpropagated_activisions[j]



#             elif layer == -1:

#                 print("backpropagate from output layer to this layer")

#                 dz = neurons[layer][i].weigth[j]

#                 da = sigmoid_ableitung(dz)

#                 dC_a = (da - expected_output_list[i]) * 2

#                 dC_aL_1 = dz * da * dC_a

#                 neurons[layer][i].backpropagated_activisions[j] = dC_aL_1

                

                
def rekursive_backpropagation(layer, prev_BPed_activision, prev_neuron):

    if abs(layer) < len(neurons):

        mittelwert_of_BPed_weigths = []

        BPed_weight_next_layers = []

        neuron_BPed_weights = []

        for neuron_pos in range(len(neurons[layer])):

            dz = prev_neuron.weight[neuron_pos]

            da = sigmoid_ableitung(dz)

            BPed_activision = dz * da * prev_BPed_activision

        
            BPed_weight_next_layers.append(rekursive_backpropagation(layer-1, BPed_activision, neurons[layer][neuron_pos]))

            print(BPed_weight_next_layers)

            print("----------------------------------------")

            #mittelwert von vorherigen backprops





            # backprop von eigenen weights

            neuron_BPed_weights.append([])

            for weight_pos in range(len(neurons[layer][neuron_pos].weight)):

                dz = neurons[layer - 1][weight_pos].activision

                da = sigmoid_ableitung(dz)

                BPed_weight = dz * da * BPed_activision

                neuron_BPed_weights[neuron_pos].append(BPed_weight)



        zipped_lists = zip(*BPed_weight_next_layers)

        zipped_layers = []

        for layer in zipped_lists:

            zipped_layers.append(zip(*layer))


        for layer in range(len(zipped_layers)):

            mittelwert_of_BPed_weigths.append([])

            neuron_count = 0

            for weights in zipped_layers[layer]:

                mittelwert_of_BPed_weigths[layer].append([])

                zipped_weights = zip(*weights)

                for wight_pair in zipped_weights:

                    mittelwert_of_BPed_weigths[layer][neuron_count].append(sum(wight_pair) / len(zipped_layers))

                neuron_count += 1


        #!!!!  mittelwert von allen listen aus BPed_weight_next_layers in output_BPed_weight_list


        mittelwert_of_BPed_weigths.append(neuron_BPed_weights)

        print(mittelwert_of_BPed_weigths)

        print("----------------m------------------------")

        return mittelwert_of_BPed_weigths

        

    else:

        neuron_BPed_weights = [[]]

        for neuron_pos in range(len(neurons[layer])):

            dz = prev_neuron.weight[neuron_pos]

            da = sigmoid_ableitung(dz)

            BPed_activision = dz * da * prev_BPed_activision

            neuron_BPed_weights[0].append([])

            for input in input_layer:

                # backprop von eigenen weights

                dz = input

                da = sigmoid_ableitung(dz)

                BPed_weight = dz * da * BPed_activision

                neuron_BPed_weights[0][neuron_pos].append(BPed_weight)

        return neuron_BPed_weights



        









def backpropagation_of_weights():

    BPed_weigths_of_output_neurons = []

    neuron_BPed_weights = []

    backpropagated_weights = []

    current_output_neuron = 0
    
    for output_neuron in neurons[-1]:

        dC_a = 2*(output_neuron.activision - expected_output_list[current_output_neuron])

        dz = sigmoid_ableitung(dC_a)

        ableitung_of_output = dz * dC_a

        BPed_weigths_of_output_neurons.append(rekursive_backpropagation(-2, ableitung_of_output, output_neuron))

        neuron_BPed_weights.append([])

        for weight_pos in range(len(neurons[-1][current_output_neuron].weight)):

            print(len(neurons[-1][current_output_neuron].weight))

            BPed_weight = ableitung_of_output * neurons[-2][weight_pos].activision

            neuron_BPed_weights[current_output_neuron].append(BPed_weight)

        current_output_neuron += 1


    zipped_lists = zip(*BPed_weigths_of_output_neurons)

    zipped_layers = []

    for layer in zipped_lists:

        zipped_layers.append(zip(*layer))


    for layer in range(len(zipped_layers)):

        backpropagated_weights.append([])

        neuron_count = 0

        for weights in zipped_layers[layer]:

            backpropagated_weights[layer].append([])

            zipped_weights = zip(*weights)

            for wight_pair in zipped_weights:

                backpropagated_weights[layer][neuron_count].append(sum(wight_pair) / len(zipped_layers))

            neuron_count += 1


    backpropagated_weights.append(neuron_BPed_weights)

    return backpropagated_weights






    

# root = tk.Tk()


# buttons = []
# counter = []

neurons = []
neuron_outputs = []



def start_neuronal_network(start_value, neuron_count, layers, expected_number):

    global expected_output_list
    global input_layer

    print(start_value)

    print(expected_number)


    input_layer = start_value

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

    for i in range(OUTPUT_LAYER_COUNT):
        expected_output_list.append(0)

        if i == expected_number:
            expected_output_list[i] = 1


    cost = 0
    neurons.append([])

    for i in range(OUTPUT_LAYER_COUNT):


        neurons[-1].append(Neuron(input_value, True))

        
        output = neurons[-1][i].output()

        print(output)

        add_cost = (output - expected_output_list[i]) ** 2

        cost = cost + add_cost


    print("cost: " + str(cost))

    print("----------backpropagated-weights----------")

    print(backpropagation_of_weights())

    





      

    


    
    
    
    

    


# #draw digit

# def change_color(i):

#     if counter[i] == 0:
#         buttons[i].configure(bg="white") 

#         counter[i] = 1

#         print("on" + str(i))

#     elif counter[i] == 1:
#         buttons[i].configure(bg="black") 

#         counter[i] = 0

#         print("off" + str(i))



# x = -10

# y = 10

# for i in range(256):
    
#     counter.append(0)
#     buttons.append(tk.Button(root, command=lambda i=i: change_color(i))) 

    


#     x += 20

#     if x >= 330:

#         y += 20

#         x = 10

#     buttons[i].place(x=x, y=y, width=20, height = 20)

#     buttons[i].configure(bg="black")


# expec_number_field = tk.Entry(root)

# expec_number_field.pack()


# start_button = tk.Button(root, text="Start", command=lambda: start_neuronal_network(counter, 8, 2, int(expec_number_field.get())))

# start_button.pack()





# root.mainloop()
