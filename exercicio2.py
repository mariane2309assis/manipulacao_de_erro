while True:
    print("=============menu===========")
    print("Opção 1 - Criar  nome: ")
    print("Opção 2 - Sair do programa: ")
    print("============================")
    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
            with open("nomes.txt", "a") as arquivo:
                novonome = input("Digite o nome: ")
                arquivo.write(f"{novonome}\n")

    elif opcao == 2:
        print("saindo do programa")
        break

