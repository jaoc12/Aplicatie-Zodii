import requests
import bs4
import time
from datetime import date
data = date.today()
data = data.strftime('%d/%m/%Y')
zodii = ['Berbec', 'Taur', 'Gemeni', 'Rac', 'Leu', 'Fecioara',
         'Balanta', 'Scorpion', 'Sagetator', 'Capricorn',
         'Varsator', 'Pesti']
for zodie in zodii:
    zodie = zodie.lower()
    url = 'https://www.horoscop.ro/' + zodie
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('p')
    azi = str(elems[0])
    azi = azi[3:-4]
    fisier = r'.\lib\Zodii' + '\\' + zodie + '.txt'
    f = open(fisier, "w", encoding = "utf-8")
    f.write("Horoscop " + zodie.capitalize() + " " + data + ":\n")
    text = azi.split('. ')
    for line in text:
        if(line.find('.') == -1):
            f.write(line + ".\n")
        else:
            f.write(line + "\n")
    f.close()
    time.sleep(2)