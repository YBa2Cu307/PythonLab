import numpy as np
import numba

def Hamiltonian(x,y,H,N,S,J,B):
        if(x==-1):
            for i in range(N):
                for j in range(N):
                    if(i==N-1):
                        if(j==N-1):
                            H+=-J/2*(S[i][j]*S[i-1][j]+S[i][j]*S[0][j]+S[i][j]*S[i][j-1]+S[i][j]*S[i][0])-B*S[i][j]
                        else:
                            H+=-J/2*(S[i][j]*S[i-1][j]+S[i][j]*S[0][j]+S[i][j]*S[i][j-1]+S[i][j]*S[i][j+1])-B*S[i][j]
                    elif(j==N-1):
                        H+=-J/2*(S[i][j]*S[i-1][j]+S[i][j]*S[i+1][j]+S[i][j]*S[i][j-1]+S[i][j]*S[i][0])-B*S[i][j]
                    else:
                        H+=-J/2*(S[i][j]*S[i-1][j]+S[i][j]*S[i+1][j]+S[i][j]*S[i][j-1]+S[i][j]*S[i][j+1])-B*S[i][j]
        else:
            if(x==N-1):
                if(y==N-1):
                    H-=-J/2*(S[x][y]*S[x-1][y]+S[x][y]*S[0][y]+S[x][y]*S[x][y-1]+S[x][y]*S[x][0])-B*S[x][y]
                    H+=J/2*(S[x][y]*S[x-1][y]+S[x][y]*S[0][y]+S[x][y]*S[x][y-1]+S[x][y]*S[x][0])+B*S[x][y]
                else:
                    H-=-J/2*(S[x][y]*S[x-1][y]+S[x][y]*S[0][y]+S[x][y]*S[x][y-1]+S[x][y]*S[x][y+1])-B*S[x][y]
                    H+=J/2*(S[x][y]*S[x-1][y]+S[x][y]*S[0][y]+S[x][y]*S[x][y-1]+S[x][y]*S[x][y+1])+B*S[x][y]
            elif(y==N-1):
                H-=-J/2*(S[x][y]*S[x-1][y]+S[x][y]*S[x+1][y]+S[x][y]*S[x][y-1]+S[x][y]*S[x][0])-B*S[x][y]
                H+=J/2*(S[x][y]*S[x-1][y]+S[x][y]*S[x+1][y]+S[x][y]*S[x][y-1]+S[x][y]*S[x][0])+B*S[x][y]
            else:
                H-=-J/2*(S[x][y]*S[x-1][y]+S[x][y]*S[x+1][y]+S[x][y]*S[x][y-1]+S[x][y]*S[x][y+1])-B*S[x][y]
                H+=J/2*(S[x][y]*S[x-1][y]+S[x][y]*S[x+1][y]+S[x][y]*S[x][y-1]+S[x][y]*S[x][y+1])+B*S[x][y]
        return H
def start(N,wypelnienie,S):
        for i in range(N*N):
            los=np.random.random()
            losX=np.random.randint(0,N-1)
            losY=np.random.randint(0,N-1)
            if(los<wypelnienie):
                S[losX][losY]=-1*S[losX][losY]
        return S
def licz(Hstart,Mag,iloscKrokSym,N,beta,J,B,S_Start,wypelnienie):
        S=start(N,wypelnienie,S_Start)
        H=Hamiltonian(-1,-1,Hstart,N,S,J,B)
        Mag.append(np.sum(S)/(N*N))
        print("obliczenia")
        for i in range(iloscKrokSym):
            tymczasowa=H
            los=np.random.random()
            losX=np.random.randint(0,N-1)
            losY=np.random.randint(0,N-1)
            tymczasowa2=Hamiltonian(losX,losY,tymczasowa,N,S,J,B)
            if(tymczasowa2<tymczasowa):
                S[losX][losY]=-1*S[losX][losY]
                H=tymczasowa2
            else:
                pstwo=np.exp((-(tymczasowa2-tymczasowa))*beta)
                if(pstwo<los):
                    S[losX][losY]=-1*S[losX][losY]
                    H=tymczasowa2
            Mag.append(np.sum(S)/(N*N))
        return 0
