pessoa = {
    'nome': 'Denis',
    'idade': 26,
    'cidade': 'Pouso Alegre',
    'estado': 'MG',
    'país': 'BR'
}

print(f'Idade {pessoa['idade']}\n')
nova_idade = int(input('Informe nova idade\n'))
pessoa['idade'] = nova_idade
print(f'Idade {pessoa['idade']}\n')
pessoa['profissão'] = 'Desenvolvedor'
print(f'Profissão {pessoa['profissão']}\n')
print(pessoa)
pessoa.pop('país')
print(pessoa)

quadrados = {}
for num in range(1, 6):
    quadrados[num] = num**2
print(quadrados)

