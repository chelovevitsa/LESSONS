tab = [2, 4, 5, 7, 8]
element_to_find = 7

left = 0
right = len(tab) - 1

while left <= right:
    mid = (left + right) // 2

    if tab[mid] == element_to_find:
        print(mid)
        break

    elif tab[mid] < element_to_find:
        left = mid + 1

    else:
        right = mid - 1

else:
    print("Nie ma takiego elementu")