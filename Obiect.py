class Obiect:
    def __init__(self, cantitate, valoare):
        self._cantitate=cantitate
        self._valoare=valoare
    def getCantitate(self):
        return self._cantitate
    def getValoare(self):
        return self._valoare
    def setValoare(self, newValoare):
        self._valoare=newValoare
    def setCantitate(self, newCantitate):
        self._cantitate=newCantitate
    def _eq_(self, other):
        if(self.getCantitate()==other.getCantitate()) and (self.getValoare()==other.getValoare()):
            return  True
        else:
            return False
    def _str_(self):
        return str(self.getCantitate())+" "+str(self.getValoare())
