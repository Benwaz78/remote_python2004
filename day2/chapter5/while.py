
# x = 1
# while x <= 5:
#     print(x)
#     x += 1

# name='Benedict'

states = ['Imo', 'Lagos', 'Abia', 'Abuja', 'Oyo']
x = 0
while x < len(states):
    print(states[x])
    if x == 3:
        break
    x += 1

total = 0
x = 1

while x <= 1000:
    total += x
    x += 1
print(total)

x = 1
while x <= 20:
    if x % 2 == 0:
        print(x)
    x += 1

x = 2
while x <= 20:
    print(x)
    x += 2