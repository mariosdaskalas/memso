import random
import time
import os
import sys

f = open('flowers.txt', 'r')
content = f.read()

words = content.split("\n")

def question_word():
    choice = input("Choose either 'Level' or 'Specific' \n")
    if (choice == "level"):
        choice = choice.lower()
        level = input("Enter Level # Low / Medium / Hard \n")
        if (level == 'low'):
            question_word.num_words = 5
        elif (level == 'medium'):
            question_word.num_words = 10
        elif (level == 'hard'):
            question_word.num_words = 20
        else:
            print(f"Invalid entry.")
            question_word()
            answer_word()
    elif (choice == 'specific'):
        choice = choice.lower()
        question_word.num_words = int(input("Enter how many flowers to recall: \n"))
    else:
        print(f"Invalid entry.")
        question_word()
        answer_word()
    print(f"After 5 seconds, you will see a list of {question_word.num_words} random flowers. \n")
    print("You have to recall them in the correct order. \n")
    time.sleep(5)
    os.system('clear')
    question_word.answer_words = []
        
    for word in range(0, question_word.num_words):
        random_word = random.randint(0, len(words))
        print(f"Word[{word + 1}]: {words[random_word]}")
        time.sleep(1)
        os.system('clear')

        question_word.answer_words.append(words[random_word])
    os.system('clear')
    print("Time to recall the flowers in order: \n")

def answer_word():
    score = 0

    for answer in range(0, len(question_word.answer_words)):
        userAnswer = input(f"Please type the {answer + 1} flower: \n")
        userAnswer = userAnswer.lower()
        os.system('clear')
        if (userAnswer == question_word.answer_words[answer].lower()):
            print(f"Correct (+1)")
            score = score + 1
        else:
            print(f"Wrong (-1): The flower was: {question_word.answer_words[answer]}")
            score = score - 1
        print(f"Your total score: {score}")
    
    def continues_word():
        continues = input(f"Type 'Y' if you want to start over or 'N' if you want to terminate the program. \n")
        continues = continues.lower()
        if (continues == 'y'):
            question_word()
            answer_word()
        elif (continues == 'n'):
            sys.exit()
        else:
            continues_word()
    continues_word()

f.close()