##La ora de matematica Gigel este scos la tabla.Profesorul dicteaza trei numere si cere sa se verifice daca cele trei numere pot fi laturile unui triunghi.Ajutati-l pe Gigel sa afle rezultatul.
##Scriti un program care primeste numerele lui Gigel, care sunt mai mici ca 32000, si returneaza DA sau NU
a=int(input("Nr1"))
b=int(input("Nr2"))
c=int(input("Nr3"))
if (a<b+c) and (b<a+c) and (c<a+b):
    print(DA)
else: (NU)