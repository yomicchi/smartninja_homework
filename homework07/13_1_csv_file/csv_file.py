from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'https://scrapebook22.appspot.com/'
response = urlopen(url).read()
soup = BeautifulSoup(response)

print soup.html.head.title.string


class Person:
    def __init__(self, vorname, nachname, email, city):
        self.vorname = vorname
        self.nachname = nachname
        self.email = email
        self.city = city


persons = []

for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = "https://scrapebook22.appspot.com" + link["href"]
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)

        name = person_soup.find("div", attrs={"class": "col-md-8"}).h1.string
        email = person_soup.find("span", attrs={"class": "email"}).string
        city = person_soup.find("span", attrs={"data-city": True}).string

        vorname, nachname = name.split(" ")

        person = Person(vorname=vorname, nachname=nachname, email=email, city=city)
        persons.append(person)

csv_question = raw_input("Wollen Sie die Daten in einer CSV-Datei speichern? (yes/no) ")

if csv_question.lower() == "yes" or "ja":
    csv_file = open("person_list.csv", "w")
    csv_file.write("Vorname,Nachname,Email,Stadt\n")

    for person in persons:
        csv_file.write("%s,%s,%s,%s\n" % (person.vorname, person.nachname, person.email, person.city))

csv_file.close()

print ("Danke, dass Sie Beautiful Soup benutzt haben!")
