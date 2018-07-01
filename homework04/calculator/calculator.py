# coding=utf-8

print "╔════════════════════════════════════════════════╗"
print "║ Willkommen beim Taschenrechner 2000!    ║"
print "║       ∧＿∧                              ║"
print "║    ／(๑•ω•๑) ／＼                        ║"
print "║   ／|￣∪ ∪ ￣|＼／                       ║"
print "║    |＿＿ ＿＿ |／                         ║"
print "╚════════════════════════════════════════════════╝"

num1 = float(raw_input("Gib den ersten Wert ein: "))
print num1

num2 = float(raw_input("Gib einen zweiten Wert ein "))
print num2

operation = raw_input("Wähle eine Rechenart aus (+, -, *, /:) ")
print operation

if operation == "+":
    print "Das Ergebnis beträgt " + str(num1 + num2) + "."
elif operation == "-":
    print "Das Ergebnis beträgt " + str(num1 - num2) + "."
elif operation == "*":
    print "Das Ergebnis beträgt " + str(num1 * num2) + "."
elif operation == "/":
    print "Das Ergebnis beträgt " + str(num1 / num2) + "."
else:
    print "Du hast keine gültige Rechenart ausgewählt!"
