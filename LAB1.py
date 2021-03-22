import random
def generareSol(n):
    sol=[]
    for i in range(n):
        sol.append(random.randint(0,1))
    return sol
def validare(g,sol,w):
    s=0
    for i in range(len(g)):
        s+=sol[i]*g[i]
    if s==0:
        return False
    else:
        if s<=w:
            return  True
        else:
            return False
sol=generareSol(5)
g=[10,2,4,2,6]
w=17
print(sol)
print(validare(g,sol,w))