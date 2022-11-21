
def metoda(f, x0, x1, n):
    h = (x1-x0) / n
    met = 0
    for i in range(n):
        x = h * i + x0
        m = eval(f)
        x = h *(i+1) + x0
        m1 = eval(f)
        #print(i)
        #i =  x0 + x * i
        #m = eval(f)
        #i = x0 + x * (i+1)
        #m1 = eval(f)
        met += (m + m1) /2 * h
        #print(m)
        #print(m1)
        print(x, m,m1, met)
    return met

def trap(wywod):
    funkcja = input("Funkcja: ")
    poczatek = float(input("Początek przedziału: "))
    koniec = float(input("Koniec przedziału: "))
    liczba_p = int(input("Liczba przedziałow: "))
    print(metoda(funkcja, poczatek, koniec, liczba_p))

if __name__ == '__main__':
    trap(metoda)