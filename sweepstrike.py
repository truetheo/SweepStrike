#! python3
# sweepstrike.py - Creates world cup tuples with questions and answers in
# random order, along with the question key.
import random
import itertools
import time


def czytaj_kraje():
    filez = open(r'D:\python_scripts\kraje.txt', 'r')
    countries = filez.read().splitlines()
    filez.close()
    return countries


def zapiszOsoby():
    with open("names.txt", "w") as text_file:
        for i in range(1, 33):
            print(f"Osoba {str(i)}", file=text_file)
        text_file.close()
    print("Writing done!")


def czytaj_osoby():
    filez = open(r'D:\python_scripts\names.txt', 'r')
    names = filez.read().splitlines()
    filez.close()
    return names


def lista1(ludzie, kraje):
    print("Rozpoczynam loswanie!")
    for osoba, kraj in itertools.product(ludzie, kraje):
        print(osoba + " wylosowala - " + kraj)
    print("Koniec losowania!")


def lista2(ludzie, kraje):
    assignments = list(zip(ludzie, kraje))
    """ wypisz wynik
    for i in assignments:
        time.sleep(2)
        print(i)
    """
    return assignments


def zapisz_wyniki(wynik):
    date_string = time.strftime("%Y-%m-%d_%H%M%S")
    with open("wyniki{0}.txt".format(date_string), "w") as text_file:
        for i in range(0, 32):
            print(f"Para:  {str(i+1)}", file=text_file)
            print(wynik[i], file=text_file)
        text_file.close()
    print("Writing done!")


"""czyta plik z lista osob bioracych udzial w zabawie oraz lista druzyn"""
ludzie = czytaj_osoby()
kraje = czytaj_kraje()
"""randomowe przesortowanie list"""
random.shuffle(ludzie)
random.shuffle(kraje)
"""polaczenie w pary"""
wynik = lista2(ludzie, kraje)
"""zapisanie do pliku"""
zapisz_wyniki(wynik)
