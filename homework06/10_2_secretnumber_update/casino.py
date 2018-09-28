# coding=utf-8
import random

print "╔════════════════════════════════════════════════╗"
print "║ Willkommen im Casino!                   ║"
print "║       ∧＿∧                              ║"
print "║    ／(๑•ω•๑) ／＼                        ║"
print "║   ／|￣∪ ∪ ￣|＼／                       ║"
print "║    |＿＿ ＿＿ |／                         ║"
print "╚════════════════════════════════════════════════╝"


def main():
    secret = random.randint(1, 100)
    highest_number = 100

    while True:
        try:
            guess = int(raw_input("Bitte suche dir eine Zahl zwischen 0 und " + str(highest_number) + " aus: "))
            print guess

            if guess == secret:
                print "Gratulation! Richtig geraten!"
                break
            elif guess > secret:
                print "Deine Zahl ist leider zu groß. Versuche es nochmal!"
            elif guess < secret:
                print "Deine Zahl ist leider zu klein. Versuche es nochmal!"

        except Exception as e:
            print "Bitte gib eine ganze Zahl an!"


if __name__ == '__main__':
    main()
