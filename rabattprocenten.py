import os
os.system("CLS")
ordinariepris = int(input("ordinariepris"))

procent = int(input("procent"))
ff = (100-procent)/100
produkt = ff * ordinariepris 


print(ordinariepris, "*" ,ff, "=", produkt )
