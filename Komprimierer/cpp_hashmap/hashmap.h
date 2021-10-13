#pragma once
#include <iostream>
#include<list>



// als key die Länge des Arrays mal die position im text

class Own_Hashmap
{

private:

    int size = 1;

    int *Hash_Array = new int[size];

    // std::list<std::list<int>> test;
    


public:

    Own_Hashmap(int hash_size)
    {
        size = hash_size;

        int *Hash_Array = new int[size];

        // test.resize(size);


        std::cout << size << std::endl;
    }
    ~Own_Hashmap()
    {
        delete[] Hash_Array;
    }

    //wir brauchen zwei arrays eins für die Umwandlung in den Zahlencode und das zweite für die Umwandlung 
    //zum Wort/Silbe
    void Insert(int key, int value)
    {
        int hash_value = key % size;


        if(Hash_Array[hash_value] == 0)
        {
            
            Hash_Array[hash_value] = value;
        }
        else
        {
            //bei jedem value den key mit abspeichern um bei einer Kollision die elemente aus einer liste dem key zu zuordnen.


            
        }

        
    }
};


