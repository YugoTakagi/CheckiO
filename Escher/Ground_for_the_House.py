import numpy as np
def house(plan):
    #replace this for solution
    print(plan)
    h=0
    w=0
    row=[]
    col=[]
    i = [i for i in range(len(plan)) if plan[i]=='\n']
    wb = i[1]-i[0]
    for line in range(len(i)):
        l = plan[wb *line:wb *(line +1)]
        li = list(l)
        row.append([val for val in li if val!="\n"])
    
    print(row)
    for i in range(len(row)):
        for j in range(len(row[i])):
            if row[i][j]=='#':
                h +=1
                break
    array = np.array(row)
    print(array)
    print(wb -1)
    if array[0] == []:
        array = np.delete(array, 0, 0)
    for i in range(wb-1):
        print(array[:,i])
        col.append(array[:,i])
    for i in range(len(col)):
        for j in range(len(col[i])):
            if col[i][j]=='#':
                w +=1
                break
    print(w*h)
    return h*w

if __name__ == '__main__':
	house('''
0000000
##00##0
######0
##00##0
#0000#0
''')
