# coding=utf-8

print "╔════════════════════════════════════════════════╗"
print "║ Willkommen im Casino!                   ║"
print "║       ∧＿∧                              ║"
print "║    ／(๑•ω•๑) ／＼                        ║"
print "║   ／|￣∪ ∪ ￣|＼／                       ║"
print "║    |＿＿ ＿＿ |／                         ║"
print "╚════════════════════════════════════════════════╝"

secret = 33
highestNumber = 100

guess = int(raw_input("Bitte suche dir eine Zahl zwischen 0 und " + str(highestNumber) + " aus: "))
print guess

if guess > secret:
    print "Deine Zahl ist leider zu groß."
elif guess < secret:
    print "Deine Zahl ist leider zu klein."
elif guess == secret:
    print "Gratulation! Richtig geraten!"
