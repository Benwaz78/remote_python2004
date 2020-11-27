def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(name='Slim', age=30, color='Fair', height='Tall')

def states_capital(**kwargs):
    for state, capital in kwargs.items():
        print(f'The capital of state {state} is {capital}')

states_capital(Imo='Owerri', Lagos='Ikeja', Niger='Minna')
