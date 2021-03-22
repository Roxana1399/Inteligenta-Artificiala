from UI import *
"""
Descriere: Porneste programul citind datele din fisier
Input:nr_ob  - nr de obiecte pe care le va avea lista, filename - fisierul de unde trebuie sa citeasc[, k - numarul de iteratii
Output: scrie rezultatele in fisier
"""
def start(nr_ob, filename,k,w):
    print("Punctul a.")
    sol = generateSolutie(nr_ob)
    g = citireObiecte(filename)
    print(sol)
    ok=validare(g, sol, w)
    print(ok)
    print("Punctul b.")
    if ok==True:
        suma=calitateSolutie(g,sol)
        print(suma)
    print("Punctul c.")
    solbest,suma_best,suma_med=BestSolution(k,g,w)
    #print(suma_best,suma_med)
    scriereRezultate("rezultate.txt",k,suma_best,suma_med)

def stratNonFisier(nr_ob, k,w):
    g=defObiecte()
    sol=generateSolutie(nr_ob)
    ok=validare(g,sol,w)
    print(ok)
    if ok==True:
        suma=calitateSolutie(g,sol)
        print(suma)
    print("Punctul c.")
    solbest,suma_best,suma_med=BestSolution(k,g,w)
    print(suma_best,suma_med)
    #scriereRezultate("rezultate.txt",k,suma_best,suma_med)


start(200,"rucsac_200.txt",10,112648)
#stratNonFisier(5, 100,17)

