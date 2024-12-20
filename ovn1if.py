import os
os.system ("CLS")

däckdjup = float(input("skriv in ett mönsterdjup i mm: "))
lagligt = 1.6

if däckdjup<lagligt:
    print("olagligt däck")
elif däckdjup>=lagligt:
    print("lagligt däck")