##Elevii in clasa a v-a sunt repartizatii in ordinea  mediei a clesei a IV-a, Radu este pe oridinul x in clasa mediilor, in ce clasa va fi repartizat?(A, B , C , D sau E)
x=int(input("Radu este pe locul"))
n_clasa= x//25
if x%25!=0:
    n_clasa +=1
if n_clasa<=5:
    if n_clasa==1:
        print("Clasa A")
    elif n_clasa==2:
        print("Clasa B")
    elif n_clasa==3:
        print("Clasa C")
    elif n_clasa ==4:
        print("Clasa D")
    else:
        print("Clasa E")
else:
        print("Nu mai sunt clase")