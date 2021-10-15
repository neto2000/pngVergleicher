
def Save(save_item, save_file):

    print("save")
    
    #0=gar nichts; 1=zahl; 2=string; 3=bool
    data_type = 0


    if type(save_item) == type(1) or type(save_item) == type(1.1):
        data_type = 1

    elif type(save_item) == type("string"):
        data_type = 2

    elif type(save_item) == type(True):
        data_type = 3

    else:
        print("error")


    print(type(save_item))

    print(data_type)

    try:
    
        Kaze_file = open(save_file, "r")

        Kaze_file.close()


    
    except:

        Kaze_file = open(save_file, "w")

        Kaze_file.write("{\n}\n")

        Kaze_file.close()


    Kaze_file = open(save_file, "r")

    lines = Kaze_file.readlines()

    Kaze_file.close()



    saved_var_counter = len(lines) - 2


    

    if saved_var_counter > 0:

        lines[-2] = lines[-2][:-2] + "," + lines[-2][-2:] 

    lines[-1] = "    save_var" + str(saved_var_counter) + ": " + str(save_item) + " \n"

    lines.append("} \n")

    Kaze_file = open(save_file, "w")


    Kaze_file.writelines(lines)



    Kaze_file.close()


lol = [10, 10, 11]

Save(lol, "test.json")    

