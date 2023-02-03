import argparse
from ascii_graph import Pyasciigraph


parser = argparse.ArgumentParser()
parser.add_argument('--nazwaPliku',required=True)
parser.add_argument('--wielkoscHist',type=int,default=10,required=False)
parser.add_argument('--minDlugoscSlowa',type=int,default=0,required=False)
args = parser.parse_args()

nazwaPliku=args.nazwaPliku
wielkHist=args.wielkoscHist
minDlSlowa=args.minDlugoscSlowa
listaWyrazow=[]
#wczytanie i obrobka danych
with open(nazwaPliku, 'r',encoding="utf-8") as f:
    for line in f:
        listaWyrazow.append(line.strip().translate({ord(i): None for i in '.,:;?—'}).split(' '))
listaWyrazow2=[]
for i in range(len(listaWyrazow)):
    for j in range(len(listaWyrazow[i])):
        listaWyrazow2.append(listaWyrazow[i][j].lower())
listaWyrazow.clear()
while("" in listaWyrazow2):
    listaWyrazow2.remove("")
#tworzenie slownika
slownik=dict.fromkeys(listaWyrazow2,0)
for elem in listaWyrazow2:
    slownik[elem]=listaWyrazow2.count(elem)
slownik=dict(sorted(slownik.items(),key=lambda item: item[1],reverse=True))
#szykowanie danych do histogramu
slownikTuple=[(k,v) for k,v in slownik.items()]
doHistogramu=[]
i=0
for j in range(len(slownikTuple)):
    if(i<wielkHist and len(slownikTuple[j][0])>minDlSlowa):
        doHistogramu.append((slownikTuple[j][0],slownikTuple[j][1]))
        i+=1
#tworzenie histogramu
graph=Pyasciigraph()
for line in graph.graph('Histogram',doHistogramu):
    print(line)
