import os
os.system ("CLS")

 #skapa en listvariabel med frukter

frukter = ["banan","melon","drakfrukt","kiwi","citron"]
raknare = 0
# skapa en for-loop som går igenom listan och x byter värde
print(">>>>>mina frukter<<<<<")
for x in frukter:

    print("gillar du",x,"? (j/n)")
    check = input()
    if check == "n":
       continue
    
    raknare = raknare + 1
print("_________________________")
print("listan hade" ,raknare ,"frukter")
raknare = 0
for y in "Oskar  v Fawcett":
    print(y)
    raknare = raknare + 1
print("mitt namn har", raknare-1,"bokstäver")