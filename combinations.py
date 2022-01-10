import itertools
def bananas(s):
    result = []
    length = len("banana")
    if len(s) < length:
        return ([])
    if s == "banana":
        print (s)
        return (['banana'])
    index_list = list(range(0, len(s)))
    combos = list(itertools.combinations(index_list, len(s)-length))
    for remove_list in combos:
        s_list = list(s)
        for index in remove_list:
            s_list[index] = '-'
        new_str = ''.join(s_list)
        test_str = new_str.replace('-', '')
        if test_str == "banana":
            result.append(new_str)
            print(new_str)
    return result
    
##bananas("bbannanana")
##print ("----------------")
##bananas("banana")
##print ("----------------")
bananas("bbananana")



##    for n in range(1, 1 + len(s)- length):
##        combos = list(itertools.combinations(index_list, n))
##        ## print(combos)
##        for remove_list in combos:
##            s_list = list(s)
##            for index in remove_list:
##                s_list[index] = '-'
##            new_str = ''.join(s_list)
##            test_str = new_str.replace('-', '')
##            ## print(new_str)
##            ## print (test_str)
##            if test_str == "banana":
##                result.append(new_str)
##                print(new_str)
