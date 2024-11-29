#!/usr/bin/env python3

def return_evens(num_list):
    return [x for x in num_list if x % 2 == 0]
    

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]

if __name__ == "__main__":
    
    evens_result = return_evens([0, 1, 3, 5, 7, 8, 9])
    print("Evens result:", evens_result) 
    exclamation_result = make_exclamation(["Hello", "I'm doing great", "Python is fun"])
    print("Exclamation result:", exclamation_result)  
   

