####note##############################################
#return sorted(items, key=lambda i: (-items.count(i), items.index(i)))
######################################################
import collections
'''
def frequency_sort(items):
    # your code here
    if len(items) == 0:
        return []
    ans=[]
    clt = collections.Counter(items)
    clt.most_common()
    values, counts = zip(*clt.most_common())
    for j in range(len(values)):
        ans.extend([i for i in items if i==values[j]])
    return ans
#'''
def frequency_sort(items):
    ####lambda no imi############
    #test = lambda x : x**2
    #print(test(3))
    #############################
    ####sorted no kakinata#######
    #l=[["バームクーヘン",3],["コーヒー",1],["misterDonut",2]]
    #sortedL = sorted(l, key=lambda x: x[1])
    #print(sortedL)
    #############################
    #############################
    #for i in items:
    #    #list.items(x) -> x no saisho no index
    #    print("{}> {}, {}".format(i, -items.count(i),items.index(i)))
    #    test2 = lambda i: (-items.count(i), items.index(i))
    #    print("test2 = {}\n".format(test2(i)))
    #############################

    return sorted(items, key=lambda i: (-items.count(i), items.index(i)))
if __name__ == '__main__':
    ans=frequency_sort([4,4,4,4,3,3,5,6,7,2,2,4,6,7,4,3,6,7,8,4,35,6,9])
    print(ans)
