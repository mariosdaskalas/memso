import random
import time
import os
import sys
import memory

f = open('words.txt', 'r')
content = f.read()

words = content.split("\n")

def question_word():
    print("After 5 seconds, you will see a list of random words. \n")
    print("You have to recall them in the correct order. \n")
    time.sleep(5)
    os.system('clear')
    question_word.answer_words = []
        
    for word in range(0, memory.choices.num_words):
        random_word = random.randint(0, len(words))
        print(f"Word[{word + 1}]: {words[random_word]}")
        time.sleep(1)
        os.system('clear')

        question_word.answer_words.append(words[random_word])
    os.system('clear')
    print("Time to recall the words in order: \n")

def answer_word():
    score = 0

    for answer in range(0, len(question_word.answer_words)):
        userAnswer = input(f"Please type the {answer + 1} word: \n")
        userAnswer = userAnswer.lower()
        os.system('clear')
        if (userAnswer == question_word.answer_words[answer]):
            print(f"Correct (+1)")
            score = score + 1
        else:
            print(f"Wrong (-1): The word was: {question_word.answer_words[answer]}")
            score = score - 1
        print(f"Your total score: {score}")
    def continues_word():
        continues = input(f"Type 'Y' if you want to start over or 'N' if you want to terminate the program. \n")
        continues = continues.lower()
        if (continues == 'y'):
            memory.choices()
        elif (continues == 'n'):
            sys.exit()
        else:
            print(f"You gave an invalid entry. \n")
            continues_word()
    continues_word()

f.close()