

from posixpath import split


test = "[[moin, lol, lel]]"

test = test.replace("[", '')

test = test.replace("]", '')

ergeb = test.split(",")

print(ergeb)

