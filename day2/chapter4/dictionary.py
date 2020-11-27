states = {
    'Imo':'Owerri',
    'Abia':'Umuahia',
    'Anambra':'Awka',
    'Ebonyi':'Abakaliki',
    'Enugu':'Enugu'
}

print(states['Imo'])
states['Lagos'] = 'Ikeja'
print(states)

del states['Imo']

print(states.get('Anambra'))
print(states)
