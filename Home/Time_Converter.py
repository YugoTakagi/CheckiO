####note###################################################
# time.split(':')で分けられた
# suffix = "p.m." if int(nums[0])>11 else "a.m."は初めて見た
# h, m = map(int, time.split(':')) #map()って何？
###########################################################
def time_converter(time):
    #replace this for solution
    box = [t for t in time if t != ":"]
    print(box)
    hour = box[:2]
    minite = box[2:4]
    print(hour, minite)
    h = ''.join(hour)
    m = ''.join(minite)
    print(h)
    if int(h)>=13:
        print(int(h) - 12)
        h = str(int(h) - 12)
        t=[]
        t.extend(h)
        t.extend(':')
        t.extend(m)
        t.extend(" p.m.")
    elif int(h)==0:
        t=[]
        t.extend('12')
        t.extend(':')
        t.extend(m)
        t.extend(" a.m.")
    elif int(h)==12:
        t=[]
        t.extend(h)
        t.extend(':')
        t.extend(m)
        t.extend(" p.m.")
    elif int(h)<10:
        t=[]
        t.extend(h[1])
        t.extend(':')
        t.extend(m)
        t.extend(" a.m.")
    else:
        t=[]
        t.extend(h)
        t.extend(':')
        t.extend(m)
        t.extend(" a.m.")
    ans = ''.join(t)
    #print(ans)
    return ans
if __name__ == '__main__':
    time_converter('12:30')
