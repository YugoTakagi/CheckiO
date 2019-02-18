####note#############################################
#def house(plan):
#    grounds = [(i, j) for i, row in enumerate(plan.split()) for j, cell in enumerate(row) if cell == '#']
#    if not grounds:
#        return 0
#    xs, ys = zip(*grounds)
#    return (xs[-1] - xs[0] + 1) * (max(ys) - min(ys) + 1)
#
#
def house(plan):
    if '#' not in plan:
        return 0
    grid = plan.split()
    no_so, east, west = [], [], []
    for index, line in enumerate(grid):
        if '#' in line:
            no_so.append(index)
            east.append(line.find('#'))
            west.append(line.rfind('#'))
    return (max(no_so) - min(no_so) + 1) * (max(west) - min(east) + 1)
#grid = plan.split() == grid = plan.split('\n')
def note():
    l=[1,2,3,4,5]
    for i, value in enumerate(l):#enumerate(list) -> index, value?
        print("i, value = {}, {}".format(i,value))
    for i, value in enumerate(l, 22):#enumerate(list) -> index, value?
        print("i, value = {}, {}".format(i,value))
#####################################################
import numpy as np
def vhouse(plan):
    pass
def myhouse(plan):
    #replace this for solution
    h,w=[],[]
    splan = plan.split('\n')
    nsplan=[list(splan[i]) for i in range(len(splan)) if splan[i] != '']
    nplist=np.array(nsplan)
    for i in range(len(nplist)):
        for j in range(len(nplist[i])):
            if nplist[i][j] == "#":
                h.append(i)
                break
    for i in range(len(nplist[0])):
        col = nplist[:,i]
        for j in range(len(col)):
            if col[j]=='#':
                w.append(i)
                break
    if len(h) != 0:
        nh = [i for i in range(h[0],h[len(h)-1] +1,1)]
    else:
        nh = []
    if len(w) != 0:
        nw = [i for i in range(w[0],w[len(w)-1] +1,1)]
    else:
        nw = []
    return len(nh)*len(nw)
if __name__ == '__main__':
    note()
    s1 = house('''
0##0
0000
#00#
''')
    s = vhouse('''0000
0000
''')
    print(s1)
