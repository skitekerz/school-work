import os
os.system("CLS")

while True:

   
   tal = int(input("skriv in ett tal" ))
   tal2 = int(input("skriv in ett tal till"))
   if tal % tal2 == 0:
    print(tal,"delbart")

   else:
    rest = tal - tal//7 * 7
    print(tal,"ej delbart med" ,tal2, "resten blir ",rest)

