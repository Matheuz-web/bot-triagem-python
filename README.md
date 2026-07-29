Sistema Inteligente de Suporte e Triagem via Bot

Esse é um projeto de assistência via bot que coleta as informções dadas pelo usuario armazena no banco de dados e disponibiliza categorias para resolver de forma eficiente o problema e envia os dados coletados para um agente humano terminar o atendimento.

Skills Utilizadas;

Python 3 - Linguagem base para a lógica do bot.
SQLite3 - Banco de dados relacional leve embutido para armazenamento dos chamados.
Git & GitHub - Ferramentas para controle de versão e hospedagem do código.

Estrutura do Projeto;

- `banco.py`: Script responsável por inicializar o arquivo de banco de dados (triagem.db) e criar as tabelas necessárias.

- `bot.py`: Script principal que roda o loop de atendimento, interage com o cliente e salva os dados via SQL.

Como Executar;

1. Inicializar o Banco de Dados:
Antes de rodar o bot pela primeira vez, execute o script para criar a estrutura SQL:
```bash
python banco.py
```

2. Iniciar o Atendimento:
Para abrir o terminal interativo do bot e simular um chamado, execute:
```bash
python bot.py
```

///
Projeto desenvolvido para fins de aprendizado prático em desenvolvimento de software com Python e Bancos de Dados.
