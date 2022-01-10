def print_deep (item):
    if isinstance (item, list):
        for i in item:
            print_deep(i)
    else:
        print(item)


l = [1, 2, 3, [4, 5, [7, 8, 9]]]
print_deep(l)

'''

print_deep("hello")
print("-----------------------------")
print_deep(["item1", "item2", "item3"])
print("-----------------------------")
l1 = ["apple1", "apple2"]
l2 = ["pear1", "pear2", "pear3"]
l3 = ["orange1", "orange2"]
l4 = ["tree"]
l5 = 1968
l = [l1, l2, l3, l4, l5]
print_deep(l)
print("-----------------------------")
l6 = [l2, l3]
l = [l6, l4, l5]
print_deep(l)
'''

