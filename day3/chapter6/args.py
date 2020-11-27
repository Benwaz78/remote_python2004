# def add(var1, var2):
#     add = var1 + var2
#     print(add)

# add(2, 3, 4)

def add(*args):
    total = 1
    for n in args:
        total +=n
    print(total)

add(2,3,4,5)

def names(*args):
    for name in args:
        print(name)

names('Benedict', 'Alabi', 'Joshua', 'Ayeni')