##se introduc 3 date de forma numar curent elev, punctaj.Afisati numarul elevului cu cel mai mare punctaj.
a=int(input("Nr curent 1 elev"))
x=int(input("Punctaj 1 elev"))
b=int(input("Nr curent 2 elev"))
y=int(input("Punctaj 2 elev"))
c=int(input("Nr curent 3 elev"))
z=int(input("Punctaj 3 elev"))
if (y>x ) and (y>z):
    print("Punctajul maxim il are elevulu cu nr curent", b)
if (z>y) and (z>x):
    print("Punctajul maxim il are elevul cu nr curent", c)
if (x>y) and (x==z):
    print("Punctajul maxim il are elevul cu nr curent", a)
if (x==y) and (x>z):
    print("Punctajul maxim il are elevul cu nr curent", a)
if (x==y) and (x==z):
    print("Punctajul maxim il are elevul cu nr curent", a)