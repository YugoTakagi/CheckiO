import numpy as np

def checkio(password):
    #replace this for solution
    flag1=False
    flag2=False
    flag3=False
    flag4=False
    if len(password)>=10:
        flag1 = True 
    for i in np.arange(len(password)):   
        if str.isdigit(password[i]):
            flag2 = True
            break
    for i in np.arange(len(password)):
        if str.islower(password[i]):
            flag3 = True
            break
    for i in np.arange(len(password)):
        if str.isupper(password[i]):
            flag4 = True
            break
    if flag1==True and flag2==True and flag3==True and flag4==True:
        return True
    else:
        return False

if __name__ == '__main__':
    checkio('A217048nskogakuin')
