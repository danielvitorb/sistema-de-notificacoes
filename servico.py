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