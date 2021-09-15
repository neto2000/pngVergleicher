#pragma once
#include <iostream>



// als key die Länge des Arrays mal die position im text

class Own_Hashmap
{

private:

    int size;




public:

    Own_Hashmap(int hash_size)
    {
        size = hash_size;

        std::cout << size << std::endl;
    }

    void Insert(int key, std::string value)
    {
        int hash_value = key % size;

        std::cout << hash_value << std::endl;
    }
};


