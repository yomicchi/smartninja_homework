# coding=utf-8
import random


def rand_num(anzahl):
    return sorted(random.sample(range(1,47), anzahl))


def main():
    print "Willkommen beim Lottozahlen-Generator!"

    print

    try:
        print "Hier ist deine Zahlenliste: " + str(rand_num(int(raw_input("Wieviele Zahlen möchtest du ausgeben bekommen?"))))
    except Exception as e:
        print "Bitte gib eine Zahl ein!"


if __name__ == '__main__':
    main()