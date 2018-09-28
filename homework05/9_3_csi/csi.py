# coding=utf-8
Haarfarbe = {
    "schwarz": "CCAGCAATCGC",
    "braun": "GCCAGTGCCG",
    "blond": "TTAGCTATCGC"}

Gesichtsform = {
    "quadratisch": "GCCACGG",
    "rund": "ACCACAA",
    "oval": "AGGCCTCA",
}

Augenfarbe = {
    "blau": "TTGTGGTGGC",
    "grün": "GGGAGGTGGC",
    "braun": "AAGTAGTGAC",
}

Geschlecht = {
    "weiblich": "TGAAGGACCTTC",
    "männlich": "TGCAGGAACTTC",
}


Rasse = {
    "weiß": "AAAACCTCA",
    "schwarz": "CGACTACAG",
    "asiatisch": "CGCGGGCCG",
}

Eva = {
    "Geschlecht": "weiblich",
    "Rasse": "weiß",
    "Haarfarbe": "blond",
    "Augenfarbe": "blau",
    "Gesichtsform": "oval",
}


Larisa = {
    "Geschlecht": "weiblich",
    "Rasse": "weiß",
    "Haarfarbe": "braun",
    "Augenfarben": "braun",
    "Gesichtsform": "oval",
}


Matej = {
    "Geschlecht": "männlich",
    "Rasse": "weiß",
    "Haarfarbe": "schwarz",
    "Augenfarbe": "blau",
    "Gesichtsform": "oval",
}


Miha = {
    "Geschlecht": "männlich",
    "Rasse": "weiß",
    "Haarfarbe": "braun",
    "Augenfarbe": "grün",
    "Gesichtsform": "quadratisch",
}

with open("dna.txt", "r") as f:
    dna = f.read()
    f.close()

eigenschaften_namen = ["Haarfarbe", "Gesichtsform", "Augenfarbe", "Geschlecht", "Rasse"]
eigenschaften_liste = [Haarfarbe, Gesichtsform, Augenfarbe, Geschlecht, Rasse]
eigenschaften_mit_name = zip(eigenschaften_namen, eigenschaften_liste)


beschuldigter_name = ["Miha", "Eva", "Larisa", "Matej"]
beschuldigter_liste = [Miha, Eva, Larisa, Matej]
beschuldigter_mit_name = zip(beschuldigter_name, beschuldigter_liste)


treffer_eigenschaften = {}

print
print "*"*40
for name, eigenschaft in eigenschaften_mit_name:
    for key, val in eigenschaft.iteritems():
        if val in dna:
            treffer_eigenschaften[name] = key
            print "DNA Übereinstimmung ", name + ":", key
            break


for name, beschuldigter in beschuldigter_mit_name:
    print "*" * 40
    print
    print name, "durchsuchen"
    print
    print "*"*40
    print
    for eigenschaft, besch_val in beschuldigter.iteritems():
        print "Überprüfung", eigenschaft + " ......... überprüft"
        if treffer_eigenschaften[eigenschaft] != besch_val:
            print "Keine Übereinstimmung"
            print "-"*10
            break
    else:
        print
        print "*"*40
        print
        print "%s hat das Eis gegessen!" % name
        break
