import wordzz
import numberzz
import random
import os
import time
import sys
import logo
from termcolor import colored

print(colored(logo.memso, 'red'))

print("Welcome to the Memory Game: MEMSO \n")

def choices():
    types = input("Choose either 'Words or 'Numbers' \n")
    types = types.lower()
    if (types == 'numbers'):
        numberzz.num_question()
        numberzz.num_answer() 
    elif (types == 'words'):
        wordzz.question_word()
        wordzz.answer_word()
    else:
        print("You gave an invalid choice.")
        choices()

choices()