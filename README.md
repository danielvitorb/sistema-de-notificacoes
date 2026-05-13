# Sistema de Monitoramento de Fake News e Qualidade da Informação

Este projeto é parte da avaliação da Unidade I da disciplina **DIM0501 - Boas Práticas de Programação**. O objetivo central é a aplicação prática de refatoração, modularização e programação defensiva em um código legado.

## 📋 Sobre o Projeto

O sistema permite o gerenciamento e a classificação textual de notícias para identificar potenciais desinformações. Ele foi inteiramente refatorado a partir de um código inicial problemático, aplicando melhorias de legibilidade, organização estrutural e tratamento de erros.

O sistema avalia as notícias com base nos seguintes critérios:
- Ausência de fonte informada.
- Uso excessivo de pontuação alarmista (ex: "!!!").
- Uso de linguagem sensacionalista (ex: "URGENTE").
- Tamanho do texto (textos excessivamente curtos).

## 🏗️ Estrutura do Projeto (Modularização)

O sistema foi dividido nos seguintes módulos:

- `modelo.py`: Gerencia o armazenamento e a estrutura dos dados (lista de notícias).
- `servico.py`: Contém a lógica de negócio principal e os critérios de análise de fake news.
- `interface.py`: Responsável exclusivamente pela interação com o usuário via terminal (menus, inputs e prints).
- `main.py`: Ponto de entrada que inicializa a aplicação.

## 🚀 Como Executar

Certifique-se de ter o Python 3.x instalado em sua máquina.

1. Clone o repositório:
   ```bash
   git clone https://github.com/danielvitorb/sistema-de-notificacoes.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd sistema-de-noticias
   ```
3. Execute o arquivo principal:
   ```bash
   python main.py
   ```

## 🛡️ Melhorias Implementadas (Boas Práticas)

- **Refatoração de Nomenclatura:** Substituição de nomes genéricos por variáveis e funções descritivas.
- **Programação Defensiva:** Adição de validações de entrada do usuário para evitar comportamentos inesperados e quebras.
- **Documentação:** Inclusão de *docstrings* claras nas funções e remoção de comentários redundantes.
- **Modularização:** Separação clara entre regras de negócio, dados e interface visual.

## 👨‍💻 Autor

- **Daniel Vítor de Oliveira Bezerra**