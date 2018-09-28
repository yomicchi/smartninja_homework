# coding=utf-8

class Vehicle(object):
    def __init__(self, brand, model, kilometers, service_date):
        self.brand = brand
        self.model = model
        self.kilometers = kilometers
        self.service_date = service_date

    def add_km(self, added_km):
        self.kilometers += added_km

    def update_service_date(self, new_service_date):
        self.service_date = new_service_date

    def get_full_name(self):
        return self.brand + " " + self.model


def show_list(vehicles):
    for index, car in enumerate(vehicles):
        print "#" + str(index + 1)
        print car.get_full_name()
        print "Gefahrene Kilometer: " + str(car.kilometers)
        print "Letztes Service: " + car.service_date

    if not vehicles:
        print "Keine Fahrzeuge in dieser Liste. Geben Sie ein neues Fahrzeug ein."


def create_vehicle_object(brand, model, gef_km_str, service_date, vehicles):
    try:
        gef_km_str = gef_km_str.replace(",", ".")
        kilometers = float(gef_km_str)

        new_vehicle = Vehicle(brand=brand, model=model, kilometers=kilometers, service_date=service_date)

        vehicles.append(new_vehicle)

        return True
    except ValueError:
        return False


def add_car(vehicles):
    print "Bitte geben Sie die folgenden Daten ein:"
    brand = raw_input("Wie lautet die Automarke?")
    model = raw_input("Wie lautet das Automodel?")
    gef_km_str = raw_input("Wieviele km wurden gefahren?")
    service_date = raw_input("Wann war das letzte Service?")

    result = create_vehicle_object(brand, model, gef_km_str, service_date, vehicles)

    if result:
        print "%s %s wurde erfolgreich hinzugefügt!" % (brand, model)
    else:
        print "Bitte geben Sie eine Zahl für die gefahrenen Kilometer ein."


def edit_car(vehicles):
    if not vehicles:
        print "Keine Fahrzeuge in dieser Liste. Wählen Sie Option b und legen Sie ein neues Fahrzeug an."

    else:
        print "Wählen Sie die Nummer des Fahrzeuges aus, das Sie bearbeiten wollen:"

        for index, car in enumerate(vehicles):
            print "#" + str(index + 1) + " " + car.get_full_name()

        print ""
        selected_id = raw_input("Geben Sie die ID des zu korrigierenden Fahrzeuges an: ")
        selected_car = vehicles[int(selected_id) - 1]

        while True:
            print ""
            print "Wählen Sie eine der folgenden Korrekturmöglichkeiten:"
            print "a) Kilometeranzahl ändern"
            print "b) Servicesdatum ändern"
            print "c) Zurück zum Hauptmenü"
            print ""

            selection = raw_input("Bitte geben Sie Ihre Auswahl an (a, b, oder c): ")
            print ""

            if selection.lower() == "a":
                new_km = raw_input("Wieviele Kilometer wurden gefahren?")

                try:
                    new_km = new_km.replace(",", ".")
                    new_km = float(new_km)

                    selected_car.add_km(new_km)
                    print ""
                    print "Kilometerstand für %s wurde erfolgreich geändert." % (selected_car.get_full_name())
                except ValueError:
                    print "Geben Sie nur die Anzahl an gefahren Kilometern ein."

            elif selection.lower() == "b":
                new_service = raw_input("Geben Sie ein neues Servicedatum für %s an: " % selected_car.get_full_name())
                selected_car.update_service_date(new_service)

                print ""
                print "Servicedatum wurde erfolgreich geändert."

            elif selection.lower() == "c":
                print "Willkommen im Hauptmenü - bitte wählen Sie eine der folgenden Möglichkeiten:"
                break
            else:
                print "Unklare Eingabe. Bitte versuchen Sie es erneut."
                continue


def delete_car(vehicles):
    print "Wählen Sie die Nummer des Fahrzeuges aus, das Sie löschen wollen:"

    for index, car in enumerate(vehicles):
        print "#" + str(index + 1) + " " + car.get_full_name()

    print ""
    selected_id = raw_input("Geben Sie die ID des zu korrigierenden Fahrzeuges an: ")
    selected_car = vehicles[int(selected_id) - 1]

    vehicles.remove(selected_car)
    print ""
    print "Fahrzeug wurde erfolgreich gelöscht."


def save_to_file(vehicles):
    with open("vehicles.txt", "w+") as car_file:
        for vehicle in vehicles:
            car_file.write("%s,%s,%s,%s\n" % (vehicle.brand, vehicle.model, vehicle.kilometers, vehicle.service_date))


def main():
    print "Willkommen beim Vehicle Manager!"

    vehicles = []
    #
    # vehicles.append(Vehicle("Audi", "TT", "350", "12.05.2018"))
    # vehicles.append(Vehicle("Opel", "Mokka X", "137", "01.03.2017"))
    # vehicles.append(Vehicle("Mazda", "CX-5", "740", "18.06.2018"))

    with open("vehicles.txt", "r") as v_file:
        for line in v_file:
            try:
                brand, model, km_done_str, service_date = line.split(",")
                create_vehicle_object(brand, model, km_done_str, service_date, vehicles)
            except ValueError:
                continue

    while True:
        print ""
        print "Bitte wählen Sie eine der folgenden Möglichkeiten:"
        print "a) Liste aller Fahrzeuge"
        print "b) Fahrzeug hinzufügen"
        print "c) Bestehendes Fahrzeug ändern"
        print "d) Fahrzeug löschen"
        print "e) Programm beenden"
        print ""

        selection = raw_input("Bitte um Ihre Eingabe (a, b, c, d oder e): ")
        print ""

        if selection.lower() == "a":
            show_list(vehicles)
        elif selection.lower() == "b":
            add_car(vehicles)
        elif selection.lower() == "c":
            edit_car(vehicles)
        elif selection.lower() == "d":
            delete_car(vehicles)
        elif selection.lower() == "e":
            print "Vielen Dank, dass Sie den Vehicle Manager benutzt haben. Bis bald!"
            save_to_file(vehicles)
            break
        else:
            print "Unklare Eingabe. Bitte versuchen Sie es erneut."
            continue


if __name__ == "__main__":
    main()
