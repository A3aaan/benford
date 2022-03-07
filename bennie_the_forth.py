from random import randint
from math import sqrt
from math import log10
from matplotlib import pyplot as plt

"""
ga na of het eerste digit van een getal gelijk is aan n
"""
def first_digit_equals(n):
    return lambda number: str(number)[0] == str(n)

"""
tel hoeveel elementen voldoen aan een bepaald criterium dat geevalueerd wordt door de evaluatie_ftie
"""
def count(evaluatie_ftie,iterable):
    return len(tuple(filter(lambda x: evaluatie_ftie(x),iterable)))

"""
creeert een lijst van lengte n met soort van willekeurige getallen 
ipv gewn een printstatement te zetten is er een printende functie meegegeven om te zien wanneer de lijst klaar is
de waarde voor repeat geeft weer hoe vaak er een getal gekozen wordt binnen de range die het vorige willekeurige getal was
dit wordt uitgevoerd door de number in repeated range functie
"""
def generate_random_data(lengte,repeat=-1,logger=lambda x:print(x)):
    data = list()
    if repeat ==-1:
        logger("started making up data*")
        for _ in range(lengte):
            data.append(randint(0,randint(0,randint(0,10**20))))
        logger("data created")
    else:
        logger("started making up data**")
        for _ in range(lengte):
            data.append(number_in_repeated_range(repeat))
        logger("data created")
    return data

def number_in_repeated_range(n, nummer = 10**20):
    if n == 0: return nummer
    return number_in_repeated_range(n-1,randint(0,nummer))

"""
Deze functie maakt gebruik van de vorige functies om in een niet zo heel willekeurige lijst getallen het aantal getallen
dat met 1,2,3 enz begint te tellen
"""
def the_benford_numbers(data):
    return [("#",str(x),count(first_digit_equals(x),data)) for x in range(1,10)]

"""
doet hetzelfde als de benford_numbers maar geeft percentages terug
"""
def the_benford_percentages(data):
    return [round(count(first_digit_equals(x),data)*100/len(data),2) for x in range(1,10)]



"""
dit is een methode om eeh getalwaarde te geven aan hoe hard lijsten verschillen
0 is een perfecte gelijkenis 
100 is (gezien met % gewerkt wordt) het grootst mogelijke (hier onmogelijk) verschil
"""
def kwadratisch_verschil(lijst_1,lijst_2):
    return sqrt(sum((lijst_1[x]-lijst_2[x])**2 for x in range(len(lijst_1)))/len(lijst_1))

"""
dit zijn de originele getallen zoals beschreven in de wet van bennie ford
"""
benfords_percentages = [30.1,17.6,12.5,9.7,7.9,6.7,5.8,5.1,4.6]
benfords_echte_percentages = [log10((1+x)/x)*100 for x in range(1,10)]

########################################################################################################################
# analyseer de resultaten
########################################################################################################################


experimentele_percentages = the_benford_percentages(generate_random_data(1000000,3))
print(experimentele_percentages, "\n",
      benfords_percentages, "\n",
      kwadratisch_verschil(experimentele_percentages,benfords_echte_percentages))


"""herhalingen , afwijking = [], []

for x in range(3,10,2):
    print(x)
    herhalingen.append(x)
    experimentele_percentages = the_benford_percentages(generate_random_data(1000000, x))
    afwijking.append(kwadratisch_verschil(experimentele_percentages,benfords_echte_percentages))

plt.plot(herhalingen,afwijking,'ro-')
plt.title("benadering van benford")
plt.xlabel("herhalingen van het kiesdomein")
plt.ylabel("afwijking")
plt.show()
"""


########################################################################################################################
# eindconclusie
"""
hoe meer herhalingen hoe beter benford benaderd wordt indien de range van waaruit gekozen mag worden maar groot genoeg is
indien deze range echter te klein is zullenn uiteindelijk alle getallen == 0 worden wat geen relevante info oplevert
"""
########################################################################################################################
