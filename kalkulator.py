import time
def time():
    time = 0
    time.sleep(10)
    time = time + 1
def lat():
    
    while True:
        file = open("история заданий.txt", "a")
        a = input("One number:" )
        if str(a) == "!":
            print("OK")
            break
        b = input("Two number:" )
        if str(b) == "!":
            print("OK")
            break
        rez = int(a)+int(b)
        print("Otvet:" + str(rez))
        file.write("\n" + str(a) + "+" + str(b) + "=" + str(rez))
        file.close()
lat()
close = input()
if close == "++":
    lat()
