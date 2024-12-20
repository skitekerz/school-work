import os,time
os.system ("CLS")
while True:
    ålder = float(input("skriv in ålder: "))

    if ålder >= 0 and ålder <= 12:
        print("vit")
    elif ålder >= 13 and ålder <= 18:
        print("grön")
    elif ålder >= 19 and ålder <= 25:
        print("röd")
    elif ålder >= 26 and ålder <= 99:
        print("blå")

    time.sleep(2)
    os.system("CLS")
