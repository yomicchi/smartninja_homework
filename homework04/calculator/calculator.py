# coding=utf-8


x = int(raw_input("Gib einen Wert für x ein: "))
print x

y = int(raw_input("Gib einen Wert für y ein "))
print y

operation = raw_input("Wähle eine Rechenart aus (+, -, *, /:) ")
print operation

if operation == "+":
    print "Das Ergebnis beträgt " + str(int(x) + int(y)) + "."
elif operation == "-":
    print "Das Ergebnis beträgt " + str(int(x) - int(y)) + "."
elif operation == "*":
    print "Das Ergebnis beträgt " + str(int(x) * int(y)) + "."
elif operation == "/":
    print "Das Ergebnis beträgt " + str(int(x) / int(y)) + "."
else:
    print "Du hast keine gültige Rechenart ausgewählt!"
