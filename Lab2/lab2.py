import numpy as np
import hamiltonian
import shutil
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--n',required=True)
parser.add_argument('--J',required=True)
parser.add_argument('--beta',required=True)
parser.add_argument('--B',required=True)
parser.add_argument('--liczbaKrokow',required=True)
parser.add_argument('--gestSpin',required=False,default=0.5)
parser.add_argument('--obr',type=str,default='test',required=False)
parser.add_argument('--anim',type=str,default='test',required=False)
parser.add_argument('--magn',type=str,default='',required=False)
args = parser.parse_args()

N=int(args.n)
#M=300
S=np.ones((N,N))
Hstart=0
J=float(args.J)
B=float(args.B)
beta=float(args.beta)
wypelnienie=float(args.gestSpin)
par=int(args.liczbaKrokow)
iloscKrokSym=int(N*N*par)
Mag=[]
nazwaObrazki=args.obr
nazwaAnimacja=args.anim
nazwaMag=args.magn
#nazwaMag='magnetyzacja.txt'
try:
    shutil.rmtree("C:\PW\WstDoPythona\lab2\wyniki")
except OSError:
    pass
ham=hamiltonian.H(S,N,J,B,wypelnienie,Hstart,Mag,iloscKrokSym,beta,nazwaObrazki,nazwaAnimacja)
h=ham.licz(Hstart)
if(nazwaMag!=''):
    with open(nazwaMag, 'w',encoding="utf-8") as f:
        tekst='Numer_kroku'+'\t'+'Magnetyzacja'+'\n'
        f.write(tekst)
        for i in range(len(Mag)):
            tekst=str(i)+'\t'+str(Mag[i])+'\n'
            f.write(tekst)

print("koniec")