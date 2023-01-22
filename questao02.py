while True:
    num = int(input('Digite um número:'))

    if num < 10:
        print(f'{num} é menor que 10.')
    if num % 2 == 0:
        print(f'{num} é par.')
    if num >= 8 and num <= 16:
        print(f'O número {num} está entre 8 e 16.')
    if num == 51 or num == 80:
        print(f'O número {num} é 51 0u 80.')
    if num == 101:
        break
   