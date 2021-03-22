import random
"""
Descriere:Genereaza o solutie aleatoare
Input:n-lungimea solutiei
Output: sol-o lista de 0 si 1
"""
def generarePunctCurent(n):
    sol = []
    for i in range(n):
        sol.append(random.randint(0, 1))
    return sol
"""
Descriere: Genereaza lista de vecini a unei solutii
Input: s- o solutie formata din 0 si 1, n - lungimea solutiei
Output: vecini - o lista de liste cu vecini
"""

def genereazaVecini(s,n):
    vecini = []
    i = 0
    while i < n:
        a = []
        for j in range(0, len(s)):
            if j != i:
                a.append(s[j])
            if j == i:
                if s[i] == 1:
                    a.append(0)

                else:
                    a.append(1)
        vecini.append(a)
        i = i + 1
    return vecini
"""
Descriere: Evalueaza o solutie: deetrmina valoarea ei 
Input: list - o lista de obiecte, sol - o solutie formata din 0 si 1
Output:
"""

def eval(list,sol):
    suma=0
    for j in range(len(sol)):
        suma=suma+ sol[j] * list[j].getValoare()
    return suma

"""
Descriere: Valideaza o solutice
Input:list -O lista de obiecte, sol - o solutie dormata din 0 si 1, w - greutatea rucsacului
Output:True/False
"""

def validSolution(lista,sol,w):
    s=0
    for i in range(len(sol)):
        s+=sol[i]*lista[i].getCantitate()

    if s == 0:
        return False
    else:
        if s <= w:
            return True
        else:
            return False

"""
Descriere: Determina cel mai bun vecin dintr-o lista de solutii 
Input: lista- o lista de obiecte, vecini -  o lista cu solutii, w- capacitatea ruscacului
Output:
"""

def celMaiBunVecin(lista,vecini,w):
    max=0
    rez=[]
    for i in range(len(vecini)):
        if(validSolution(lista,vecini[i],w)==True):
            if(eval(lista,vecini[i])>max):
                max=eval(lista,vecini[i])
                rez=vecini[i]
    return rez
"""
Descriere: Determina valoarea rucsacului data de o solutie
Input:lista - o lista de obiecte, sol  -o solute formata din 0 si 1
Output:
"""
def calitateSolutie(lista, sol):
    suma=0
    for j in range(len(sol)):
        suma += int(sol[j]) * int(lista[j].getValoare())
    return suma
"""
Descriere: Determina suma totala a tuturor solutiilor posibiel
Input:w- capacitatra ruscacului, solutii_posibile - o lista de solutii posibile, lista - o lista de obiecte
Output:
"""
def valoare_Sol(w, solutii_posibile, lista):
    suma_totala=0
    for i in range(len(solutii_posibile)):
        s = 0
        x=solutii_posibile[i]
        if validSolution(lista,x,w)==True:
            s= calitateSolutie(lista, x) #calculez valoarea
        else:
            s = 0
        suma_totala += s
    return suma_totala

