import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}
]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    ''' Essa função é responsavel por exibir as oppções do menu '''
    print('1 . Cadastrar Restaurante')
    print('2 . Lista Restaurante')
    print('3 . Alternar estado do Restaurante')
    print('4 . Sair\n')

def finalizar_app():
    exibir_subtitulo('Encerrar programa')

def opcao_invalida():
    print('Opcão Invalida!\n')
    voltar_menu_principal()

def cadastrar_novo_restaurante():
    ''' Essa função é responsavel por cadastrar restaurante '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite nome do restaurante:\n')
    categoria = input(f'Digite nome do categoria do restaurante {nome_do_restaurante}:\n')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restautante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu_principal()

def listar_restaurantes():
    ''' Essa função é responsavel por listar restaurantes '''
    exibir_subtitulo('Listando todos os restaurantes cadastrados')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(21)} | Status')
    for restaurante in restaurantes:
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {restaurante['nome'].ljust(20)} |  {restaurante['categoria'].ljust(20)} | {ativo}')
    voltar_menu_principal()

def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def exibir_subtitulo(texto):
    ''' Essa função é responsavel por exibir subtitulo '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(f'{texto}')
    print(linha)
    print()

def alternar_estado_restaurante():
    ''' Essa função é responsavel por alternar estado do restaurante '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O Restaurante {restaurante['nome']} foi ativado com sucesso' if restaurante['ativo'] else f'O Restaurante {restaurante['nome']} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não foi encontrado')
         
    voltar_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você Escolheu opção {opcao_escolhida}')
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()     
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
