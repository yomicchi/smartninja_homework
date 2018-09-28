from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

quote_url = 'http://quotes.yourdictionary.com/theme/marriage/'
quote_html = urlopen(quote_url).read()
quote_soup = BeautifulSoup(quote_html)

quotes = quote_soup.findAll('p', limit=5, attrs={'class': 'quoteContent'})

print quote_soup.html.head.title.string + "\n"

for quote in quotes:
    print(quote.text + "\n" + "~**~" + "\n")