import random

def affichage(tab):
    for i in tab:
        print(i)

def choose(tab,tabSol):
    ligne=input("ligne")
    colonne=input("colonne")
    tab[ligne][colonne]=tabSol[ligne][colonne]
    if tabSol[ligne][colonne]==0:
        plusieursCase(tab,tabSol,ligne,colonne)
    

def plusieursCase(tab,tabSol,ligne,colonne):
    for i in range(3):
        a=i-1
        for j in range(3):
            b=j-1
            print(b)
            try:
                if ligne+a!=-1 and colonne+b!=-1 and tab[ligne+a][colonne+b]!=tabSol[ligne+a][colonne+b]:
                    tab[ligne+a][colonne+b]=tabSol[ligne+a][colonne+b]
                    if tabSol[ligne+a][colonne+b]==0:
                        plusieursCase(tab,tabSol,ligne+a,colonne+b)
            except (IndexError,RuntimeError):
                print(IndexError)
                pass    
 
tabDem=[]
tabSol=[]
maxBomb=5
for ligne in range(5):
    tabDem.append([])
    tabSol.append([])
    for colonne in range(5):
        tabDem[ligne].append(colonne)
        tabSol[ligne].append(colonne)
        if random.randint(0,2) == 1 and maxBomb>0:
            # print("saucisse")
            tabSol[ligne][colonne]=9
            maxBomb-=1
        else:
            tabSol[ligne][colonne]=0
        tabDem[ligne][colonne]="X"

for ligne in range(5):
    for colonne in range(5):
        if tabSol[ligne][colonne]==9:
            try:
                for i in range(3):
                    a=i-1
                    for j in range(3):
                        b=j-1
                        if tabSol[ligne+a][colonne+b]!=9 and ligne+a!=-1 and colonne+b!=-1:
                            tabSol[ligne+a][colonne+b]+=1

            except (IndexError):
                print(IndexError)
                pass    


affichage(tabDem)
choose(tabDem,tabSol)
affichage(tabDem)
choose(tabDem,tabSol)
affichage(tabDem)
print (len(tabDem))