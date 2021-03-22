from Obiect import Obiect
from Repo import *
"""
Descriere: Creează o lista cu obiecte
Input:-
Output:lista - o lista cu obiecte
"""
def defObiecte():
    lista=[]
    ob=Obiect(10,2)
    lista.append(ob)
    ob=Obiect(2,4)
    lista.append(ob)
    ob=Obiect(7,5)
    lista.append(ob)
    ob=Obiect(3,4)
    lista.append(ob)
    ob=Obiect(6,7)
    lista.append(ob)
    return lista
"""
Descriere: Citeste obiectele din fisier
Input:Numele unui fisier
Output:lista - o lista cu obiecte
"""
def citireObiecte(filename):
    lista=[]
    f = open(filename, "r")
    nr_Obiecte=int(f.readline())
    for i in range(nr_Obiecte):
        ob=f.readline()
        lis=ob.split()
        obj=Obiect(int(lis[2]),int(lis[1]))
        lista.append(obj)
    f.close()
    return lista
"""
Descriere: Scrie rezultatele in fisiei
Input:filename - fisierul in care trebuie sa scrie, k - valoarea nr. de iteratii, best- cea mai buna valoare, average- valoarea medie
Output: - 
"""
def scriereRezultate(filename,k,best,average):
    f=open(filename,"a")
    string=str(k)+"     "+str(best)+"    "+str(average)+"\n"
    f.write(string)
    f.close()

"""
Descriere: Genereaza cea mai buna solutie folosind algoritnul NAHC
Input:n - lungimea unei solutii, maxIteratii - numarul de iteratii dupa care se stabileste o solutie, filename - fisierul de unde se citesc obiectele, w-capacitaea rucsacului
Output: c- cel mai bun vecin, average_suma - valoarea medie, best_sum - cea mai buna valoare
"""
def NAHC(n,maxIteratii,lista,w):
    c=generarePunctCurent(n) #se genereaza punctul curent
    solutiiPos=[]
    #print(c)
    for i in range(maxIteratii): #maxIteratii=k
        vecini = genereazaVecini(c, n)  # se genereaza vecinii punctului curent
        j=0
        while j < len(vecini):
            x = vecini[j]
            if int(eval(lista,x))> int(eval(lista,c)):
               if validSolution(lista,x,w)== True: #daca se gaseste un vecin mai bun, acesta devine punct curent si se genereaza pentru el vecinii
                    c=x
                    vecini=[]
                    vecini=genereazaVecini(x,n) #se genereaza vecinii pentru noul punct curent
            j=j+1
        solutiiPos.append(c)  #se adauga punctul curent in lista
        c = generarePunctCurent(n)  # se genereaza un nou punct curent

    c = celMaiBunVecin(lista, solutiiPos,w)  # se determina cel mai bun vecin -best vecin
    best_sum=calitateSolutie(lista,c)
    average_suma=valoare_Sol(w,solutiiPos,lista)/maxIteratii
    if validSolution(lista, c, w) == True:  # se verifica daca solutia determinata este valida
        return c, average_suma, best_sum
    else:
        return None, average_suma, best_sum
