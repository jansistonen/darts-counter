# tehdään skirpti joka tallentaa darts tuloksia, 3 heittoa / vuoro
# jatketaan siten että lasketaan keskiarvo 'vapaalta kierrokselta'
# nyt pisteet tallentuu vain ohjelmaan muttei tiedostoon, opetellaan tallentamaan kaikki json-filuun

import json
import os
from datetime import datetime

data = {
    'sessio_id' : 'sessio1',
    'kierrokset' : 0,
    'kierros' : [],
    'kierroksien_ka' : 0,
    'heitetyt_tikat': 0
}

FILENAME = "sessions.json"

now = datetime.now()
timestamp = now.strftime("%d/%m/%Y-%H:%M:")

# 1. Lue vanha data (tai luo uusi)
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        all_data = json.load(f)
else:
    all_data = {"sessiot": []}

# 2. Luo uusi sessio
uusi_sessio = {
    "sessio_id": "sessio" + timestamp,
    "kierros": [],
    "kierrokset": data["kierrokset"],
    "session_ka": 0
}

all_data["sessiot"].append(uusi_sessio)

json_str = json.dumps(data, indent=4)
with open('sample.json', 'w') as f:
    f.write(json_str)



kierroksia = 0
lista_per_kierros = []
lista_kierroksen_tulos = []
jatka = True

def kierros_count(para1):
    summa = 0
    for num in para1:
        summa = summa + num
    #return summa / (len(para1)) #funktio palauttaa keskiarvon, joka tallennetaan toiseen listaan! HUOM. ka/ per tikka
    return summa

def kierros_lista_läpikäynti(para2):
    #jotain lissää
    sum = 0
    for turn in lista_kierroksen_tulos:
        sum = sum + turn
    if sum == 0:
        return None
    return sum / len(lista_kierroksen_tulos)

while jatka:
    #syötä täällä heittosi
    print('Q lopettaa kieroksen')
    heitto1 = input('Kierros: ')
    if heitto1 == '':
        heitto1 = 0
    '''heitto2 = input('Tikka 2: ')
    if heitto2 == '':
        heitto2 = 0
    heitto3 = input('Tikka 3: ')
    if heitto3 == '':
        heitto3 = 0'''
    #if heitto1 == 'q' or heitto2 == 'q' or heitto3 == 'q':
    if heitto1 == 'q':
        print('päätit lopettaa')
        break
    lista_per_kierros.append(int(heitto1))
    #lista_per_kierros.append(int(heitto2))
    #lista_per_kierros.append(int(heitto3))
    lista_kierroksen_tulos.append(kierros_count(lista_per_kierros))
    print('Vuoro heitetty!!!')
    lista_per_kierros.clear()
    print(f'Olet heittänyt {kierroksia} vuoroa')
    kierroksia += 1
    uusi_sessio['kierros'] = uusi_sessio['kierros'] + [int(heitto1)]

print(f'Lopetit heittovuoron. Heitit yhteensä {kierroksia} kierrosta!')
print(lista_kierroksen_tulos)
print('Session keskiarvo: ', kierros_lista_läpikäynti(lista_kierroksen_tulos))

uusi_sessio['kierrokset'] = kierroksia
uusi_sessio['session_ka'] = kierros_lista_läpikäynti(lista_kierroksen_tulos)

with open(FILENAME, "w") as f:
    json.dump(all_data, f, indent=4)



#TODO 
# - Aloita kierros 
# - Lopeta kierros 
# - Pelimuoto: 
# - Vapaa heittely 
# - 301/501 
# - Kellotaulu

