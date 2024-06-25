numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Denis', 'Maria', 'Denise', 'José']
anos = [1998, 2024]
numero_impar = 0
total_numeros=0
for numero in numeros:
    print(numero)
    if numero % 2 != 0:
        numero_impar += numero
print(numero_impar)

for nome in nomes:
    print(nome)
print()

for ano in anos:
    print(ano)
print()

for i in range(10, 0, -1):
    print(i)


numero_tabuada = int(input('Informe um numero '))

for numero in numeros:
    result=numero_tabuada*numero
    print(f'{numero_tabuada}x{numero} = {result}')

for numero in numeros:
    try:
        total_numeros+=numero
    except:
        print('Erro ao somar numeros')

print(f'Total numeros: {total_numeros}')

try:
    print(f'Media numeros: {total_numeros/len(numeros)}')
except:
    print('Erro ao fazer media')    