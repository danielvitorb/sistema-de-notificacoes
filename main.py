# sistema de noticias

noticias = []

# função que faz tudo
def adicionar_noticia(texto, classificacao=None):
    # essa função adiciona uma notícia na lista de notícias
    if texto != "":
        noticia = {}
        noticia["texto"] = texto
        if classificacao == None:
            noticia["classificação"] = "duvidosa"
        else:
            noticia["classificação"] = classificacao
        noticias.append(noticia)
    else:
        print("Não é possível adicionar uma notícia sem texto.")


def listar_noticias():
    # lista todas as notícias
    for noticia in noticias:
        print("Texto:", noticias[noticia]["texto"])
        print("Classificação:", noticias[noticia]["classificação"])
        print("-------------------")


def analisar_texto(texto):
    # analisa o texto
    score = 0
    tamanho_texto = len(texto)

    if "FONTE" not in texto:
        score = score + 1

    if "!!!" in texto:
        score = score + 1

    if "URGENTE" in texto:
        score = score + 1

    if tamanho_texto < 10:
        score = score + 1

    if score == 0:
        return "confiável"
    elif score == 1:
        return "duvidosa"
    else:
        return "falsa"


def adicionar_noticia_manualmente():
    texto = input("Digite o texto: ")
    classificacao = input("Digite classificação: ")

    if classificacao == "":
        classificacao = analisar_texto(texto)
        
    adicionar_noticia(texto, classificacao)


def adicionar_noticia_automaticamente():
    texto = input("Digite o texto: ")
    classificacao = analisar_texto(texto)
    
    adicionar_noticia(texto, classificacao)


def menu():
    while True:
        print("1 - adicionar manual")
        print("2 - adicionar automatico")
        print("3 - listar")
        print("4 - sair")

        opcao = input("Opção: ")

        if opcao == "1":
            adicionar_noticia_manualmente()
        elif opcao == "2":
            adicionar_noticia_automaticamente()
        elif opcao == "3":
            listar_noticias()
        elif opcao == "4":
            break
        else:
            print("errado")


# inicia o programa
# chama o menu
menu()
