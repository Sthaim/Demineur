import random
import tkinter as tk
import tkinter.font as tkFont
from functools import partial

def choose(tab,tabSol,ligne,colonne,tLigne,tColonne,root):
    global first
    color=["","","","","","","",""]
    for i in range(8):
        color[i]=" "
    color[0]="blue"
    color[1]="green"
    color[2]="red"
    color[3]="#8000FF"
    color[4]="#915427"
    color[5]="#1F5800"
    color[6]="black"
    color[7]="#7E7E7E"
    if first==1:
        first=0
        createTabSolution(tabSol,ligne,colonne,tLigne,tColonne)
    # colorI=tabSol[ligne][colonne]
    tab[ligne][colonne].config(text=tabSol[ligne][colonne])
    if tabSol[ligne][colonne]-1==-1 and tabSol[ligne][colonne]!=9:
        tab[ligne][colonne].config(fg="black")
    elif tabSol[ligne][colonne]!=9:
        tab[ligne][colonne].config(fg=color[tabSol[ligne][colonne]-1])

        # 
    if tabSol[ligne][colonne]==0:
        plusieursCase(tab,tabSol,ligne,colonne,color)
    if tabSol[ligne][colonne]==9:
        defaite(tab,tabSol,root)
    else:
        victoire(tab,tabSol,root)

def victoire(tabBomb,tabRes,root):
    bomb=0
    covered=0
    for ligneF in range(len(tabRes)):
        for colonneF in range(len(tabRes[0])):
            if tabRes[ligneF][colonneF]==9:
                bomb+=1
            if tabBomb[ligneF][colonneF].cget("text")=="X":
                covered+=1
    if covered==bomb:
        popup = tk.Tk()
        popup.geometry("200x200")
        yup=tk.Button(popup,text="C'est gagné, bien joué",command=lambda:[root.destroy(),popup.destroy()])
        yup.pack()

def defaite(tabBomb,tabRes,root):
    for ligne in range(len(tabRes)):
        for colonne in range(len(tabRes[0])):
            if tabRes[ligne][colonne]==9:
                tabBomb[ligne][colonne].config(text=tabRes[ligne][colonne])
    print("Vous avez activer une bombe! Perdu")
    popup = tk.Tk()
    popup.geometry("200x200")
    yup=tk.Button(popup,text="Vous avez activer une bombe!"+" Perdu",command=lambda:[root.destroy(),popup.destroy()])
    yup.pack()

def plusieursCase(tab,tabSol,ligne,colonne,color):
    for i in range(3):
        a=i-1
        for j in range(3):
            b=j-1
            try:
                if ligne+a!=-1 and colonne+b!=-1 and tab[ligne+a][colonne+b].cget("text")!=str(tabSol[ligne+a][colonne+b]):
                    if tabSol[ligne+a][colonne+b]-1!=-1 and tabSol[ligne+a][colonne+b]!=9:
                        tab[ligne+a][colonne+b].config(text=str(tabSol[ligne+a][colonne+b]),fg=color[tabSol[ligne+a][colonne+b]-1])
                    else:
                        tab[ligne+a][colonne+b].config(text=str(tabSol[ligne+a][colonne+b]),fg="black")
                    if tabSol[ligne+a][colonne+b]==0:
                        plusieursCase(tab,tabSol,ligne+a,colonne+b,color)
                    # if tabSol[ligne+a][colonne+b]==9:
                    #     defaite(tabSol,tab)
            except (IndexError,RuntimeError):
                pass    

def createBoard(tLigne,tColonne,tabBomb,tabRes,frame,root,bold):
    for ligne in range(tLigne):
        tabBomb.append([])
        for colonne in range(tColonne):
            tabBomb[ligne].append(colonne)
            tabBomb[ligne][colonne]=tk.Button(frame,text="X",command=partial(choose,tabBomb,tabRes,ligne,colonne,tLigne,tColonne,root),width=5,font=bold)
            tabBomb[ligne][colonne].grid(column=colonne, row=ligne)
            
def createTabSolution(tabRes,ligneI,colonneI,tLigne,tColonne):
    maxBomb=int((tLigne*tColonne)/4)
    min=0
    for ligne in range(tLigne):
        tabRes.append([])
        for colonne in range(tColonne):
            tabRes[ligne].append(0)

    for ligne in range(tLigne):
        for colonne in range(tColonne):      
            min=0
            for i in range(3):
                a=i-1
                for j in range(3):
                    b=j-1
                    if ligneI+a!=-1 and colonneI+b!=-1 and colonneI+b<tColonne and ligneI+a<tLigne and random.randint(0,(tLigne+tColonne)*2) == 0 and maxBomb > 0 and ligne!=ligneI+a and colonne!=colonneI+b:
                        tabRes[ligne][colonne]=9
                        if min==0:
                            maxBomb-=1
                            min=1
                    else:
                        if ligneI+a!=-1 and colonneI+b!=-1 and colonneI+b<tColonne and ligneI+a<tLigne:
                            tabRes[ligneI+a][colonneI+b]=0

    for ligne in range(tLigne):
        for colonne in range(tColonne):
            if tabRes[ligne][colonne]==9:
                for i in range(3):
                    c=i-1
                    for j in range(3):
                        d=j-1
                        if ligne+c!=-1 and colonne+d!=-1 and colonne+d<tColonne and ligne+c<tLigne:
                            if tabRes[ligne+c][colonne+d]!=9:
                                tabRes[ligne+c][colonne+d]+=1

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
frame.grid(row=0,column=0)
bold = tkFont.Font(family='Helvetica',size=10,weight='bold')

first=1
tabDem=[]
tabSol=[]
loose=0
createBoard(int(input("Hauteur du démineur ?")),int(input("Largeur du démineur ?")),tabDem,tabSol,frame,root,bold)
root.mainloop()
# affichage(tabDem)
# while loose!=1:
#     loose=choose(tabDem,tabSol,,)
#     affichage(tabDem)
# choose(tabBomb,tabRes,ligne,colonne)


