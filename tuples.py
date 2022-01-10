from collections import namedtuple


Country = namedtuple('Country', ['population', 'capital', 'area'])

Germany = Country(80, 'Berlin', 250)
France = Country(65, "Paris", 650)


print (Germany.population)
print (Germany.capital)
print (Germany[1])
print (Germany.area)
print (France.population)
print (France.capital)
print (France.area)


                     


