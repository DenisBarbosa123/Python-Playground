x = int(input('Informe valor de X\n'))
y = int(input('Informe valor de Y\n'))

if x > 0 and y > 0:
    print('Primeiro quadrante')
elif x < 0 and y > 0:
    print('Segundo quadrante')
elif x < 0 and y < 0:
    print('Terceiro quadrante')
elif x > 0 and y < 0:
    print('Quarto quadrante')
else:
    print('ponto está localizado no eixo ou origem')              