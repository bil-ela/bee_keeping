import numpy
from math import sqrt
import pylab

pylab.clf()

"""
THEME : RUCHE
"""

"""
SOUS THEME : SAISON
"""

#On suppose que l'année commence au début du printemps (mi-fin mars)
# 1 unité correspond à 1 un jour, un an = 360 unités
#On pose comme convention le jour 0 comme le 20 mars 2010 (1er jour du printemps 2010)

pop=eval(input("Choississez le nombre d'abeilles avec lequelles vous voulez commencer "))
jour=eval(input('Choississez le jour où vous souhaitez commencez la simulation '))
duree=eval(input('Choississez la duree de la simulation '))
jvie=eval(input("Choississez la durée de vie moyen d'une abeille "))
mult=eval(input('Choississez le multiplicateur de temps de vie durant l"hibernation '))
#loc=eval(input('Choississez la loc'))

def fsaison (jour):
    temps=jour%360 #reste de la division euclidienne par 360
    s = ''
    if temps < 90:
        s = 'printemps'
    elif temps <270:
        s = 'automne_ete'
    else:
        s = 'hiver'
    return s

print(" Nous somme donc au/en",fsaison(jour),"le jour",jour,"et nous allons simuler",duree,"jours")
#fsaison=fsaison(jour)

#temps=eval(input("Valeur reine pop svp"))
#print(saison(temps))


"""
SOUS THEME : ''Aleatoire''
"""

#Gaussienne pour distribuer l'âge des abeilles au sein d'une ruche

#x=pylab.linspace(-3,3,1000)
f = lambda x:(1/sqrt(2*numpy.pi))*numpy.exp((-x**2)/2)
g = lambda x:(-80/81)*x**2+(800/9)*x #fonction polynomiale qui a x associe le nombre de naissance de la reine
#pylab.plot(x,f(x))
#pylab.show()

"""
"""

def fpop_init(pop):
    #4 tableaux différents, le tableau tot n'est pas nécessaire
    h= 10/jvie ; a=-5  #a correspond a mon x min, h correspond a mon pas, implicitement b correspond a 5 et a mon x max
    pop_tot=[]; ouv=[]; mal=[]; res=[]
    for i in range (jvie): #65 pour le temps de vie moyen d'une abeille quelconque qu'elle soit au printemps
        pop_tot.append(int((f(a+i*h)*h)*pop))
        ouv.append(int((f(a+i*h)*h)*pop*0.85))
        mal.append(int((f(a+i*h)*h)*pop*0.05))
        res.append(int((f(a+i*h)*h)*pop*0.10))
    return (pop_tot,ouv,mal,res) #pour mal, ouv et res, comment les renvoyer ?


