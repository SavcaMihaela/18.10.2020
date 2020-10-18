##Se considera 3 numere intregi. Daca toate sunt pozitive, sa se afiseze numarul mai mare dintre al doilea is al treilea, in caz contrar sa se calculeze suma primelor doua numere
a=int(input("Nr 1"))
b=int(input("Nr 2"))
c=int(input("Nr 3"))
if(a>0) and (b>0) and (c>0):
    if (b>c):
        print(b)
    if (c>b):
        print(c)
    if (c==b):
        print(b)
elif (a<0) or (b<0) or (c<0):
    print(a+b)