import random
"""
Descriere:Genereaza o solutie aleatoare
Input:n-lungimea solutiei
Output: sol-o lista de 0 si 1
"""
def generateSolutie(n):
    sol = []
    for i in range(n):
        sol.append(random.randint(0, 1))
    return sol
"""
Descriere: Valideaza o solutice
Input:list -O lista de obiecte, sol - o solutie dormata din 0 si 1, w - greutatea rucsacului
Output:True/False
"""
def validare(list, sol, w):
    s = 0
    for i in range(len(list)):
        s += sol[i] * list[i].getCantitate()
    if s == 0:
        return False
    else:
        if s <= w:
            return True
        else:
            return False
"""
Descriere: Determina valoarea rucsacului data de o solutie
Input:lista - o lista de obiecte, sol  -o solute formata din 0 si 1
Output:
"""
def calitateSolutie(lista, sol):
    suma=0
    for j in range(len(sol)):
        suma += sol[j] * lista[j].getValoare()
    return suma


"""
Descriere:Determina cea mai buna solutie dupa k rulari 
Input: k - numarul de rulari, list - lista de obiecte, w-capacitaea rucsacului
Output: solbest - cea mai buna solutie, suma_best - valoarea celei mai bune solutii, suma_total/k - valoarea medie a tuturor solutiilor
"""
def BestSolution(k,list,w):
    i = 1
    suma_best = 0
    solbest = []
    suma_totala=0
    while i <= k:
        s = 0
        sol = generateSolutie((len(list)))
        if validare(list,sol,w)==True: #calculeaza valoarea
            for j in range(len(sol)):
                s += sol[j] * list[j].getValoare()
        else:
            s=0
        suma_totala+=s
        if s > suma_best:
            suma_best = s
            solbest = sol
        i = i + 1
    return solbest,suma_best, suma_totala/k
