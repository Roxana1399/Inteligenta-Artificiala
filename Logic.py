from Obiect import *
import random
class Logic:
    def __init__(self, lista_obiecte):
        self._lista_obiecte=lista_obiecte

    def addElem(self, newElem):
        self._lista_obiecte.append(newElem)

    def getLiata(self):
        return self._lista_obiecte

    def setLista(self, newList):
        self._lista_obiecte=newList

    def generateSolutie(n):
        sol = []
        for i in range(n):
            sol.append(random.randint(0, 1))
        return sol

    def validare(self, sol, w):
        s = 0
        for i in range(len(self)):
            s += sol[i] * self.getLiata().getCantitate()
        if s == 0:
            return False
        else:
            if s <= w:
                return True
            else:
                return False