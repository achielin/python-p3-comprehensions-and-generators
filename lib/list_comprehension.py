#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [num for num in num_list if num % 2 == 0]
    return even_numbers
    
num_list = [1,2,3,4,5,6,7,8,9,10]
result = return_evens(num_list)
print (result)

def make_exclamation(sentence_list):
    sentences_with_exclamation = [sentence + '!' for sentence in sentence_list]
    return sentences_with_exclamation

sentence_list =[ "Hello", "I'm doing great", "Python is fun"]
result= make_exclamation(sentence_list)
print(result)
