import sqlite3

def iniciar_banco():
 # conecta ao banco de dados. se o arquivo não existir, ele cria na hora

    conexao = sqlite3.connect('triagem.db')
    cursor = conexao.cursor()
    
 # cria a tabela para salvar o histórico de conversas e triagem
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chamados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            categoria TEXT NOT NULL,
            descricao TEXT NOT NULL,
            status TEXT DEFAULT 'Aberto'
        )
    ''')
    
    conexao.commit()
    conexao.close()
    print("Banco de dados configurado com sucesso!")

 # se rodar este arquivo direto, ele cria o banco
if __name__ == "__main__":
    iniciar_banco()
