from pathlib import Path


def Get(file):

    variables = []


    repo_path = Path(__file__).resolve().parent.parent.parent

    lib_file = Path(file)

    uni_file = repo_path / lib_file

    print(uni_file)

    try:
    
        Kaze_file = open(uni_file, "r")

        Kaze_file.close()


    
    except:

        print("could not find the file")


    Kaze_file = open(uni_file, "r")

    lines = Kaze_file.readlines()

    Kaze_file.close()

    print(lines[1])

    eckige_klammern_auf = 0
    eckige_klammern_zu = 0

    item_counter = 0

    for i in range(len(lines)):
        
        eckige_klammern_auf = lines[i].count("[")

        eckige_klammern_zu = lines[i].count("]")

        if eckige_klammern_auf - eckige_klammern_zu == 1:

            variables.append([])
        elif eckige_klammern_auf - eckige_klammern_zu == -1:
            item_counter +=1

        if eckige_klammern_auf == 0:
            print(variables)

            if lines[i].count("{") == 0:
                variables[item_counter].append(lines[i].replace(",", ''))
        
        elif eckige_klammern_auf == 1:

            bet_line = lines[i].replace("[",'')
            bet_line = lines[i].replace("]",'')

            # variables[item_counter].append(bet_line.split(","))

            print("test")

        elif eckige_klammern_auf == 2:

            # bet_line2 = variables[i].split(",")

            print("bet_line2")

        print(i)

        

        

        



    print(eckige_klammern_auf)



print(Path(__file__).resolve().parent.parent.parent)

Get("Komprimierer/hash.json")



