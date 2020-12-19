# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:21:40 2020

@author: Nimje
"""
#Game

import random

num = random.randint(1,100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

guesses = [0]

while True:

    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess?: "))
    if guess==num:
        print("Correct Guess!")
        print(len(guesses)-1)
        break
    if len(guesses)==1:
        if guess < 1 or guess > 100:
            print('OUT OF BOUNDS! Please try again: ')
            print(guesses)
            continue
        elif abs(num - guess)<=10:
            print("WARM!")
            guesses.append(guess)
            print(guesses)
        else:
            print("COLD!")
            guesses.append(guess)
            print(guesses)
    else:
        if guess < 1 or guess > 100:
            print('OUT OF BOUNDS! Please try again: ')
            print(guesses)
            continue
        elif abs(num - guess)<=abs(num - guesses[-1]):
            print("WARMER!")
            guesses.append(guess)
            print(guesses)
        else:
            print("COLDER!")
            guesses.append(guess)
            print(guesses)
    

