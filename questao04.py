def concatenar(param1, param2):
    return param1+','+param2

def print_parametros():
    param1 = input('Digite uma palavra:')
    param2 = input('Digite uma palavra:')

    print(concatenar(param1, param2))

print_parametros()