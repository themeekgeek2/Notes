def mfunc(): # put the dictionary within the function instead of creating a global var
    return {'mafumafu':0,'soraru':1,'amatsuki':2,'araki':3,'ado':4,'eve':5,'uratanuki':5,'reol':6}
    
utaite=mfunc() # this gets the key
print(utaite['eve'])

def sfunc(k): # retrieves key from the dictionary to get the value
    # restating the dictionary within this func scope
    #mdict={'mafumafu':0,'soraru':1,'amatsuki':2,'araki':3,'ado':4,'eve':5,'uratanuki':5,'reol':6}
    sdict={1:'mafu',2:'sora',3:'ura'}
    return sdict[k]
    
print(sfunc(1))
    
    

    

    