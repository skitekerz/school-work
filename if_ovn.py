import os,time
os.system("CLS")
#övningar på if satser(vilkor sant eller falskt)
while True:

    a = int(input("skriv in ett tal: "))
    b = int(input("skriv in ett tal till: "))
    if a<b:
        print(a,"är mindre än" ,b)
    elif a>b:
        print(a, "är större än" ,b)
    else:
        print(a, "är lika stor som" ,b)

    time.sleep(2)
    os.system("CLS")