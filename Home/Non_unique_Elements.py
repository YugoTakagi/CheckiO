####note###################################################
#return [i for i in data if data.count(i) > 1]
###########################################################
#Your optional code here
#You can import some modules or create additional functions


def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.  
    count = [data.count(data[i]) for i in range(len(data))]
    index = [i for i in range(len(count)) if count[i]==1]
    nai = 0
    for i in index:
        data.pop(i -nai)
        nai += 1
    #replace this for solution
    return data

if __name__ == '__main__':
    d = checkio([1,2,3,4,5])
    print(d)
