

class HashMap:
    def __init__(self, hash_size):
        self.size = hash_size

        self.hash_list = [[[None, None]]for _ in range(self.size)]

        

        # print(self.hash_list)

    def Insert(self, key, value):

        self.hash_value = key % self.size


        # print(self.hash_list[self.hash_value][0][0])

        if self.hash_list[self.hash_value][0][0] == None:

            self.hash_list[self.hash_value][0][0] = value

            self.hash_list[self.hash_value][0][1] = key

            # print(self.hash_list)

        else:
            self.hash_list[self.hash_value].append([0,0])

            lenght = len(self.hash_list[self.hash_value])

            self.hash_list[self.hash_value][lenght - 1][0] = value

            self.hash_list[self.hash_value][lenght - 1][1] = key


            # print(self.hash_list)


    def Output(self, key):

        self.hash_value_output = key % self.size

        lenght_output = len(self.hash_list[self.hash_value])

        if(lenght_output == 1):

            return self.hash_list[self.hash_value][0][0]

        else:

            for i in range(lenght_output):

                if self.hash_list[self.hash_value][i][1] == key:

                    return self.hash_list[self.hash_value][i][0]










        

