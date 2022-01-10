import weakref
import gc

class Item:
    instances = []
    def __init__(self, x):
        self.x = x
##        self.__class__.instances.append(weakref.proxy(self))
        self.__class__.instances.append(self)

##    @classmethod
##    def get_instances(cls):
##        for inst_ref in cls.__refs__[cls]:
##            inst = inst_ref()
##            if inst is not None:
##                yield inst

item1 = Item(5)
item2 = Item(6)
item3 = Item(7)

for i in Item.instances:
    print (i.x)

for i in gc.get_objects():
    if isinstance(i, Item):
        print (i.x)

    

    
