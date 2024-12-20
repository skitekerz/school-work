import os
os.system("CLS")

basen = int(input(" basen"))
höjden = int(input("höjden"))
area = basen * höjden / 2

print(basen, "*" ,höjden, "/" ,2, "=" ,area )


ordinariepris = int(input("ordinariepris"))

rabatt = 0.85 * ordinariepris 

print(ordinariepris, "*" ,0.85, "=", rabatt )