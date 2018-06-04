#! python3
# sweepstake.py - Creates world cup tuples with people and countiries in random order
import random
import itertools
import time


def read_countries():
    filez = open(r'D:\python_scripts\countries.txt', 'r')
    countries = filez.read().splitlines()
    filez.close()
    return countries


def save_names():
    with open("names.txt", "w") as text_file:
        for i in range(1, 33):
            print(f"Osoba {str(i)}", file=text_file)
        text_file.close()
    print("Writing done!")


def read_names():
    filez = open(r'D:\python_scripts\names.txt', 'r')
    names = filez.read().splitlines()
    filez.close()
    return names


def perform_lottery_one(names, countries):
    print("Lottery begins!")
    for osoba, kraj in itertools.product(names, countries):
        time.sleep(2)
        print(osoba + " has team from " + kraj)
    print("Lottery ends!")


def connect_two_lists(names, countries):
    assignments = list(zip(names, countries))
    return assignments


def save_result(result):
    date_string = time.strftime("%Y-%m-%d_%H%M%S")
    with open("result{0}.txt".format(date_string), "w") as text_file:
        for i in range(0, 32):
            print(f"Pair:  {str(i+1)}", file=text_file)
            print(result[i], file=text_file)
    text_file.close()
    print("Writing done!")


"""read files with names and countires"""
names = read_names()
countries = read_countries()
"""randomize lists"""
random.shuffle(names)
random.shuffle(countries)
"""connect into pairs"""
result = connect_two_lists(names, countries)
"""write to file"""
save_result(result)
