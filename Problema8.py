##Sa se afiseze cel mai mare numar par dintre doua introduse in calculator
a=int(input("Nr 1"))
b=int(input("Nr 2"))
if (a%2==0) and (b%2!=0):
    print(a)
if (a%2!=0) and (b%2==0):
    print (b)
if (a%2!=0) and (b%2!=0):
    print("nu sunt pare")