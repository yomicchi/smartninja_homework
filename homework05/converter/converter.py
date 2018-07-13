# coding=utf-8

print "*" * 65
print " _   _       _ _     _____                           _  "
print "| | | |     (_) |   /  __ \                         | |"
print "| | | |_ __  _| |_  | /  \/ ___  _ ____   _____ _ __| |_ ___ _ __"
print "| | | | '_ \| | __| | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|"
print "| |_| | | | | | |_  | \__/\ (_) | | | \ V /  __/ |  | ||  __/ |"
print " \___/|_| |_|_|\__|  \____/\___/|_| |_|\_/ \___|_|   \__\___|_|"
print
print
print "Willkommen beim Größenumrechner :)"
print "Dieses Programm rechnet Kilometer in Meilen um!"
print "*" * 65

print
print

while True:
    print "Bitte gib die Kilometer, die du umrechnen möchtest ein!"
    km = raw_input("Kilometer:")

    try:
        km = float(km.replace(",", "."))

        if km > 0:
            miles = km * 0.621371

        print "{0} Kilometer sind {1} Meilen.".format(km, miles)
    except Exception as e:
        print "Bitte gib ausschließlich Zahlen ein!"

    repeat = raw_input("Möchtest du eine weitere Umrechnung tätigen (y/n)?: ")

    if repeat.lower() != "y" and repeat.lower() != "yes":
        print "Danke für's Benutzen :)"
        break




