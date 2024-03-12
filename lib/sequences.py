#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = []
    if length == 0:
        print([])
    elif length == 1:
        fibonacci.append(0)
        print([0])
    elif length == 2:
        fibonacci.append(0)
        fibonacci.append(1)
        print(fibonacci)
    else:
        fibonacci = [0,1]
        for num in range(length -2):
            fibonacci.append(fibonacci[-2] + fibonacci[-1])
        print(fibonacci)


    #     
    


    




    