@numba.njit
def licz_numba(H,iloscKrokSym,N,beta,J,B,S,wypelnienie):
        for i in range(N*N):
            los=np.random.random()
            losX=np.random.randint(0,N-1)
            losY=np.random.randint(0,N-1)
            if(los<wypelnienie):
                S[losX][losY]=-1*S[losX][losY]
        for i in range(N):
            for j in range(N):
                if(i==N-1):
                    if(j==N-1):
                        H+=-J/2*(S[i][j]*S[i-1][j]+S[i][j]*S[0][j]+S[i][j]*S[i][j-1]+S[i][j]*S[i][0])-B*S[i][j]                        
                    else:
                        H+=-J/2*(S[i][j]*S[i-1][j]+S[i][j]*S[0][j]+S[i][j]*S[i][j-1]+S[i][j]*S[i][j+1])-B*S[i][j]
                elif(j==N-1):
                    H+=-J/2*(S[i][j]*S[i-1][j]+S[i][j]*S[i+1][j]+S[i][j]*S[i][j-1]+S[i][j]*S[i][0])-B*S[i][j]
                else:
                    H+=-J/2*(S[i][j]*S[i-1][j]+S[i][j]*S[i+1][j]+S[i][j]*S[i][j-1]+S[i][j]*S[i][j+1])-B*S[i][j]
        print("obliczenia")
        for i in range(iloscKrokSym):
            tymczasowa=H
            los=np.random.random()
            x=np.random.randint(0,N-1)
            y=np.random.randint(0,N-1)
            tymczasowa2=H
            if(x==N-1):
                if(y==N-1):
                    tymczasowa2-=-J/2*(S[x][y]*S[x-1][y]+S[x][y]*S[0][y]+S[x][y]*S[x][y-1]+S[x][y]*S[x][0])-B*S[x][y]
                    tymczasowa2+=J/2*(S[x][y]*S[x-1][y]+S[x][y]*S[0][y]+S[x][y]*S[x][y-1]+S[x][y]*S[x][0])+B*S[x][y]
                else:
                    tymczasowa2-=-J/2*(S[x][y]*S[x-1][y]+S[x][y]*S[0][y]+S[x][y]*S[x][y-1]+S[x][y]*S[x][y+1])-B*S[x][y]
                    tymczasowa2+=J/2*(S[x][y]*S[x-1][y]+S[x][y]*S[0][y]+S[x][y]*S[x][y-1]+S[x][y]*S[x][y+1])+B*S[x][y]
            elif(y==N-1):
                tymczasowa2-=-J/2*(S[x][y]*S[x-1][y]+S[x][y]*S[x+1][y]+S[x][y]*S[x][y-1]+S[x][y]*S[x][0])-B*S[x][y]
                tymczasowa2+=J/2*(S[x][y]*S[x-1][y]+S[x][y]*S[x+1][y]+S[x][y]*S[x][y-1]+S[x][y]*S[x][0])+B*S[x][y]
            else:
                tymczasowa2-=-J/2*(S[x][y]*S[x-1][y]+S[x][y]*S[x+1][y]+S[x][y]*S[x][y-1]+S[x][y]*S[x][y+1])-B*S[x][y]
                tymczasowa2+=J/2*(S[x][y]*S[x-1][y]+S[x][y]*S[x+1][y]+S[x][y]*S[x][y-1]+S[x][y]*S[x][y+1])+B*S[x][y]
            if(tymczasowa2<tymczasowa):
                S[x][y]=-1*S[x][y]
                H=tymczasowa2
            else:
                pstwo=np.exp((-(tymczasowa2-tymczasowa))*beta)
                if(pstwo<los):
                    S[x][y]=-1*S[x][y]
                    H=tymczasowa2
        return 0
