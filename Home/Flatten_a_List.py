'''
from itertools import chain
import collextions
def flat_list(array):
    result = []
    for element in array:
        if isinstance(element, collections.Iterable) and not isinstance(element, str):
            result.extend(flat_list(element))
        else:
            result.append(element)
    return result
'''
def flat_list(array):
    l = []
    m = [array]

    while len(m) > 0:
        node = m.pop(0)
        if isinstance(node, list):
            m = node + m
        else:
            l.append(node)
    return l
'''








    while True:
        if type(array) is list:
            *lis = array
            a


    for i, e in enumerate(array):
        while True:
            if type(e) is list:
                for f in e:
                    if type(f) is not list:
                        l.extend(f)
                    else:
                        
            else:
                l.extend(e)
                break

    

    for i, e in enumerate(array):
        print("{}: {}".format(i, e))
        if type(e) is list:
            l.extend(flat_list(e))
        else:
            l.extend(e)
    print(l)
    return l
'''
if __name__ == "__main__":
    print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))
