import py_hashmap as h



test = h.HashMap(7)

test.Insert(7, "no.1")

test.Insert(14, "no.2")

test.Insert(5, "no.3")

print(test.hash_list)

 

print(test.Output(14))

