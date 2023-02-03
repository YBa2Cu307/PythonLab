import numpy as np
import tqdm
from PIL import Image
import os
class H:
    def __init__(self,S,N,J,B,wypelnienie,Hstart,Mag,iloscKrokSym,beta,nazwaObrazki,nazwaAnimacja):
        self.S=S
        #self.H=H
        self.N=N
        #self.M=M
        self.J=J
        self.B=B
        self.wypelnienie=wypelnienie
        self.Hstart=Hstart
        self.Mag=Mag
        self.iloscKrokSym=iloscKrokSym
        self.beta=beta
        self.nazwaObrazki=nazwaObrazki
        self.nazwaAnimacja=nazwaAnimacja
    def Hamiltonian(self,x,y,H):
        if(x==-1):
            for i in range(self.N):
                for j in range(self.N):
                    if(i==self.N-1):
                        if(j==self.N-1):
                            H+=-self.J/2*(self.S[i][j]*self.S[i-1][j]+self.S[i][j]*self.S[0][j]+self.S[i][j]*self.S[i][j-1]+self.S[i][j]*self.S[i][0])-self.B*self.S[i][j]
                        else:
                            H+=-self.J/2*(self.S[i][j]*self.S[i-1][j]+self.S[i][j]*self.S[0][j]+self.S[i][j]*self.S[i][j-1]+self.S[i][j]*self.S[i][j+1])-self.B*self.S[i][j]
                    elif(j==self.N-1):
                        H+=-self.J/2*(self.S[i][j]*self.S[i-1][j]+self.S[i][j]*self.S[i+1][j]+self.S[i][j]*self.S[i][j-1]+self.S[i][j]*self.S[i][0])-self.B*self.S[i][j]
                    else:
                        H+=-self.J/2*(self.S[i][j]*self.S[i-1][j]+self.S[i][j]*self.S[i+1][j]+self.S[i][j]*self.S[i][j-1]+self.S[i][j]*self.S[i][j+1])-self.B*self.S[i][j]
        else:
            if(x==self.N-1):
                if(y==self.N-1):
                    H-=-self.J/2*(self.S[x][y]*self.S[x-1][y]+self.S[x][y]*self.S[0][y]+self.S[x][y]*self.S[x][y-1]+self.S[x][y]*self.S[x][0])-self.B*self.S[x][y]
                    H+=self.J/2*(self.S[x][y]*self.S[x-1][y]+self.S[x][y]*self.S[0][y]+self.S[x][y]*self.S[x][y-1]+self.S[x][y]*self.S[x][0])+self.B*self.S[x][y]
                else:
                    H-=-self.J/2*(self.S[x][y]*self.S[x-1][y]+self.S[x][y]*self.S[0][y]+self.S[x][y]*self.S[x][y-1]+self.S[x][y]*self.S[x][y+1])-self.B*self.S[x][y]
                    H+=self.J/2*(self.S[x][y]*self.S[x-1][y]+self.S[x][y]*self.S[0][y]+self.S[x][y]*self.S[x][y-1]+self.S[x][y]*self.S[x][y+1])+self.B*self.S[x][y]
            elif(y==self.N-1):
                H-=-self.J/2*(self.S[x][y]*self.S[x-1][y]+self.S[x][y]*self.S[x+1][y]+self.S[x][y]*self.S[x][y-1]+self.S[x][y]*self.S[x][0])-self.B*self.S[x][y]
                H+=self.J/2*(self.S[x][y]*self.S[x-1][y]+self.S[x][y]*self.S[x+1][y]+self.S[x][y]*self.S[x][y-1]+self.S[x][y]*self.S[x][0])+self.B*self.S[x][y]
            else:
                H-=-self.J/2*(self.S[x][y]*self.S[x-1][y]+self.S[x][y]*self.S[x+1][y]+self.S[x][y]*self.S[x][y-1]+self.S[x][y]*self.S[x][y+1])-self.B*self.S[x][y]
                H+=self.J/2*(self.S[x][y]*self.S[x-1][y]+self.S[x][y]*self.S[x+1][y]+self.S[x][y]*self.S[x][y-1]+self.S[x][y]*self.S[x][y+1])+self.B*self.S[x][y]
        return H
    def start(self):
        for i in range(self.N*self.N):
            los=np.random.random()
            losX=np.random.randint(0,self.N-1)
            losY=np.random.randint(0,self.N-1)
            if(los<self.wypelnienie):
                self.S[losX][losY]=-1*self.S[losX][losY]
        return self.S
    def licz(self,Hstart):
        images=[]
        self.S=self.start()
        H=self.Hamiltonian(-1,-1,Hstart)
        self.Mag.append(np.sum(self.S)/(self.N*self.N))
        print("obliczenia")
        for i in tqdm.tqdm(range(self.iloscKrokSym)):
            tymczasowa=H
            los=np.random.random()
            losX=np.random.randint(0,self.N-1)
            losY=np.random.randint(0,self.N-1)
            tymczasowa2=self.Hamiltonian(losX,losY,tymczasowa)
            if(tymczasowa2<tymczasowa):
                self.S[losX][losY]=-1*self.S[losX][losY]
                H=tymczasowa2
            else:
                pstwo=np.exp((-(tymczasowa2-tymczasowa))*self.beta)
                if(pstwo<los):
                    self.S[losX][losY]=-1*self.S[losX][losY]
                    H=tymczasowa2
            self.Mag.append(np.sum(self.S)/(self.N*self.N))
            if(self.nazwaObrazki!='test'):
                arr=np.zeros((self.N,self.N))
                for i in range(self.N):
                    for j in range(self.N):
                        if(self.S[i][j]==-1):
                            arr[i][j]=0
                        else:
                            arr[i][j]=255
                arr=arr.astype(np.uint8)
                img=Image.fromarray(arr)
                #img.thumbnail((1000,1000),Image.Resampling.LANCZOS)
                img=img.resize((200,200),Image.Resampling.LANCZOS)
                images.append(img)
        try:
            path=os.path.join("C:\PW\WstDoPythona\lab2","wyniki")
            os.mkdir(path)
            os.chdir("C:\PW\WstDoPythona\lab2\wyniki")
        except OSError:
            pass  
        if(self.nazwaObrazki!='test'):
            print("zapis zdjec")
            for im in tqdm.tqdm(range(len(images))):
                tekst=self.nazwaObrazki+str(im+1)+'.png'
                images[im].save(tekst)  
        if(self.nazwaObrazki!='test' and self.nazwaAnimacja!='test'):
            tekst2=self.nazwaAnimacja+'.gif'
            images[0].save(tekst2,save_all=True,append_images=images[1:])
        return 0