import sqlite3
import time
import os
from groq import Groq
# genai para usar a API Gemini da Google

from dotenv import dotenv_values

# carrega a chave guardada no arquivo .env
config = dotenv_values(".env")

# força a leitura do arquivo .env no mesmo diretório do script
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_env = os.path.join(diretorio_atual, '.env')

CHAVE_API = config.get("GROQ_API_KEY")
cliente_ia = Groq(api_key=CHAVE_API)

def salvar_no_banco(nome, categoria, descricao):
    """Função para salvar o problema do cliente no banco SQL"""
    # criando uma instrução clara de como a IA deve se comportar

    conexao = sqlite3.connect('triagem.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO chamados (usuario, categoria, descricao) VALUES (?, ?, ?)", (nome, categoria, descricao))
    conexao.commit()
    conexao.close()

def classificar_com_ia(texto_do_cliente):
    """Função que envia o problema para o Gemini categorizar"""
    comando = (
        "Você é um robô de triagem de suporte técnico. "
        "Analise o problema do cliente e responda APENAS com uma das três categorias exatas abaixo, "
        "sem nenhuma outra palavra, saudação ou ponto final:\n"
        "Técnico - Internet\n"
        "Financeiro\n"
        "Comercial / Planos\n"
        f"Problema do cliente: '{texto_do_cliente}'"
    )
    
    try:
        resposta = cliente_ia.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": comando,
                }
            ],
            model="llama-3.1-8b-instant"
        )
    
        texto_ia = resposta.choices[0].message.content

        # a IA retornaa uma categoria, caso contrario, retorna "Outros / Não Identificado"
        if texto_ia:
            return texto_ia.strip()
        return "Outros / Não Identificado"
        
    except Exception as e:
        print(f"Erro ao conectar com a IA: {e}")
        return "Outros / Não Identificado"

def iniciar_atendimento():
    print("\n[Bot Inteligente]: Olá! Bem-vindo ao Suporte com Inteligência Artificial.")
    nome = input("[Bot]: Qual é o seu nome? \nVocê: ")
    
    print(f"\n[Bot]: Prazer, {nome}!")
    descricao = input("[Bot]: Me conte com as suas palavras: qual problema você está enfrentando hoje?\nVocê: ")
    
    print("\n[Bot]: Analisando o seu relato com Inteligência Artificial...")
    time.sleep(1)

    # a IA analisa o texto do cliente e mostra a categoria identificada
    categoria_final = classificar_com_ia(descricao)
    
    print(f"[Bot]: Triagem concluída! Identifiquei que seu problema pertence ao setor: {categoria_final}")
    print("[Bot]: Processando seus dados e abrindo chamado...")
    time.sleep(1)
    
    salvar_no_banco(nome, categoria_final, descricao)
    
    print(f"\n[Bot]: Sucesso, {nome}! Seu chamado foi registrado na categoria '{categoria_final}'.")
    print("[Bot]: Um especialista deste setor entrará em contato em breve. Obrigado!\n")

if __name__ == "__main__":
    iniciar_atendimento()
