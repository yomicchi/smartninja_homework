# coding=utf-8

print "*" * 65
print "          ______ _        ______               "
print "          |  ___(_)       | ___ \              "
print "          | |_   _ _______| |_/ /_   _ ________"
print "          |  _| | |_  /_  / ___ \ | | |_  /_  /"
print "          | |   | |/ / / /| |_/ / |_| |/ / / / "
print "          \_|   |_/___/___\____/ \__,_/___/___|"
print
print

print "          Lass uns ein Spiel spielen ;D        "
print "*" * 65
print
print

ende = raw_input("Bitte gib eine Zahl zwischen 1 und 100 ein:")

try:
    ende = int(ende)

    if ende > 0 and ende <= 100:
        for zahl in range(1, ende + 1):
            if zahl % 3 == 0 and zahl % 5 == 0:
                print "FizzBuzz!! :DD"
            elif zahl % 3 == 0:
                print "Fizz!"
            elif zahl % 5 == 0:
                print "Buzz!"
            else:
                print zahl
    elif ende > 100 or ende < 0:
        print "Bitte gib keine negative Zahl ein!"

except Exception as e:
    print "Bitte gib eine ganze Zahl an!"
