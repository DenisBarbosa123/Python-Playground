from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_praca.alternar_estado()

restaurante_praca.receber_avaliacao('Denis', 10)
restaurante_praca.receber_avaliacao('Maria', 8)
restaurante_praca.receber_avaliacao('José', 5)
restaurante_praca.receber_avaliacao('Denise', 1)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()