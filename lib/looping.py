#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    return [i ** 2 for i in int_list]

def fizzbuzz():
    for numbers in range(1, 101):
        if not numbers % 15:
            print("FizzBuzz")
        elif not numbers % 5:
            print("Buzz")
        elif not numbers % 3:
            print("Fizz")
        else:
            print(numbers)