#pop=eval(input("Valeur population totale"))
#print(fpop_init(pop))
tot_pop,ouv,mal,res=fpop_init(pop)
list_graph_tot_pop=[];list_graph_mal=[];list_graph_ouv=[];list_graph_res=[]
no_var_glo_cycle=duree//360
no_var_cycle=[duree//360]
no_var_compteur=[0]
duree_ini=[duree]

def ruche (jour,duree):
    #Définition de toutes les constantes
    compteur=no_var_compteur[0]
    nb_pol = tot_pop
    no_var_jour = jour
    no_var_duree = duree
    saison = fsaison(jour)
    cycle = no_var_cycle[0]
    print('nb_pol vaut ',nb_pol)
    print('no_var_jour vaut ',no_var_jour)
    print('no_var_duree vaut ',no_var_duree)
    #Saison
    # Printemps été, saison optimal pour la fécondation
    while cycle > -1:
        if saison == 'printemps' and (no_var_jour+no_var_duree) >90+360*compteur:
            print('PRINTEMPS ++')
            if sum(tot_pop) != 0:
                for i in range (no_var_jour-(360*compteur),91):
                    nb_pol[0] = nb_pol[0] + int(g(i))                                   #Naissance reine, jusqu'a 2000 par jour
                    ouv[0] = ouv[0] +  int(g(i)*0.85)
                    mal[0] = mal[0] + int(g(i)*0.05)
                    res[0] = res[0] + int(g(i)*0.10)
                    list_graph_ouv.append(sum(ouv))
                    list_graph_tot_pop.append(sum(tot_pop))
                    list_graph_res.append(sum(res))
                    list_graph_mal.append(sum(mal))
                    nb_pol[len(nb_pol)-1]=0
                    ouv[len(ouv)-1]=0
                    res[len(res)-1]=0
                    mal[len(mal)-1]=0
                    nb_pol.insert(0,nb_pol.pop())                                       #Décale d'un cran les éléments du tableau, pop() supprime puis retourne le dernier élement d'une liste
                    ouv.insert(0,ouv.pop())
                    mal.insert(0,mal.pop())
                    res.insert(0,res.pop())
                    duree = duree - 1
            else:
                for i in range (no_var_jour-(360*compteur),91):
                    list_graph_ouv.append(0)
                    list_graph_tot_pop.append(0)
                    list_graph_res.append(0)
                    list_graph_mal.append(0)
                    duree = duree - 1                                                     
            jour=jour + ((no_var_glo_cycle*360)-(cycle*360)+90-no_var_jour)
            print(jour)
            print(duree)
            return ruche(jour,duree)
        elif saison == 'printemps' and (no_var_jour+no_var_duree) <= 90+360*compteur:
            print('PRINTEMPS --')
            if sum(tot_pop) != 0:
                for i in range (duree+1):
                    nb_pol[0] = nb_pol[0] + int(g(i))                                   #Naissance reine, jusqu'a 2000 par jour
                    ouv[0] = ouv[0] +  int(g(i)*0.85)
                    mal[0] = mal[0] + int(g(i)*0.05)
                    res[0] = res[0] + int(g(i)*0.10)
                    list_graph_ouv.append(sum(ouv))                                     #Ajout totaux population dans une liste
                    list_graph_tot_pop.append(sum(tot_pop))
                    list_graph_res.append(sum(res))
                    list_graph_mal.append(sum(mal))
                    nb_pol[len(nb_pol)-1]=0
                    ouv[len(ouv)-1]=0
                    res[len(res)-1]=0
                    mal[len(mal)-1]=0
                    nb_pol.insert(0,nb_pol.pop())                                       #Décalage
                    ouv.insert(0,ouv.pop())
                    mal.insert(0,mal.pop())
                    res.insert(0,res.pop())
            else:
                for i in range (duree+1):
                    list_graph_ouv.append(0)
                    list_graph_tot_pop.append(0)
                    list_graph_res.append(0)
                    list_graph_mal.append(0)
                jour = jour + 1 
        elif (saison == 'automne_ete') and (no_var_jour+no_var_duree)>270+360*compteur:
            chgmt = 0                                                               #Au vue de l'hibernation, le temps de vie est multiplié par 4 (6 mois de vie)
            ajus_pol = 0
            print('AUTOMNE_ETE ++')
            for i in range (no_var_jour,no_var_jour+181):
                chgmt = chgmt + 1
                if chgmt >= mult:
                    nb_pol[len(nb_pol)-1]=0
                    ouv[len(ouv)-1]=0
                    res[len(res)-1]=0
                    mal[len(mal)-1]=0
                    nb_pol.insert(0,nb_pol.pop())                                   #Décalage
                    mal.insert(0,mal.pop())
                    res.insert(0,res.pop())
                    ouv.insert(0,ouv.pop())
                    chgmt = chgmt - mult
                for j in range (len(mal)):
                    ajus_pol = mal[j]-int(0.95*mal[j])
                    mal[j]=int(0.95*mal[j])                                         #Les mâles meurent petit à petit (à définir) puisqu'il n'ont aucune utilité
                    nb_pol[j]=nb_pol[j]-ajus_pol                                    #Les mâles meurentt petit à petit (à définir) puisqu'il n'ont aucune utilité
                list_graph_ouv.append(sum(ouv))                                     #Ajout totaux population dans une liste
                list_graph_tot_pop.append(sum(tot_pop))
                list_graph_res.append(sum(res))
                list_graph_mal.append(sum(mal))
                duree = duree - 1 
            jour=jour + ((no_var_glo_cycle*360)-(cycle*360)+270-no_var_jour)                       #Retour à la date initial sans le jours d'automne (à revoir peut-être)
            return ruche(jour,duree)
        elif (saison == 'automne_ete') and (no_var_jour+no_var_duree)<=270+360*compteur:
            chgmt = 0
            ajus_pol = 0
            print('AUTOMNE_ETE --')                                           
            for i in range (duree+1):                       #Changement au niveau des paramètres de la boucle 'for'
                chgmt = chgmt + 1
                if chgmt >= mult:
                    nb_pol[len(nb_pol)-1]=0
                    ouv[len(ouv)-1]=0
                    res[len(res)-1]=0
                    mal[len(mal)-1]=0
                    nb_pol.insert(0,nb_pol.pop())                                   #Décalage
                    mal.insert(0,mal.pop())
                    res.insert(0,res.pop())
                    ouv.insert(0,ouv.pop())
                    chgmt = chgmt - mult
                for j in range (len(mal)):
                    ajus_pol = mal[j]-int(0.95*mal[j])
                    mal[j]=int(0.95*mal[j])                                         #Les mâles meurent petit à petit (à définir) puisqu'il n'ont aucune utilité
                    nb_pol[j]=nb_pol[j]-ajus_pol                                    #Les mâles meurent petit à petit (à définir) puisqu'il n'ont aucune utilité
                list_graph_ouv.append(sum(ouv))                                     #Ajout totaux population dans une liste
                list_graph_tot_pop.append(sum(tot_pop))
                list_graph_res.append(sum(res))
                list_graph_mal.append(sum(mal))
                jour = jour + 1
                duree = duree - 1                                                   #Si bug verif avec valeur de la duree
        elif saison == 'hiver' and (no_var_jour+no_var_duree) >360+360*compteur:
            chgmt = 0                                                                   #Au vue de l'hibernation, le temps de vie est multiplié par 4 (6 mois de vie)
            print('HIVER ++');print('HIVER ++');print('HIVER ++');print('HIVER ++')
            for i in range (no_var_jour,no_var_jour+91):
                chgmt = chgmt + 0.5
                if chgmt == mult:
                    chgmt = chgmt - mult
                    nb_pol[len(nb_pol)-1]=0
                    ouv[len(ouv)-1]=0
                    res[len(res)-1]=0
                    mal[len(mal)-1]=0
                    nb_pol.insert(0,nb_pol.pop())                                    #Décalage
                    mal.insert(0,mal.pop())
                    ouv.insert(0,ouv.pop())
                    res.insert(0,res.pop())  
                list_graph_ouv.append(sum(ouv))                                     #Ajout totaux population dans une liste
                list_graph_tot_pop.append(sum(tot_pop))
                list_graph_res.append(sum(res))
                list_graph_mal.append(sum(mal))
                duree = duree - 1 
            jour=jour + ((no_var_glo_cycle*360)-(cycle*360)+360-no_var_jour)  #Retour a la date initial sans le jours d'automne (à revoir peut-être)
            no_var_cycle[0] = no_var_cycle[0] - 1
            no_var_compteur[0]=no_var_compteur[0]+1
            print('Nous sommes en',2010+no_var_compteur[0])
            return ruche(jour,duree)
        elif saison == 'hiver' and (no_var_jour+no_var_duree) <=360+360*compteur:
            chgmt = 0                                               #Au vue de l'hibernation, le temps de vie est multiplié par 4 (6 mois de vie)
            print('HIVER --');print('HIVER --');print('HIVER --');print('HIVER --')
            for i in range (0,duree+1):
                chgmt = chgmt + 0.5
                if chgmt == mult:
                    chgmt = chgmt - mult
                    nb_pol[len(nb_pol)-1]=0
                    ouv[len(ouv)-1]=0
                    res[len(res)-1]=0
                    mal[len(mal)-1]=0
                    nb_pol.insert(0,nb_pol.pop())                   #Décalage
                    mal.insert(0,mal.pop())
                    ouv.insert(0,ouv.pop())
                    res.insert(0,res.pop())
                list_graph_ouv.append(sum(ouv))                     #Ajout totaux population dans une liste
                list_graph_tot_pop.append(sum(tot_pop))
                list_graph_res.append(sum(res))
                list_graph_mal.append(sum(mal))
                jour = jour + 1
                duree = duree - 1
        return (list_graph_tot_pop,list_graph_ouv,list_graph_mal,list_graph_res)
    
ruche(jour,duree)

def maximum_pop(list_graph_tot_pop):
    max=list_graph_tot_pop[0]
    for i in list_graph_tot_pop:
        if i>max:
            max=i
    return max

def lissage (T):
    for i in range (1,len(T)-2):
        if T[i] == T[i+1]:
            T[i] = int((T[i-1]+T[i+1])/2)
    return T

liss_tot_pop=lissage(list_graph_tot_pop)
liss_ouv=lissage(list_graph_ouv)
liss_mal=lissage(list_graph_mal)
liss_res=lissage(list_graph_res)


max_list_graph_tot_pop=maximum_pop(list_graph_tot_pop)      

pylab.ylim(-10,max_list_graph_tot_pop+int(0.1*max_list_graph_tot_pop))
pylab.xlim(jour,jour+duree+10)



tabl_x=range(jour,jour+duree+1,1)
x=numpy.array(tabl_x)
y_pop=numpy.array(liss_tot_pop)
y_ouv=numpy.array(liss_ouv)
y_mal=numpy.array(liss_mal)
y_res=numpy.array(liss_res)
(pylab.plot(x,y_pop,'y-'),pylab.plot(x,y_ouv,'g-'),pylab.plot(x,y_mal,'b--'),pylab.plot(x,y_res,'g--'))

pylab.legend([': POP TOT',': OUV',': MALES',': RESTE',],loc='lower right')
pylab.show()    

#print(maximum_pop(list_graph_tot_pop))
#print(maximum_pop(list_graph_tot_pop))
#print(maximum_pop(list_graph_tot_pop))
#print(maximum_pop(list_graph_tot_pop))
#print(maximum_pop(list_graph_tot_pop))
