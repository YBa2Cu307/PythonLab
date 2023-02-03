import numpy as np
import hamiltonian as ham
import time

N=100
S=np.ones((N,N))
Hstart=0
J=1.5
B=1
beta=0.5
wypelnienie=0.3
par=100
iloscKrokSym=int(N*N*par)
Mag=[]

time_start=time.time()
h=ham.licz(Hstart,Mag,iloscKrokSym,N,beta,J,B,S,wypelnienie)
time_stop=time.time()
print("czas wykonania kodu bez numby:", time_stop-time_start,"s")
time_start=time.time()
h=ham.licz_numba(Hstart,iloscKrokSym,N,beta,J,B,S,wypelnienie)
time_stop=time.time()
print("czas wykonania kodu z numbą:", time_stop-time_start,"s")
print("koniec")