#
# print(bool([]))
#
# print(False or [] or 1)
#
#
# def generate_number(N: int, M:int, prefix=None):
#     """Генерирует все числа в N-ричной системе счисления (N <=10 ) длины M"""
#     prefix = prefix or []
#     if M == 0:
#         print(prefix)
#         return
#     for digit in range(N):
#         prefix.append(digit)
#         generate_number(N, M-1, prefix)
#         prefix.pop()
#
# # generate_number(2, 10)
#
# def find(number, A):
#     """ищет number в А и возвращает True если есть"""
#     for x in A:
#         if number == x:
#             return True
#     return False
#
# def generate_permutations(N:int, M:int=-1, prefix=None):
#     """Генерация всех перестановок N чисел в M позициях, начиная с префиксом prefix"""
#     M = N if M == -1 else M
#     prefix = prefix or []
#     if M == 0:
#         print(*prefix, end=', ')
#         # print(prefix,end='')
#         return
#     for number in range(1, N+1):
#         if find(number, prefix):
#             continue
#         prefix.append(number)
#         generate_permutations(N, M-1, prefix)
#         prefix.pop()
#
# generate_permutations(5)
#

from collections import deque

def is_inside_complex(x, y, K, L):
    return 1 <= x <= K and 1 <= y <= L

def find_second_component(K, L, c1, t1, c2, t2):
    # Первая компонента антидота
    target1 = (c1, t1)
    # Вторая компонента антидота
    target2 = (c2, t2)

    # Переменные для отслеживания посещенных комнат и дней
    visited = set()
    days = 0

    # Очередь для BFS
    queue = deque([(1, 1)])  # Команда начинает с (1, 1)

    while queue:
        current_level_size = len(queue)
        for _ in range(current_level_size):
            x, y = queue.popleft()
            if (x, y) == target1 or (x, y) == target2:
                # Если мы нашли одну из компонент, то ищем вторую
                target = target2 if (x, y) == target1 else target1
                visited = set()  # Сбрасываем посещенные комнаты
                queue.clear()    # Очищаем очередь для поиска второй компоненты
                queue.append(target)
                days += 1
                break

            # Добавляем соседние комнаты в очередь, если они внутри комплекса и не посещены
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if is_inside_complex(new_x, new_y, K, L) and (new_x, new_y) not in visited:
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))

        days += 1

    return days

# Ввод исходных данных
K, L = map(int, input().split())
c1, t1 = map(int, input().split())
c2, t2 = map(int, input().split())

# Вывод результата
print(find_second_component(K, L, c1, t1, c2, t2))