# coding=utf-8
from datetime import date


class Contact(object):
    def __init__(self, vorname, nachname, telefon, geburtsjahr, email):
        self.vorname = vorname
        self.nachname = nachname
        self.telefon = telefon
        self.geburtsjahr = geburtsjahr
        self.email = email

    def get_full_name(self):
        return self.vorname + " " + self.nachname

    def alter(self):
        today = date.today()
        return today.year - int(self.geburtsjahr)


def list_all_contacts(contacts):
    for index, person in enumerate(contacts):
        print "ID: " + str(index + 1)
        print person.get_full_name()
        print person.geburtsjahr
        print person.alter()
        print person.email
        print "~***~"

    if not contacts:
        print "Es sind keine Kontakte vorhanden."


def add_new_contact(contacts):
    vorname = raw_input("Bitte geben Sie einen Vornamen ein: ")
    nachname = raw_input("Bitte geben Sie einen Nachnamen ein: ")
    email = raw_input("Bitte geben Sie eine Email Adresse ein: ")
    telefon = raw_input("Bitte geben Sie eine Telefonnummer ein: ")
    geburtsjahr = raw_input("Bitte geben Sie ein Geburtsjahr an: ")

    new = Contact(vorname=vorname, nachname=nachname, telefon=telefon, geburtsjahr=geburtsjahr, email=email)
    contacts.append(new)

    print ""
    print new.get_full_name() + " wurde erfolgreich hinzugefügt."


def edit_contact(contacts):
    print "Wählen Sie die Nummer des Kontaktes aus, den Sie editieren wollen:"

    for index, person in enumerate(contacts):
        print "#" + str(index + 1) + " " + person.get_full_name()

    print ""
    selected_id = raw_input("Geben Sie die ID des zu korrigierenden Kontaktes an: ")
    selected_contact = contacts[int(selected_id) - 1]

    while True:
        print ""
        print "Wählen Sie eine der folgenden Korrekturmöglichkeiten:"
        print "a) Vorname ändern"
        print "b) Nachname ändern"
        print "c) Email ändern"
        print "d) Telefon ändern"
        print "e) Geburtsjahr ändern"
        print "f) Zurück zum Hauptmenü"
        print ""

        selection = raw_input("Bitte geben Sie Auswahl an (a, b, c, d oder e): ")
        print ""

        if selection.lower() == "a":
            new_fname = raw_input("Geben Sie einen neuen Vornamen für %s an:" % selected_contact.get_full_name())
            selected_contact.vorname = new_fname

            print ""
            print "Vorname wurde erfolgreich geändert."
        elif selection.lower() == "b":
            new_lname = raw_input("Geben Sie einen neuen Nachnamen für %s an: " % selected_contact.get_full_name())
            selected_contact.nachname = new_lname

            print ""
            print "Nachname wurde erfolgreich geändert."
        elif selection.lower() == "c":
            new_email = raw_input("Geben Sie eine neue Email Adresse für %s an:  " % selected_contact.get_full_name())
            selected_contact.email = new_email

            print ""
            print "Email wurde erfolgreich geändert."

        elif selection.lower() == "d":
            new_phone = raw_input("Geben Sie eine neue Telefonnummer für %s an:  " % selected_contact.get_full_name())
            selected_contact.telefon = new_phone

            print ""
            print "Telefonnummer wurde erfolgreich geändert."

        elif selection.lower() == "e":
            new_dob = raw_input("Geben Sie ein neues Geburtsjahr für %s an: " % selected_contact.get_full_name())
            selected_contact.geburtsjahr = new_dob

            print ""
            print "Geburtsdatum wurde erfolgreich geändert."

        elif selection.lower() == "f":
            print "Willkommen im Hauptmenü - bitte wählen Sie eine der folgenden Möglichkeiten:"
            break
        else:
            print "Ungklare Eingabe. Bitte versuchen Sie es erneut."
            continue


def delete_contact(contacts):
    print "Wählen Sie die Nummer des Kontaktes aus, den Sie löschen wollen:"

    for index, person in enumerate(contacts):
        print str(index + 1) + ") " + person.get_full_name()

    print ""
    selected_id = raw_input("Geben Sie die ID des zu löschenden Kontaktes an:  ")
    selected_contact = contacts[int(selected_id) - 1]

    contacts.remove(selected_contact)
    print ""
    print "Kontakt wurde erfolgreich gelöscht."


def main():
    print "Willkommen beim Contact Manager!"

    #Testeinträge
    john = Contact(vorname="John", nachname="Clark", telefon=89348239429, geburtsjahr=1979, email="john@clark.com")
    marissa = Contact(vorname="Marissa", nachname="Mayer", telefon=83483204032, geburtsjahr=1978,
                      email="marissa@yahoo.com")
    bruce = Contact(vorname="Bruce", nachname="Wayne", telefon=902432309443, geburtsjahr=1939, email="bruce@batman.com")
    contacts = [john, marissa, bruce]

    while True:
        print ""
        print "Bitte wählen Sie eine der folgenden Möglichkeiten:"
        print "a) Liste aller Kontakte"
        print "b) Kontakt hinzufügen"
        print "c) Bestehenden Kontakt ändern"
        print "d) Kontakt löschen"
        print "e) Programm beenden"
        print ""

        selection = raw_input("Bitte um Ihre Eingabe (a, b, c, d oder e): ")
        print ""

        if selection.lower() == "a":
            list_all_contacts(contacts)
        elif selection.lower() == "b":
            add_new_contact(contacts)
        elif selection.lower() == "c":
            edit_contact(contacts)
        elif selection.lower() == "d":
            delete_contact(contacts)
        elif selection.lower() == "e":
            print "Vielen Dank, dass Sie das Kontaktbuch benutzt haben. Bis bald!"
            break
        else:
            print "Unklare Eingabe. Bitte versuchen Sie es erneut."
            continue


if __name__ == "__main__":
    main()