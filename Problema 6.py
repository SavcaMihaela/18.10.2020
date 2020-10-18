##Andrei primeste intr-o zi 3 note, nu toate bune.Se hotaraste ca daca ultima nota este macar 8 sa le zica parintilor toate notele, dar daca este mai mica de cat 8 sa le comunice cea mai mare nota primita dintre cele doua
a=int(input("Prima nota"))
b=int(input("A doua nota"))
c=int(input("A treia nota"))
if (c>8):
    print(a, b, c)
if (a>b):
    print(a)
if (b>a):
    print(b)
if (a==b):
    print(a)