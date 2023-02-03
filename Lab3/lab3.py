import numpy as np
from numpy import linalg as LA
import functools
import time

daneStat=[100,0,0,0,0,0]#min,max,avar,iterator,biezacy czas,wybor
def dekorator(st):
    def dekoratorWew(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if(st[5]==0):
                startTime=time.time()
                func(*args, **kwargs)
                daneStat[4]=(time.time()-startTime)
                if(daneStat[4]<daneStat[0]):
                    daneStat[0]=daneStat[4]
                if(daneStat[4]>daneStat[1]):
                    daneStat[1]=daneStat[4]
                daneStat[2]=(daneStat[2]*daneStat[3]+daneStat[4])/(daneStat[3]+1)
                daneStat[3]+=1
                daneStat[4]=0
            else:
                print("minimalny czas wykonania funkcji: ",daneStat[0]," s")
                print("maksymalny czas wykonania funkcji: ",daneStat[1]," s")
                print("sredni czas wykonania funkcji: ",daneStat[2]," s")    
        return wrapper
    return dekoratorWew
    
@dekorator(daneStat)
def czasochlonnaFunkcja():
    N=200
    macierz=np.random.rand(N,N)
    e,v=LA.eig(macierz)
@dekorator(daneStat)
def funkcjaTest():
    pass
for i in range(100):
    czasochlonnaFunkcja()
daneStat[5]=1
funkcjaTest()
