#!/usr/bin/python3
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

numbers[0:3] = ['two', 'three', 'five']
print(numbers)
numbers[0:3] = []
print(numbers)
numbers[0:3] = [2, 3, 5]
numbers[::2] = [100, 100, 100]
print(numbers)
