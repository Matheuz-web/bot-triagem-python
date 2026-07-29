### Sistema Inteligente de Suporte e Triagem com IA (GROQ)

Fiz um Projeto de um assistente virtual de triagem para suporte ao cliente. O bot interage com o cliente de forma aberta, permitindo que ele descreva seu problema com as próprias palavras. A Inteligência Artificial (Groq) analisa o relato, categoriza o chamado automaticamente e salva os registros de forma estruturada em um banco de dados SQL.

## 🚀 Tecnologias Utilizadas
* **Python 3**: Linguagem base para a lógica do sistema.
* **Groq API (Llama 3)**: Modelo de IA avançado utilizado para processamento de linguagem natural e triagem automatizada.
- **SQLite3**: Banco de dados relacional leve para armazenamento seguro dos chamados.
- **Python-Dotenv**: Gerenciamento de variáveis de ambiente para proteção de chaves de API.
- **Git & GitHub**: Controle de versão e hospedagem profissional do código.

## Estrutura do projeto;

- `banco.py`: Script responsável por inicializar o banco de dados (`triagem.db`) e estruturar as tabelas SQL.
- `bot.py`: Script principal que gerencia o loop de atendimento, conecta-se à IA para classificação e salva os dados.
- `.env`: Arquivo local e protegido para armazenamento das credenciais de acesso da API.

### Como executar o projeto;

## 1. Configurar as Credenciais
Crie um arquivo chamado `.env` na raiz do projeto e adicione a sua chave da Groq:
```text
GROQ_API_KEY=sua_chave_aqui
```

## 2. Inicializar o Banco de Dados
Execute o script para criar a estrutura das tabelas SQL:
```bash
python banco.py
```

## 3. Iniciar o Atendimento com IA
Para abrir o terminal interativo do bot e simular um chamado analisado por IA, execute:
```bash
python bot.py
```

///
*Projeto desenvolvido para fins de aprendizado prático em desenvolvimento de software, Inteligência Artificial e Banco de Dados.*
