class Martian:
    """ this is a test """
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln

    def __setattr__(self, name, value):
        # print(f">>> You set {name} = {value}")
        self.__dict__[name] = value

    def __getattr__(self, name):
        # print(f">>> Get the '{name}' attribute")
        if name == 'full_name':
            return f"{self.first_name} {self.last_name}"
        else:
            raise AttributeError(f"No attribute named {name}")
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __lt__(self, other):
        print (f"Comparing {self} with {other}")
        if self.last_name != other.last_name:
            return (self.last_name < other.last_name)
        else:
            return (self.first_name < self.last_name)

m1 = Martian('Stephan', 'Schirrecker')
m2 = Martian ('Alois', 'Schirrecker')
m3 = Martian ('John', 'Doe')
m1.arrival_date = "2021-08-10"

# print (dir(m1))
# print (f"First name = {m1.first_name}")
# print (f"Last name = {m1.last_name}")
# print (f"Full name = {m1.full_name}")
# print (m1.__dict__)

# print (m1)
# same as print (m1.__str())
# print(id(m1))   id = decimal value of HEX object address in cpython
# check https://docs.python.org/3/reference/datamodel.html

martians = [m1, m2, m3]
martians.sort()
for m in martians:
    print (m)
    
