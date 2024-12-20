import os,random,time
os.system("CLS")
slumptal = random.randint(1, 100)
försök = 1
highscore = 100
while True:
#här visar den att man ska gissa på en siffra 
    print("Försök: ", försök)
    gissning= int(input("Gissa på en siffra: "))

#här visar den på vilket försök man gissade rätt på
    if gissning == slumptal:    
        print("Du gissade rätt på försök nummer:", försök, )
       
 # Kolla om highscore
        if försök<highscore:
            highscore = försök
        print("||>>> Ditt nya highscore :",highscore,"<<<||")
       
# Spela igen?
        spelaigen = (input("Vill du köra igen ? (j/n) : "))
#Ja=då kör vi en till gång
        if spelaigen == "j":
            print("Då kör vi")
#nej=då är spelet slut och den tackar för man har spelat nedanför
        if spelaigen == "n":
            print("Tack för att du spelade gissa siffran")
            break
 #här säger den om man ska gissa lägre eller högre  
    elif gissning > slumptal:
        print("gissa lägre")
    elif gissning < slumptal:
        print("gissa högre")
 
    försök = försök +1
