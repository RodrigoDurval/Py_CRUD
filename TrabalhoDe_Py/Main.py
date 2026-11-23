#Colocando Notas de Ajuste

#Possivel Erro (Bug) no Parte 5 do Codigo
# Item 5 está com erro de "Caminho" Volta para a "tela" de selecionar o item mas
# não para alterar sua quantidade
#

# ------------------------------- Começo da Lista ---------------------------
lista = []

while True:

    
    print(" ")
    print('*'* 30)
    print("*MENU DE OPÇÕES*")
    print('*'* 30)
    print(" ")
    print('1-Incluir')
    print('2-Remover')
    print('3-Mostrar')
    print('4-Editar Nome do Item')
    print('5-Editar Quantidade')
    print('6-Apagar')
    op = str(input("Digite a Opção a ser selecionada ou 'FIM' para encerrar: "))

    if op.upper() == "FIM":
        print("Encerrando Programa")
        break

    # ------------------------------- Fim da Lista ---------------------------

    
# ------------------------------- Começo das (Funções) ---------------------------

# ------------------------------- Começo da 1 Incluir ---------------------------
    elif op == "1":
        while True:
            nome = str(input("Digite o Nome, ou digite X para sair: "))
            if nome == "X":
                break
            qnt = int(input("Digite a Quantidade: "))
                            
            lista.append([nome, qnt])

    # ------------------------------- Começo da 2 Incluir ---------------------------
    elif op == "2":
        while True:
            if not lista:
                print("           ")
                print("=" * 30)
                print("   A lista esta vazia")
                print("=" * 30)
                break
            
            for numero, item in enumerate(lista, start=1):
                print(numero, item)
                
            remover = input("Digite o Item a ser Removido ou X para sair: ")
            if remover.upper() == "X":
                break
            
            remover = int(remover)
            
            if remover >= 1 and remover <= len(lista):
                produto = lista.pop(remover - 1)
                print(f"Item {remover} removido")
                
            else:
                print("Produto não encontrado, tente novamente")    

        # ------------------------------- Começo da 3 Incluir ---------------------------
    elif op == "3":
        if not lista:
            print("           ")
            print("=" * 30)
            print("   A lista esta vazia")
            print("=" * 30)
        else:    
            print("           ")
            print("=" * 30)
            print("    Lista dos Produtos")
            print("=" * 30)
            for numero, item in enumerate(lista, start=1):
                print(f"{numero} - Nome: {item[0]} | Quantidade: {item[1]}")
            print("=" * 30)
            print("           ")


    # ------------------------------- Começo da 4  ---------------------------
    elif op == "4":
        while True:
            if not lista:
                print("=" * 30)
                print("   A lista esta vazia")
                print("=" * 30)
                break
    
            for numero, item in enumerate(lista, start=1):
                print(f"{numero} - Nome: {item[0]} | Quantidade: {item[1]}")
    
            editar = input("Digite o número do produto ou X para sair: ")
    
            if editar.upper() == "X":
                break
    
            editar = int(editar)
    
            if editar >= 1 and editar <= len(lista):
                novonome = input("Digite o novo nome do produto: ")
    
                lista[editar - 1][0] = novonome
    
                print("Nome atualizado com sucesso!")
    
            else:
                print("Produto não encontrado!")
# ------------------------------- Começo da 5  ---------------------------
    elif op == "5":
        while True:
            if not lista:
                print("=" * 30)
                print("   A lista esta vazia")
                print("=" * 30)
                break
    
            for numero, item in enumerate(lista, start=1):
                print(f"{numero} - Nome: {item[0]} | Quantidade: {item[1]}")
    
            editar = input("Digite o número do produto ou X para sair: ")
            
            if editar.upper() == "X":
                break
            
        if not editar.isdigit():
                print("Digite apenas números!")
                continue
        
        editar = int(editar)
    
        if editar >= 1 and editar <= len(lista):
                print("1 - Adicionar quantidade")
                print("2 - Remover quantidade")
    
                opqnt = input("Escolha uma opção: ")
    
                if opqnt == "1":
                    adicionar = int(input("Quanto deseja adicionar? "))
                    lista[editar - 1][1] += adicionar
                    print("Quantidade atualizada!")
    
                elif opqnt == "2":
                    remover = int(input("Quanto deseja remover? "))
    
                    if remover <= lista[editar - 1][1]:
                        lista[editar - 1][1] -= remover
                        print("Quantidade atualizada!")
                    else:
                        print("Quantidade insuficiente!")
    
                else:
                    print("Opção inválida!")

                    break

        else:
            print("Produto não encontrado!")


    # ------------------------------- Começo da 6 Incluir ---------------------------
    elif op == "6":
        while True:
            print("Deletar toda a lista de Produtos")
            deletar = input("Vocẽ quer deletar permanentimente toda lista de Produtos? (s/n): ")
            if deletar.lower() == "n":
                print("Comando cancelado")
                break
            elif deletar.lower() == "s":
                lista.clear()
                print("Lista deletada com sucesso")
                break
            else:
                print('Opções invalida, tente novamente')
    
    else:
        print("Opção inválida!")


        # "Desmenbrando" Codigo 
        
        # O Copilot nos deu a sugestão de usar o "isdigit()"
        #O método isdigit() verifica se uma string contém apenas dígitos numéricos.