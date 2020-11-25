states = ['Imo', 'Abuja', 'Lagos', 'Ondo', 'Edo']

for s in states:
    print(s)

states_capital = {
    'Imo':'Owerri',
    'Abia':'Umuahia',
    'Anambra':'Awka',
    'Ebonyi':'Abakaliki',
    'Enugu':'Enugu'
}

for slim, ben in states_capital.items():
    print(slim, ben)


for x in states_capital:
    # print(x, states_capital[x])
    print(states_capital[x])

for x in states_capital.values():
    print(x)
