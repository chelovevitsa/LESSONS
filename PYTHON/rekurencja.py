# def fun(zmienna):
#     print(zmienna)
#     if zmienna < 10:
#         fun(zmienna + 1)

# fun(4)

# tab = [2, 4, 5, 7, 8]
# element_to_find = 7

# left = 0
# right = len(tab) - 1

# while left <= right:
#     mid = (left + right) // 2

#     if tab[mid] == element_to_find:
#         print(mid)
#         break

#     elif tab[mid] < element_to_find:
#         left = mid + 1

#     else:
#         right = mid - 1

# else:
#     print("Nie ma takiego elementu")


tab = [2, 4, 5, 7, 8]
element_to_find = 7

left = 0
right = len(tab) - 1
    
def binary_search(tab, left, right, x):

    if left <= right:
        mid = (left + right) // 2
        if tab[mid] == x:
            return mid
        elif tab[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
        return binary_search(tab, left, right, x)
    else:
        return -1

print(binary_search(tab, left, right, element_to_find))

