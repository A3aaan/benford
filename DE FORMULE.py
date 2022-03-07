from math import log10
from random import randint
def get_eerste_digit(getal):
    return getal//(10**(int(log10(getal))))

def eerste_digit(getal):
    return int(str(getal)[0])


"""test
my_set = set()
for _ in range(500000):
    getal = randint(1,1000000000000)
    my_set.add(eerste_digit(getal) == get_eerste_digit(getal))
print(my_set)
"""
