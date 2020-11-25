even_numbers = []
for e in range(0, 20, 2):
    even_numbers.append(e)
print(even_numbers)

print('LIST COMPREHENSION (Shorthand)')

even_numbers = [e for e in range(0, 20, 2)]
print(even_numbers)

double_even_numbers = []
for n in range(10):
    if n % 2 == 0:
        square = n**2
        double_even_numbers.append(square)
print(double_even_numbers)
print('LIST COMPREHENSION (Shorthand)')
double_even_numbers = [n**2 for n in range(10) if n % 2 == 0]
print(double_even_numbers)
