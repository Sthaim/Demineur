import random
import tkinter as tk

def affichage(tab):
    print("  [1]   [2]  [3]   [4]   [5]   [6]   [7]   [8]   [9]   [10]")
    nLigne=1
    for i in tab:
        print(nLigne,i)
        nLigne+=1

def choose(tab,tabSol):
    ligne=int(input("ligne"))-1
    colonne=int(input("colonne"))-1
    tab[ligne][colonne].config(text=tabSol[ligne][colonne])
    if tabSol[ligne][colonne]==0:
        plusieursCase(tab,tabSol,ligne,colonne)
    if tabSol[ligne][colonne]==9:
        defaite(tabSol,tab)
        return 1
    return 0

def defaite(tabRes,tabBomb):
    for ligne in range(len(tabRes)):
        for colonne in range(len(tabRes)):
            if tabRes[ligne][colonne]==9:
                tabBomb[ligne][colonne]=tabRes[ligne][colonne]
    affichage(tabBomb)
    print("Vous avez activer une bombe! Perdu")

def plusieursCase(tab,tabSol,ligne,colonne):
    for i in range(3):
        a=i-1
        for j in range(3):
            b=j-1
            try:
                if ligne+a!=-1 and colonne+b!=-1 and tab[ligne+a][colonne+b]!=tabSol[ligne+a][colonne+b]:
                    tab[ligne+a][colonne+b]=tabSol[ligne+a][colonne+b]
                    if tabSol[ligne+a][colonne+b]==0:
                        plusieursCase(tab,tabSol,ligne+a,colonne+b)
                    # if tabSol[ligne+a][colonne+b]==9:
                    #     defaite(tabSol,tab)
            except (IndexError,RuntimeError):
                pass    

def createBoard(tLigne,tColonne,tabBomb,tabRes,frame):
    maxBomb=int((tLigne*tColonne)/3)
    for ligne in range(tLigne):
        tabBomb.append([])
        tabRes.append([])
        for colonne in range(tColonne):
            tabBomb[ligne].append(colonne)
            tabRes[ligne].append(colonne)
            if random.randint(0,4) == 1 and maxBomb>0:
                # print("saucisse")
                tabRes[ligne][colonne]=9
                maxBomb-=1
            else:
                tabRes[ligne][colonne]=0
            tabBomb[ligne][colonne]= "X"
            

    for ligne in range(tLigne):
        for colonne in range(tColonne):
            if tabRes[ligne][colonne]==9:
                try:
                    for i in range(3):
                        a=i-1
                        for j in range(3):
                            b=j-1
                            if tabRes[ligne+a][colonne+b]!=9 and ligne+a!=-1 and colonne+b!=-1:
                                tabRes[ligne+a][colonne+b]+=1

                except (IndexError):
                    pass    

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
frame.grid(row=0,column=0)
but=tk.Button(frame,command="")
but.grid(column=0, row=0)

tabDem=[]
tabSol=[]
loose=0
createBoard(10,10,tabDem,tabSol,frame)
affichage(tabDem)
while loose!=1:
    loose=choose(tabDem,tabSol)
    affichage(tabDem)
print("yes")
int(input("end"))



