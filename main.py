from requests import get
from words import valid_words
from colorama import Fore, Style
from random import choice


def get_random_word():
    word = choice(valid_words)


def play_wordle():

    print('''
 ____      ____   ___   _______     ______   _____     ________  
|_  _|    |_  _|.'   `.|_   __ \   |_   _ `.|_   _|   |_   __  | 
  \ \  /\  / / /  .-.  \ | |__) |    | | `. \ | |       | |_ \_| 
   \ \/  \/ /  | |   | | |  __ /     | |  | | | |   _   |  _| _  
    \  /\  /   \  `-'  /_| |  \ \_  _| |_.' /_| |__/ | _| |__/ | 
     \/  \/     `.___.'|____| |___||______.'|________||________| 
                                                                 ''')

    get_random_word()
