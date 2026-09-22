 # zad 1.1 Funkcja wynik zwraca coś... 
print("Zadanie 1.1")   
def wynik(i):
    if i < 3:
        return 1
    elif i%2 == 0:
        return wynik(i-3) + wynik(i-1) +1
    else:
        return wynik(i-1)%7
print("Zadanie 1.1")   
for i in range(20):
   print(i, wynik(i))

# zad 1.2
print("Zadanie 1.2") 
print("E(i) = E( i-1 ) + E( i-3 ) dla parzystego i > 2")
print("E(i) = E( i-1 ) dla nieparzystego i > 2")

# zad 1.3
print("Zadanie 1.3")   
def wynik_iter(n):
    w = 1001*[0]
    w[0] = 1
    w[1] = 1
    w[2] = 1
    maks = 1
    for i in range(3,n+1):
        if i%2 == 0:
            w[i] = w[i-3] + w[i-1] +1
        else:
            w[i] = w[i-1]%7
        if w[i] > maks:
            maks = w[i]
    return maks
print ("maks:", wynik_iter(1000))    

