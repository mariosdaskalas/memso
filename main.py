import random
import os
import time
import sys
import logo

print(logo.memso)
#print(logo.art)

f = open('words.txt', 'r')
content = f.read()

words = content.split("\n")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Welcome to the Memory Game: MEMSO \n")

def num_question():
    num_numbers = int(input("Enter how many digits to recall: \n"))
    print("After 5 seconds, you will see a list of random digits. \n")
    print("You have to recall them in the correct order. \n")
    time.sleep(5)
    os.system('clear')

    num_question.answer_digits = []

    for number in range(0, num_numbers):
        random_digit = random.randint(0, len(numbers) - 1)
        print(f"Digit[{number + 1}]: {numbers[random_digit]}")
        time.sleep(1)
        os.system('clear')

        num_question.answer_digits.append(numbers[random_digit])

def statistics():
    print(f"-- Statistics -- \n")
    for i in range(0, 10):
        count = num_question.answer_digits.count(i)
        print(f"{i} appeared: {count} times")

def num_answer():
    score = 0

    for answer in range(0, len(num_question.answer_digits)):
        userAnswer = input(f"Please type the {answer + 1} digit: \n")
        
        os.system('clear')
        if (userAnswer == str(num_question.answer_digits[answer])):
            print(f"Correct (+1)")
            score = score + 1
        else:
            print(f"Wrong (-1): The digit was: {num_question.answer_digits[answer]}")
            score = score - 1
        print(f"Your total score: {score}")
    statistics()

def question_word():
    print("After 5 seconds, you will see a list of random words. \n")
    print("You have to recall them in the correct order. \n")
    time.sleep(5)
    os.system('clear')
    question_word.answer_words = []
        
    for word in range(0, choices.num_words):
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

def choices():
    types = input("Choose either 'Words or 'Numbers' \n")
    types = types.lower()
    if (types == 'numbers'):
        num_question()
        num_answer()
    elif (types == 'words'):
        choice = input("Choose either 'Level' or 'Specific' \n")
        if (choice == "level"):
            choice = choice.lower()
            level = input("Enter Level # Low / Medium / Hard \n")
            if (level == 'low'):
                choices.num_words = 5
                question_word()
                answer_word()
            elif (level == 'medium'):
                choices.num_words = 10
                question_word()
                answer_word()
            elif (level == 'hard'):
                choices.num_words = 20
                question_word()
                answer_word()
            else:
                print(f"Invalid entry.")
        elif (choice == "specific"):
            choice = choice.lower()
            choices.num_words = int(input("Enter how many words to recall: \n"))
            question_word()
            answer_word()
        else:
            print(f"Invalid entry.")
            continues = input("Type 'Y' to give another option or 'N' to terminate \n")
            continues = continues.lower()
            if (continues == "y"):
                choices()
            elif (continues == "n"):
                print("The program will terminate...")
                sys.exit()
    else:
        print("You gave an invalid choice.")
        choices()

choices()

f.close()