usuario_esperado = 'Denis'
senha_esperada = '123'

usuario_informado = input('Informe um usuario\n')
senha_informada = input('Informe uma senha\n')

if usuario_esperado == usuario_informado and senha_esperada == senha_informada:
    print('Acesso permitido')
else:
    print('Acesso negado')    