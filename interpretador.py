expressao = input('Digite uma expressão matemática no seguinte formato: int(espaço)(+;-;*;/)(espaço)int): ').strip()
x,y,z = expressao.split()
x = int(x)
z = int(z)

if y == '+':
    resultado = x + z
elif y == '-':
    resultado = x - z
elif y == '*':
    resultado = x * z
elif y == '/':
    if z == 0:
        resultado = ('Indet')
    else:
        resultado = x / z

if isinstance(resultado, str):
    print('Resultado indeterminado.')
else: print(round((float(resultado)),1))
