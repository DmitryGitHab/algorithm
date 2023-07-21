
print(bool([]))

print(False or [] or 1)


def generate_number(N: int, M:int, prefix=None):
    """Генерирует все числа в N-ричной системе счисления (N <=10 ) длины M"""
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()

# generate_number(2, 10)

def find(number, A):
    """ищет number в А и возвращает True если есть"""
    for x in A:
        if number == x:
            return True
    return False

def generate_permutations(N:int, M:int=-1, prefix=None):
    """Генерация всех перестановок N чисел в M позициях, начиная с префиксом prefix"""
    M = N if M == -1 else M
    prefix = prefix or []
    if M == 0:
        print(*prefix, end=', ')
        # print(prefix,end='')
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()

generate_permutations(5)
