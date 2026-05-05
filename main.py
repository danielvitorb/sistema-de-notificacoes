# sistema de noticias

def adicionar_noticia_automaticamente():
    """Coleta o texto do usuário e aplica a regra de negócio para classificar a notícia."""
    texto = input("Digite o texto da notícia: ")
    classificacao = analisar_texto(texto)
    print(f"A notícia foi avaliada automaticamente como: {classificacao}")
    
    adicionar_noticia(texto, classificacao)


def menu():
    """Exibe o menu interativo e gerencia as opções selecionadas pelo usuário."""
    while True:
        print("--- Menu Principal ---")
        print("1 - Adicionar notícia manualmente")
        print("2 - Adicionar notícia automaticamente")
        print("3 - Listar notícias")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_noticia_manualmente()
        elif opcao == "2":
            adicionar_noticia_automaticamente()
        elif opcao == "3":
            listar_noticias()
        elif opcao == "4":
            print("Encerrando o sistema...")
            break
        else:
            print("Erro: Opção inválida. Digite um número de 1 a 4.\n")


if __name__ == "__main__":
    menu()