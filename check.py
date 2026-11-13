def f(n):
    return 11**(n+1) + 12**(2*n-1) # вираз зі свого варіанта
m = 133 # дільник зі свого варіанта
bad = [n for n in range(1, 101) if f(n) % m != 0]
print("Контрприкладів не знайдено" if not bad else bad)