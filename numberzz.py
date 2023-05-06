import random
import time
import os
import sys

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def num_question():

    num_question.num_numbers = int(input("Enter how many digits to recall: \n"))
    print(f"After 5 seconds, you will see a list of {num_question.num_numbers} random digits. \n")
    print("You have to recall them in the correct order. \n")
    time.sleep(5)
    os.system('clear')
    
    num_question.answer_digits = []

    for number in range(0, num_question.num_numbers):
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
    def continues_num():
        continues = input(f"Type 'Y' if you want to start over or 'N' if you want to terminate the program. \n")
        continues = continues.lower()
        if (continues == 'y'):
            num_question()
            num_answer()
            statistics()
        elif (continues == 'n'):
            sys.exit()
        else:
            continues_num()
    continues_num()