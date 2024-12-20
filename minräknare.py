import os
os.system("CLS")
while True:
    print ("||=====================||")
    print ("||---Min Miniräknare---||")
    print ("||=====================||")
    
    
    tal1 = int(input("skriv in tal 1: "))
    tal2 = int(input("skriv in tal 2: "))
    Räknesätt = (input("välj räknesätt (+ - * /) : "))
    
    Summa = tal1 + tal2
    Differans = tal1 - tal2
    produkt = tal1 * tal2
    kvot = tal1 / tal2
    plus=Räknesätt
    
    if Räknesätt == "+" :
        print(tal1, "+", tal2, "=",Summa)
    elif Räknesätt == "-":
        print(tal1, "-", tal2, "=",Differans)
    elif Räknesätt == "*":
        print(tal1, "*", tal2, "=",produkt)
    elif Räknesätt == "/":
        print(tal1, "/", tal2, "=",kvot)

    Räknaigen = (input("Vill du köra igen ? (j/n) : "))
    if Räknaigen == "j" :
        print("Då kör vi")
    if Räknaigen == "n":
        print("Tack för att du räknade")
   

 
