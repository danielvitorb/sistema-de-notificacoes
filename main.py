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
        print("erro")


def listar_noticias():
    # lista todas as notícias
    for noticia in noticias:
        print("Texto:", noticias[noticia]["texto"])
        print("Classificacao:", noticias[noticia]["classificação"])
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
        return "confiavel"
    elif score == 1:
        return "duvidosa"
    else:
        return "falsa"


def adicionar_noticia_manualmente():
    texto = input("Digite o texto: ")
    classificacao = input("Digite classificacao: ")

    if classificacao == "":
        adicionar_noticia(texto)
    else:
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

        op = input("opcao: ")

        if op == "1":
            adicionar_noticia_manualmente()
        elif op == "2":
            adicionar_noticia_automaticamente()
        elif op == "3":
            func2()
        elif op == "4":
            break
        else:
            print("errado")


# inicia o programa
# chama o menu
menu()
