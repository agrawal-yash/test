# -*- coding: utf-8 -*-
"""
Created on Mon May  9 10:46:14 2022

@author: agraw
"""

def addition(num_1, num_2):
    return num_1 + num_2

def subtraction(num_1, num_2):
    return num_1 - num_2

def multiplication(num_1, num_2):
    return num_1 * num_2

if __name__ == "__main__":
    num_1 = int(input())
    num_2 = int(input())
    
    print ("Summation : ", addition(num_1, num_2))
    print ("Difference : ", subtraction(num_1, num_2))
    print ("Product : ", multiplication(num_1, num_2))