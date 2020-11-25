import random
import tkinter as tk
from functools import partial

def choose(tab,tabSol,ligne,colonne,root):
    tab[ligne][colonne].config(text=tabSol[ligne][colonne])
    print(ligne,colonne)
    # tabSol[ligne][colonne]
    if tabSol[ligne][colonne]==0:
        plusieursCase(tab,tabSol,ligne,colonne)
    if tabSol[ligne][colonne]==9:
        defaite(tabSol,tab,root)

def defaite(tabBomb,tabRes,root):
    for ligne in range(len(tabRes)):
        for colonne in range(len(tabRes)):
            if tabRes[ligne][colonne]==9:
                tabBomb[ligne][colonne].config(text=str(tabRes[ligne][colonne]))
    print("Vous avez activer une bombe! Perdu")
    popup = tk.Tk()
    popup.geometry("200x200")
    yup=tk.Button(popup,text="Vous avez activer une bombe!"+" Perdu",command=lambda:root.destroy())
    yup.pack()
def plusieursCase(tab,tabSol,ligne,colonne):
    for i in range(3):
        a=i-1
        for j in range(3):
            b=j-1
            try:
                if ligne+a!=-1 and colonne+b!=-1 and tab[ligne+a][colonne+b].cget("text")!=str(tabSol[ligne+a][colonne+b]):
                    tab[ligne+a][colonne+b].config(text=str(tabSol[ligne+a][colonne+b]))
                    if tabSol[ligne+a][colonne+b]==0:
                        plusieursCase(tab,tabSol,ligne+a,colonne+b)
                    # if tabSol[ligne+a][colonne+b]==9:
                    #     defaite(tabSol,tab)
            except (IndexError,RuntimeError):
                pass    

def createBoard(tLigne,tColonne,tabBomb,tabRes,frame,root):
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
            
            tabBomb[ligne][colonne]=tk.Button(frame,text="X",command=partial(choose,tabBomb,tabRes,ligne,colonne,root),width=5)
            tabBomb[ligne][colonne].grid(column=colonne, row=ligne)

            
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


tabDem=[]
tabSol=[]
loose=0
createBoard(10,10,tabDem,tabSol,frame,root)
root.mainloop()
# affichage(tabDem)
# while loose!=1:
#     loose=choose(tabDem,tabSol,,)
#     affichage(tabDem)
# choose(tabBomb,tabRes,ligne,colonne)
print("yes")
int(input("end"))