
def Get(file):

    try:
    
        Kaze_file = open(file, "r")

        Kaze_file.close()


    
    except:

        print("could not find the file")


    Kaze_file = open(file, "r")

    lines = Kaze_file.readlines()

    Kaze_file.close()

    print(lines)


Get("D:\Dokumente\Scripts\GitHub\pngVergleicher\Komprimierer\hash.json")

