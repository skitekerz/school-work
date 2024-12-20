import os
os.system("CLS")
 #här matar man in spelarna som ska spela 
spelare1 = input("Mata in första spelare :")
spelare2 = input("Mata in andra spelaren :")
 
import os,random,time
poäng_spelare1 = 0
poäng_spelare2 = 0
Highscore = 100
antalslag1 = 0
vinst_spelare1 = 0
vinst_spelare2 = 0
#här har jag gjort en while true loop
while (poäng_spelare1 or poäng_spelare2 < 100):
    time.sleep(0.1)
   
    tärning_spelare1 = random.randint(1,6)
    tärning_spelare2 = random.randint(1,6)
    poäng_spelare1 += tärning_spelare1
    poäng_spelare2 += tärning_spelare2
 
    antalslag1 = antalslag1 + 1
   #här räknar det ut slag en óch totala poäng
    print(spelare1, "slog", tärning_spelare1, "(Total poäng",poäng_spelare1,")")
    print(spelare2, "slog", tärning_spelare2, "(Total poäng",poäng_spelare2,")")  
   #här är if satserna som visar om spelare 1 eller 2 har vunnit
    if poäng_spelare1>=100:
        vinst_spelare1= vinst_spelare1 + 1
        print("Grattis", spelare1,"du har vunnit med",poäng_spelare1,"poäng"," Vinster:",vinst_spelare1)
               
    elif poäng_spelare2>=100:
        vinst_spelare2= vinst_spelare2 + 1
        print("Grattis", spelare2, "du har vunnit med",poäng_spelare2,"poäng",". Vinster:",vinst_spelare2)
   #här printar den totala vinster
    print("Totala vinster:",spelare1, "<",vinst_spelare1,">","och",spelare2,"<",vinst_spelare2,">")
   #här visar den vem som fick 100 av spelare 1 eller 2 och sedan highscore och antalslag
    if poäng_spelare1 >= 100 or poäng_spelare2 >= 100:
        if antalslag1<Highscore:
            Highscore = antalslag1
            print("||>>> Nytt highscore :",Highscore,"<<<||")
        else:
            print("Antal slag",antalslag1,". Highscore:",Highscore)
 
        spelaigen = (input("Vill du köra igen ? (j/n) : "))
   #här visar den om man vill spela igen och genom variabler att den noll ställer
        if spelaigen == "j" :
            print("Då kör vi")
            antalslag1 = 0
            poäng_spelare1= 0
            poäng_spelare2=0
           
   #här visar den att om man säger nej till att köra igen och tackar sedan och en break på slutet    
        if spelaigen == "n":
            print("Tack för att du körde")
            break