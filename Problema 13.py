##la un concurs se dau ca premi primelor 100 de concurenti, tricouri de culoare alba, rosie, albastra si neagra in aceasta secvennta. Ionut este pe locul x, ce culoare va avea tricoul lui
x=int(input("Ionel este pe locul"))
if x<=100:
    if (x%4)==1:
        print("Ionel va primi tricou de culoare alba")
    if (x%4)==2:
        print("Ionel va primi tricou de culoare rosie")
    if (x%4)==3:
        print("Ionel va primi tricou de culoare albastra")
    if (x%4)==4:
        print("Ionel va primi tricou de culoare neagra")
else:
    print("Ionel nu va primi nici un tricou")