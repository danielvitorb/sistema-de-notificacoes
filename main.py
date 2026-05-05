# sistema de noticias

noticias = []

def adicionar_noticia(texto, classificacao=None):
    """
    Adiciona uma nova notícia à lista global.
    Aplica validação para impedir a inserção de textos vazios.
    Se a classificação não for informada, adota 'duvidosa' como padrão.
    """
    texto_limpo = texto.strip()
    
    if not texto_limpo:
        print("Erro: Não é possível adicionar uma notícia sem texto.")
        return

    noticia = {
        "texto": texto_limpo,
        "classificação": classificacao if classificacao is not None else "duvidosa"
    }
    noticias.append(noticia)
    print("Notícia adicionada com sucesso!\n")


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


def analisar_texto(texto):
    """
    Analisa o texto de uma notícia e retorna uma classificação de confiabilidade.
    Aumenta o score de falsidade caso falte fonte, haja excesso de exclamações, 
    termos sensacionalistas ou o texto seja muito curto.
    """
    score = 0
    texto_upper = texto.upper() 

    if "FONTE" not in texto_upper:
        score += 1

    if "!!!" in texto:
        score += 1

    if "URGENTE" in texto_upper:
        score += 1

    if len(texto.strip()) < 10:
        score += 1

    # Retorna a classificação com base na pontuação
    if score == 0:
        return "confiável"
    elif score == 1:
        return "duvidosa"
    else:
        return "falsa"


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