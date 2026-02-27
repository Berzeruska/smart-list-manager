def exibir_lista_compras(itens):
    """
    Função que recebe uma lista de compras e exibe todos os itens.
    
    Parâmetro:
        itens (list): Lista contendo os itens de compras
    """
    print("\n" + "="*40)
    print("LISTA DE COMPRAS COMPLETA:")
    print("="*40)
    print(itens)
    
    print("\n" + "="*40)
    print("ITENS INDIVIDUALIZADOS:")
    print("="*40)
    
    # Utilizando for para percorrer a lista
    for i, item in enumerate(itens, 1):
        print(f"{i}. {item}")
    
    print("="*40 + "\n")


# Programa Principal
def main():
    # Solicitar ao usuário quantos itens ele deseja adicionar
    while True:
        try:
            quantidade = int(input("Quantos itens você deseja adicionar à lista de compras? "))
            if quantidade <= 0:
                print("Por favor, digite um número maior que zero!\n")
                continue
            break
        except ValueError:
            print("Erro! Digite um número válido.\n")
    
    # Lista para armazenar os itens
    itens = []
    
    # Utilizar for para pedir que o usuário digite os itens
    for contador in range(quantidade):
        item = input(f"Digite o item {contador + 1}: ")
        if item.strip():  # Verifica se o item não está vazio
            itens.append(item)
        else:
            print("Item vazio! Tente novamente.")
            contador -= 1
    
    # Chamar a função para exibir a lista
    if itens:
        exibir_lista_compras(itens)
    else:
        print("\nNenhum item foi adicionado à lista!")


# Executar o programa
if __name__ == "__main__":
    main()
