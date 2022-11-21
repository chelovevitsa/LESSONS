lista = [3, 5, 0, -2, 7, -3]

najmniejsza = None
najwieksza = None

for i in lista:
    if najmniejsza == None or najmniejsza > i:
        najmniejsza = i
    if najwieksza == None or najwieksza < i:
        najwieksza = i

print('Najmniejsza liczba to: ', najmniejsza)
print('Najwieksza liczba to: ', najwieksza)