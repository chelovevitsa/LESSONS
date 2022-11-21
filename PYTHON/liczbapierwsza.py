def is_prime(number):
    if number == 2:
        return True

    for divided in range(2, number // 2 + 1):
        if number % divided == 0:
            return False

    return True

n = int(input())
num_to_check = 2
while n > 0:
    if is_prime(num_to_check):
        print(num_to_check)
        n -= 1
    num_to_check += 1

while n>0:
    if is_prime(num_to_check):
        print(num_to_check)
        n -= 1
    num_to_check += 1