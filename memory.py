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
        '''
        choice = input("Choose either 'Level' or 'Specific' \n")
        if (choice == "level"):
            choice = choice.lower()
            level = input("Enter Level # Low / Medium / Hard \n")
            if (level == 'low'):
                wordzz.question_word.num_words = 5
                wordzz.question_word()
                wordzz.answer_word()
            elif (level == 'medium'):
                choices.num_words = 10
                wordzz.question_word()
                wordzz.answer_word()
            elif (level == 'hard'):
                choices.num_words = 20
                wordzz.question_word()
                wordzz.answer_word()
            else:
                print(f"Invalid entry.")
        elif (choice == "specific"):
            choice = choice.lower()
            choices.num_words = int(input("Enter how many words to recall: \n"))
            wordzz.question_word()
            wordzz.answer_word()
        else:
            print(f"Invalid entry.")
            continues = input("Type 'Y' to give another option or 'N' to terminate \n")
            continues = continues.lower()
            if (continues == "y"):
                choices()
            elif (continues == "n"):
                print("The program will terminate...")
                sys.exit()
                '''
    else:
        print("You gave an invalid choice.")
        choices()

choices()