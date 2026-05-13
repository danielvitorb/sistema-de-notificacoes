"""
Módulo de Modelo (Dados)

Responsável por gerenciar a estrutura de armazenamento do sistema.
Mantém a lista global de notícias e a lógica base para a persistência 
de novos registros na memória.
"""

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