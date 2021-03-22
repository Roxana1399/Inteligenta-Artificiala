from Repo import *
from Obiect import Obiect
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
    f.close