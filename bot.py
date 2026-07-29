import sqlite3
import time

def salvar_no_banco(nome, categoria, descricao):
    """Função para salvar o problema do cliente no banco SQL"""
    conexao = sqlite3.connect('triagem.db')
    cursor = conexao.cursor()
    
    cursor.execute("INSERT INTO chamados (usuario, categoria, descricao) VALUES (?, ?, ?)", (nome, categoria, descricao))
    
    conexao.commit()
    conexao.close()

def iniciar_atendimento():
    print("\n[Bot]: Olá! Bem-vindo ao Suporte Inteligente.")
    nome = input("[Bot]: Qual é o seu nome? \nVocê: ")
    
    print(f"\n[Bot]: Prazer, {nome}! Como posso te ajudar hoje?")
    print("Escolha uma das opções abaixo digitando o número:")
    print("1 - Problemas com Internet / Conexão")
    print("2 - Problemas com Financeiro / Faturas")
    print("3 - Dúvidas sobre Planos / Cancelamento")
    
    opcao = input("Você (Digite 1, 2 ou 3): ")
    
    # mapeamento de categorias baseado na opção escolhida pelo usuário
    categorias = {
        "1": "Técnico - Internet",
        "2": "Financeiro",
        "3": "Comercial / Planos"
    }
    
    categoria_final = categorias.get(opcao, "Outros / Não Identificado")
    
    print(f"\n[Bot]: Entendi. Você selecionou a opção de: {categoria_final}.")
    descricao = input("[Bot]: Por favor, descreva brevemente o seu problema:\nVocê: ")
    
    print("\n[Bot]: Processando seus dados e abrindo chamado...")
    time.sleep(1.5) # simulação do bot pensando

    # salvando os dados coletados no banco de dados
    salvar_no_banco(nome, categoria_final, descricao)
    
    print(f"\n[Bot]: Sucesso, {nome}! Seu chamado foi registrado na categoria '{categoria_final}'.")
    print("[Bot]: Um atendente humano entrará em contato em breve. Obrigado!\n")

if __name__ == "__main__":
    iniciar_atendimento()
