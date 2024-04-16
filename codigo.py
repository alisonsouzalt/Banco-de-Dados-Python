menu_1 = """
    ========== SEJA BEM VINDO ==========
    |                                   |
    |             by. A.S               |
    |                                   |
    ========== BANCO DE DADOS ==========

"""

menu_2 = """

    [1] Cadastre-se
    [2] Login
    [0] Sair

"""

menu_3 = """

    [1] Cadastrar Produtos
    [2] Consultar Produtos
    [3] Deletar produtos
    [0] Sair

"""

escolha = 0
userName = "&"
login = "&"
password = 0
username_table = []
produtos_table = []

print(menu_1)
print(menu_2)

while True:
    escolha = int(input("Escolha uma opção acima: "))
    if escolha == 1:
        userName = input("Escolha o nome de seu usuário: ")
        username_table.append(userName)
        if username_table.count(userName) == 2:
            username_table.remove(userName)
            print("Usuário já existe!")
            print(f"=============================\n{menu_2}\n=============================")
        elif username_table.count(userName) == 1:  
            print("Cadastro realizado com sucesso!\n")
            print(menu_2)

    if escolha == 2:
        login = input("Digite seu usuário: ")
        if login in username_table[::]:
            print(f"Bem vindo ao nosso banco de Dados {login}!")

            print(menu_3)
            while login in username_table[::]:
                escolha_2 = int(input("Escolha uma opção acima: "))
                if escolha_2 == 1:
                    cadastro = input("Digite o produto que deseja cadastrar: ")
                    produtos_table.append(cadastro)
                    print("Produto cadastrado com sucesso!\n")
                    print("=============================")
                    print(menu_3)

                elif escolha_2 == 2:
                    for indice, produtos_table in enumerate(produtos_table):
                        print(f"{indice}: {produtos_table}")
                    print("Produtos consultados com sucesso!\n")
                    print("Digite [4] para voltar para o menu inicial!")

                elif escolha_2 == 3:
                    delete = input("Digite o nome do produto que deseja deletar: ")
                    produtos_table.remove(str(delete))
                    print("Produto deletado com sucesso!\n")
                    print("=============================")
                    print(menu_3)

                elif escolha_2 == 4:
                    print(f"=============================\n{menu_3}\n=============================")

                elif escolha_2 == 0:
                    print("leaving...")
                    print("Usuário finalizado!")
                    print(f"=============================\n{menu_2}\n=============================")
                    break


        else:
            print("Usuário incorreto!\n")
            print(menu_2)


    elif escolha == 0:
        print("Obrigado por utilizar nosso sistema!")
        break
        


