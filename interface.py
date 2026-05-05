def listar_noticias():
    """Exibe todas as notícias cadastradas no sistema no terminal."""
    if not noticias:
        print("Nenhuma notícia cadastrada no momento.\n")
        return

    print("\n--- Lista de Notícias ---")
    for i, noticia in enumerate(noticias, 1):
        print(f"Notícia {i}")
        print(f"Texto: {noticia['texto']}")
        print(f"Classificação: {noticia['classificação']}")
        print("-------------------")
    print()

def adicionar_noticia_manualmente():
    """Coleta os dados do usuário para adicionar uma notícia definindo a classificação."""
    texto = input("Digite o texto da notícia: ")
    
    # Validação de entrada para a classificação
    classificacoes_validas = ["confiável", "duvidosa", "falsa", ""]
    classificacao = input("Digite a classificação (confiável, duvidosa, falsa) ou aperte Enter para análise automática: ").strip().lower()
    
    while classificacao not in classificacoes_validas:
        print("Erro: Classificação inválida. Escolha entre as opções fornecidas.")
        classificacao = input("Digite a classificação (confiável, duvidosa, falsa) ou aperte Enter: ").strip().lower()

    if classificacao == "":
        classificacao = analisar_texto(texto)
        print(f"Análise automática aplicada. Classificação: {classificacao}")
        
    adicionar_noticia(texto, classificacao)