'''
def two_teams(sailors):
    #replace this for solution
    #print(list(sailors.values()))
    #print(list(sailors.keys()))
    value = list(sailors.values())
    key = list(sailors.keys())
    ship1 = [key[i] for i in range(len(value)) if value[i]>40 or value[i]<20]
    ship2 = [key[i] for i in range(len(value)) if value[i]<=40 and value[i]>=20]
    #print(ship1)
    #print(ship2)
    stShip1 = sorted(ship1)
    stShip2 = sorted(ship2)
    
    #print(stShip1)
    #print(stShip2)
    return [stShip1,stShip2]
#'''
def two_teams(sailors):
    ship1 = sorted( [key for key, value in sailors.items() if value>40 or value<20])
    ship2 = sorted([key for key, value in sailors.items() if value<=40 and value>=20])
    return [ship1,ship2]
if __name__ == "__main__":
    two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19})
