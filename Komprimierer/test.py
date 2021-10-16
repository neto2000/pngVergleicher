import py_hashmap as h
import save_in_file/save_in_format.py as save


test = h.HashMap(7)

test.Insert(7, "no.1")

test.Insert(14, "no.2")

print(test.hash_list)

save.Save(test.hash_list,"hash.json") 

print(test.Output(14))

