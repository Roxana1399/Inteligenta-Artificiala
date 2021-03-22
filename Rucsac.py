from  UI import *
def rezultate(nr_obj, k, filename,w):
    lista = citireObiecte(filename)
    sol, average, best=NAHC(nr_obj, k, lista,w)
    scriereRezultate("rezultate.txt", k, best, average)
def rezultateNonFile(nr_obj, k,w):
    lista=defObiecte()
    sol, average, best = NAHC(nr_obj, k, lista, w)
    #scriereRezultate("rezultate.txt", k, best, average)
    print(k,best,average)

rezultate(20,100,"rucsac_20.txt",524)
#rezultateNonFile(5, 100,17)




