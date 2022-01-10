countries = [ ("France", 60, "Paris"),
              ("Germany", 80, "Berlin"), 
               ("UK", 70, "London")
            ]

# size = lambda list: list[1]

def size(t):
    return t[1]

print(countries)
countries.sort(key=size)
print(countries)
