okPin = "0805"
failedAttempts = 0
maxFail = 3
done = False

while failedAttempts < maxFail or done==True:
    pin = input("Podaj Pin: ")
    if pin==okPin:
        print("OK!")
        done = True
    else:
        if failedAttempts < maxFail-1:
            print("Została zablokowana")
        else:
            print("Nieprawidłowy PIN")
        failedAttempts = failedAttempts + 1