# coding=utf-8
import random


def rand_num(anzahl):
    zahlenliste = []

    while True:
        if len(zahlenliste) == anzahl:
            break

        zahl = random.randint(1, 46)

        if zahl not in zahlenliste:
            zahlenliste.append(zahl)

    return zahlenliste


def main():
    print "Willkommen beim Lottozahlen-Generator!"

    print

    try:
        print "Hier ist deine Zahlenliste: " + str(rand_num(int(raw_input("Wieviele Zahlen möchtest du ausgeben bekommen?"))))
    except Exception as e:
        print "Bitte gib eine Zahl ein!"


if __name__ == '__main__':
    main()

