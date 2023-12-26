result = 1
for i in range(1, 20):
    if i % 3 == 0 or i % 5 == 0:
        result *= i
print(result)

