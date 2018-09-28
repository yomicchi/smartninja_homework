# coding=utf-8

print "Willkommen im Menüprogramm!"

menue = {}

add = True
while add == True:
    gericht = raw_input("Bitte einen Speisennamen eingeben: ")
    preis = raw_input("Bitte einen Preis für '%s' eingeben:" % gericht)

    try:
        preis = float(preis)
        preis = str('%.2f' % preis)
        menue[gericht] = preis

        verification = True
        while verification == True:
            ant = raw_input("Wollen Sie eine weitere Speise hinzufügen? (j/n)").lower()
            if ant == "j" or ant == "ja":
                verification = False
            elif ant == "n" or ant == "nein":
                print
                print "Danke, dass Sie das Menüprogramm benutzt haben!"
                verification = False
                add = False
            else:
                print "Bitte geben Sie j(a) oder n(ein) ein!"

    except Exception as e:
        print "Bitte geben Sie eine Zahl als Preis ein!"

menue_file = open("menue.txt", "w+")
print
print "Nachfolgend finden Sie das Menü."
print
menue_file.write("Unser Menü: \n\n")
for gericht in menue:
    print gericht + ": €" + menue[gericht]
    menue_file.write(gericht + ": €" + menue[gericht] + "\n")

menue_file.close()
