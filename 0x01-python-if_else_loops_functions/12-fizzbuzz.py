#!/usr/bin/python3
def fizzbuzz():
    mylist = list(range(1, 101))
    for pro in mylist:
        if pro % 3 == 0 and pro % 5 != 0:
            print("Fizz ", end="")
        elif pro % 5 == 0 and pro % 3 != 0:
            print("Buzz ", end="")
        elif pro % 3 == 0 and pro % 5 == 0:
            print("FizzBuzz ", end="")
        else:
            print("{:d} " .format(pro), end="")
