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

    eckige_klammern = 0

    item_counter = 0

    for i in range(len(lines)):
        
        eckige_klammern += lines[i].count("[")

        if eckige_klammern == 0:
            variables[item_counter].append(lines[i].replace(",", ''))
        
        elif eckige_klammern == 1:

            bet_line = lines[i].replace("[",'')
            bet_line = lines[i].replace("]",'')

            variables[item_counter].append(bet_line.split(","))

        

        eckige_klammern -= lines[i].count("]")

        if eckige_klammern == 1:

            variables.append([])
        elif eckige_klammern == -1:
            item_counter +=1



    print(eckige_klammern)



print(Path(__file__).resolve().parent.parent.parent)

Get("Komprimierer/hash.json")



