class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

msg = 'ativo' if restaurante_praca.ativo else 'desativado'
print(msg)
restaurante_pizza = Restaurante()

restaurante_pizza_place = Restaurante()
restaurante_pizza_place.nome = 'Pizza Place'
restaurante_pizza_place.categoria = 'Fast food'

if restaurante_pizza_place.categoria == 'Fast food':
    print('sim')

restaurantes = [restaurante_praca, restaurante_pizza]

restaurante_pizza_place.ativo = True
print(vars(restaurante_pizza_place))