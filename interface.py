"""
Módulo de Interface (Interação com Usuário)

Responsável por toda a comunicação do sistema com o usuário via terminal.
Gerencia a exibição do menu, formatação das listas na tela (prints), 
além da coleta e validação das entradas digitadas (inputs).
"""

from modelo import noticias, adicionar_noticia
from servico import analisar_texto

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