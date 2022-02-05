from pathlib import Path


def Get(file):

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

    for i in range(len(lines)):
        if "[" in lines[i]:
            print("array in line: " + str(i))

            eckige_klammern += 1



print(Path(__file__).resolve().parent.parent.parent)

Get("Komprimierer/hash.json")

