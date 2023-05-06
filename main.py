import wordzz
import numberzz
import countrizz
import flowerzz
import random
import os
import time
import sys
import logo

print(logo.memso)

print("Welcome to the Memory Game: MEMSO \n")

def choices():
    types = input("Choose either 'Words, 'Countries', 'Flowers' or 'Numbers' \n")
    types = types.lower()
    if (types == 'numbers'):
        numberzz.num_question()
        numberzz.num_answer() 
    elif (types == 'words'):
        wordzz.question_word()
        wordzz.answer_word()
    elif (types == 'countries'):
        countrizz.question_word()
        countrizz.answer_word()
    elif (types == 'flowers'):
        flowerzz.question_word()
        flowerzz.answer_word()
    else:
        print("You gave an invalid choice.")
        choices()

choices()