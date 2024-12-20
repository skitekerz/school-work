import os
os.system ("CLS")

bensin = int(input("tankad volym"))
prisperliter = int(input("pris per liter"))
1

pris = bensin * prisperliter
print("-------------------------------")
print("betalda kronor", pris, ("kr"))
print("-------------------------------")