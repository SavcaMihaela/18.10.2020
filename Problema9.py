##Pe omasa de biliard sunt bile albe, rosii si verzi.Din fiecare culoare sunt bile de doua dimensiuni: mari si mici
##Sa se afiseze cate bile sunt in total pe masa de biliard. Cate bile sunt mai multe mari sau mici, de ce culoare sunt mai numeroase bie
xa=int(input("Bile albe mari"))
xr=int(input("Bile rosii mari"))
xv=int(input("Verzi mari"))
ya=int(input("Albe mici"))
yr=int(input("Rosii mici"))
yv=int(input("Verzi mici"))
tx=xa+xr+xv
ty=ya+yr+yv
print("Numarul total de bile", tx+ty, "bile")
if (tx>ty):
    print("Mai multe bile mari",tx, "bile")
if (ty>tx):
    print("Mai multe bile mici", ty, "bile")
if (tx==ty):
    print("Numarul de bile mari si mici este egal", ty, "bile")
if ((xa+ya>xr+yr) and (xa+ya>xv+yv)):
    print("Cele mai multe sunt bile albe", xa+ya, "bile")
if ((xr+yr>xa+ya) and (xr+yr>xv+yv)):
    print("Cele mai multe sunt bile rosii", xr+yr,"bile")
if ((xv+yv>xr+yr) and (xv+yv>xa+ya)):
    print("Cele mai multe sunt bile verzi", xv+yv, "bile")