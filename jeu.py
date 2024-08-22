from tkinter import *
from PIL import Image,ImageTk
from random import *
import tkinter.font as ft
from math import *
import time

BLOCS=15
LARGE=50



class Jeu(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.geometry("+370+140")
        self.fond= Canvas(self, width=LARGE*BLOCS , height=LARGE*BLOCS, bg='#E9E9E9')
        self.fond.pack(side = TOP)
        self.bind("<q>", self.gauche)
        self.bind('<d>', self.droite)
        self.bind('<z>', self.haut)
        self.bind('<s>', self.bas)
        self.tab_plateau=[]
        self.test=0
        self.x1=1
        self.y1=1
        self.x2=13
        self.y2=13
        f=open('map/mur.txt','r')

        for ligne in f:
            tab=[]
            for carct in ligne:
                if carct=="x" :
                    tab.append(1)

                elif carct=="p":
                    tab.append(2)

                elif carct=="A":
                    tab.append(3)

                else :
                    tab.append(0)

            self.tab_plateau.append(tab)

        f.close()

        self.img=Image.open("images/mur2.png")
        self.mur = ImageTk.PhotoImage(self.img)

        self.img1=Image.open("images/sol.png")
        self.sol = ImageTk.PhotoImage(self.img1)

        self.img2=Image.open("images/or.png")
        self.piece = ImageTk.PhotoImage(self.img2)

        self.img3=Image.open("images/persod.png")
        self.persod = ImageTk.PhotoImage(self.img3)

        self.img4=Image.open("images/persog.png")
        self.persog = ImageTk.PhotoImage(self.img4)


        for i in range(0,BLOCS):
                for j in range(0,BLOCS):

                    if self.tab_plateau[i][j]==1:
                        self.fond.create_image(LARGE*j+LARGE/2,LARGE*i+LARGE/2, image=self.mur)

                    if self.tab_plateau[i][j]==0:
                        self.fond.create_image(LARGE*j+LARGE/2,LARGE*i+LARGE/2, image=self.sol)

                    if self.tab_plateau[i][j]==2:
                        self.fond.create_image(LARGE*j+LARGE/2,LARGE*i+LARGE/2, image=self.piece)

        self.menu('start')
    """
    Fonctions de Menu:
    """

    def comencer(self,dif):

        self.dif=dif
        if dif==150:
            self.diff=170     #Un temps en milliseconde est utilisé pour la difficulte, pour simplifé le calcul du score,
        if dif==290:          #on attribu un ordre de grandeurs aux differents temps en milliseconde
            self.diff=130
        if dif==700:
            self.diff=100

        self.p=self.fond.create_image(375,75, image=self.persod)
        self.posit=[7,1]

        self.mecha = ImageTk.PhotoImage(Image.open("images/fantome.png"))
        self.mech=self.fond.create_image(75,75, image=self.mecha)

        self.mecha2 = ImageTk.PhotoImage(Image.open("images/fantome.png"))
        self.mech2=self.fond.create_image(675,675, image=self.mecha2)
        self.test_mort()

        self.mechant('d')
        self.mechant2()

        self.fond.delete(self.win)
        self.debut= time.perf_counter() # cette ligne servira a calculer le score en mesurant le temps de la partie
        #utilise time.clock() avant python 3.7

    def recommencer(self):
        self.destroy()
        jeu= Jeu()
        jeu.mainloop



    #Menu qui peut prendre 3 formes: ecran d'avant parie, gagner et perdu
    def menu(self,etat):
        self.logo = ImageTk.PhotoImage(Image.open("images/logo.png"))
        self.men=Frame(self,bd=0,bg='black')
        self.win=self.fond.create_window(375,375,height=350,width=650,window=self.men)

        if etat=='start':
            logo=Label(self.men,bd=0,image=self.logo)
            logo.pack()
            facile=Button(self.men ,bd=0 ,bg='black' ,fg='green' ,font=ft.Font(family='fixedsys',size=20),text='Facile',command=lambda:self.comencer(700))
            facile.pack(expand=True)
            moyen=Button(self.men ,bd=0 ,bg='black' ,fg='yellow' ,font=ft.Font(family='fixedsys',size=20),text='Moyen',command=lambda:self.comencer(290))
            moyen.pack(expand=True)
            dementiel=Button(self.men ,bd=0 ,bg='black' ,fg='red' ,font=ft.Font(family='fixedsys',size=20),text='Dementiel',command=lambda: self.comencer(150))
            dementiel.pack(expand=True)

        if etat=='perdu':
            self.posit=[20,20]
            self.mort = ImageTk.PhotoImage(Image.open("images/mort.png"))
            self.fond.itemconfig(self.p,image=self.mort)
            self.fond.tag_raise(self.p)

            msg=Label(self.men,bd=0,bg='black',fg='red',font=ft.Font(family='fixedsys',size=40),text='Perdu !')
            msg.pack(expand=True)
            re=Button(self.men ,bd=0 ,bg='black' ,fg='white' ,font=ft.Font(family='fixedsys',size=20),text='Recommencer',command=self.recommencer)
            re.pack(expand=True)

        if etat=='win':
            tps=time.perf_counter()-self.debut #temps total de la partie

            f=open("score/score.txt",'r')
            if int(f.read())<int(self.diff/tps*10000):            #Le score est calcule en fonction du temps total et de la difficulte choisie,
                f.close()                                         #ici, on regare dans le fichier tetxte si le meilleur score a ete vaincu
                new= open('score/score.txt','w')                        #puis on le remplace si necessaire.
                new.write(str(int(self.diff/tps*10000)))
                new.close()

            f=open("score/score.txt",'r')
            m_score=Label(self.men,bd=0,bg='black',fg='white',font=ft.Font(family='fixedsys',size=22),text=("Meilleur score: " + f.read()))
            f.close()
            score=Label(self.men,bd=0,bg='black',fg='white',font=ft.Font(family='fixedsys',size=22),text='Ton score: ' + str(int(self.diff/tps*10000)))

            self.posit=[20,20]
            self.fond.delete(self.mech)
            self.fond.delete(self.mech2)

            msg=Label(self.men,bd=0,bg='black',fg='green',font=ft.Font(family='fixedsys',size=40),text='Bien joue !')
            msg.pack(expand=True)
            score.pack(expand=True)
            m_score.pack(expand=True)
            re=Button(self.men ,bd=0 ,bg='black' ,fg='white' ,font=ft.Font(family='fixedsys',size=20),text='Recommencer',command=self.recommencer)
            re.pack(expand=True)





    """
    Fonction de mouvement:
    """

    def gauche(self,event):

        if self.tab_plateau[self.posit[1]][self.posit[0]-1] ==1:
            return
        if self.tab_plateau[self.posit[1]][self.posit[0]-1] ==2:                                              #On enleve l'or
            self.fond.create_image(LARGE*(self.posit[0]-1)+LARGE/2,LARGE*self.posit[1]+LARGE/2, image=self.sol) #si le jouer passe dessus
            self.tab_plateau[self.posit[1]][self.posit[0]-1] =0
            self.test+=1


        self.fond.delete(self.p)
        self.p=self.fond.create_image((self.posit[0]-1)*LARGE+25,self.posit[1]*LARGE+25, image=self.persog)     #On remplace l'image du personnage si il change de
        self.posit[0]-=1
        print(self.test)                                                                                        # direction dans les fonctions gauche et droite
        if self.test==17:
            self.menu('win')



    def droite(self,event):

        if self.tab_plateau[self.posit[1]][self.posit[0]+1] ==1:
            return
        if self.tab_plateau[self.posit[1]][self.posit[0]+1] ==2:
            self.fond.create_image(LARGE*(self.posit[0]+1)+LARGE/2,LARGE*self.posit[1]+LARGE/2, image=self.sol)
            self.tab_plateau[self.posit[1]][self.posit[0]+1] =0
            self.test+=1

        self.fond.delete(self.p)
        self.p=self.fond.create_image((self.posit[0]+1)*LARGE+25,self.posit[1]*LARGE+25, image=self.persod)
        self.posit[0]+=1

        if self.test==17:
            self.menu('win')


    def haut(self,event):
        if self.tab_plateau[self.posit[1]-1][self.posit[0]] ==1:
            return
        if self.tab_plateau[self.posit[1]-1][self.posit[0]] ==2:
            self.fond.create_image(LARGE*self.posit[0]+LARGE/2,LARGE*(self.posit[1]-1)+LARGE/2, image=self.sol)
            self.tab_plateau[self.posit[1]-1][self.posit[0]] =0
            self.test+=1

        self.fond.tag_raise(self.p) # tag raise permet de placer le personnage au dessus de tout les autres elements
        self.fond.move(self.p,0,-50)
        self.posit[1]-=1
        if self.test==17:
            self.menu('win')


    def bas(self,event):
        if self.tab_plateau[self.posit[1]+1][self.posit[0]] ==1:
            return
        if self.tab_plateau[self.posit[1]+1][self.posit[0]] ==2:
            self.fond.create_image(LARGE*self.posit[0]+LARGE/2,LARGE*(self.posit[1]+1)+LARGE/2, image=self.sol)
            self.tab_plateau[self.posit[1]+1][self.posit[0]] =0
            self.test+=1

        self.fond.tag_raise(self.p)
        self.fond.move(self.p,0,50)
        self.posit[1]+=1
        if self.test==17:
            self.menu('win')


    """
    fonctions des fantommes:
    """
    #Le premier fantome change de direction des qu'il rencontre une mur ou un couloir (sans revenir en arriere)
    def direction(self,x,y):
        a=[]
        if self.tab_plateau[y][x-1]!=1:
            a.append('q')

        if self.tab_plateau[y-1][x]!=1:
            a.append('z')

        if self.tab_plateau[y][x+1]!=1:
            a.append('d')

        if self.tab_plateau[y+1][x]!=1:
            a.append('s')
        return a

    def mechant(self,s):

        a=self.direction(self.x1,self.y1)
        if len(a)!=1:a.pop(a.index(s))
        d=choice(a)

        if d == 'q':

            self.fond.tag_raise(self.mech)
            self.fond.move(self.mech,-50,0)
            self.x1-=1
            self.fond.after(self.dif,lambda:self.mechant('d'))

        if d == 'z':

            self.fond.tag_raise(self.mech)
            self.fond.move(self.mech,0,-50)
            self.y1-=1
            self.fond.after(self.dif,lambda:self.mechant('s'))

        if d == 'd':

            self.fond.tag_raise(self.mech)
            self.fond.move(self.mech,50,0)
            self.x1+=1
            self.fond.after(self.dif,lambda:self.mechant('q'))

        if d == 's':

            self.fond.tag_raise(self.mech)
            self.fond.move(self.mech,0,50)
            self.y1+=1
            self.fond.after(self.dif,lambda:self.mechant('z'))



    #Le deuxieme essaye de se rapprocher de notre personnage a chaque deplacement
    def direction2(self,x,y):

        a=[]
        i=[]

        if self.tab_plateau[y][x-1]!=1:

            a.append(sqrt(
        (self.posit[0]-(self.x2-1))**2+
        (self.posit[1]-self.y2)**2
        ))
            i.append('q')

        if self.tab_plateau[y-1][x]!=1:

            a.append(sqrt(
        (self.posit[0]-self.x2)**2+
        (self.posit[1]-(self.y2-1))**2
        ))
            i.append('z')

        if self.tab_plateau[y][x+1]!=1:

            a.append(sqrt(
        (self.posit[0]-(self.x2+1))**2+
        (self.posit[1]-self.y2)**2
        ))
            i.append('d')

        if self.tab_plateau[y+1][x]!=1:

            a.append(sqrt(
        (self.posit[0]-self.x2)**2+
        (self.posit[1]-(self.y2+1))**2
        ))
            i.append('s')

        return i[a.index(min(a))]

    def mechant2(self):

        a=self.direction2(self.x2,self.y2)

        if a == 'q':

            self.fond.tag_raise(self.mech2)
            self.fond.move(self.mech2,-50,0)
            self.x2-=1
            self.fond.after(self.dif+75,lambda:self.mechant2())

        if a == 'z':

            self.fond.tag_raise(self.mech2)
            self.fond.move(self.mech2,0,-50)
            self.y2-=1
            self.fond.after(self.dif+75,lambda:self.mechant2())

        if a == 'd':

            self.fond.tag_raise(self.mech2)
            self.fond.move(self.mech2,50,0)
            self.x2+=1
            self.fond.after(self.dif+75,lambda:self.mechant2())

        if a == 's':

            self.fond.tag_raise(self.mech2)
            self.fond.move(self.mech2,0,50)
            self.y2+=1
            self.fond.after(self.dif+75,lambda:self.mechant2())



    def test_mort(self):
        if (self.x1==self.posit[0] and self.y1==self.posit[1]) or (self.x2==self.posit[0] and self.y2==self.posit[1]):

            self.menu('perdu')
        self.after(10,self.test_mort)



if __name__ == '__main__':
    jeu = Jeu()
    jeu.mainloop()

