import tkinter as tk
import sqlite3

def fazer_login():
    # Verificar se o usuário e senha estão corretos (substitua por suas próprias verificações)
    usuario = usuario_entry.get()
    senha = senha_entry.get()

    if usuario == "1" and senha == "1":
        # Login bem-sucedido, abrir a nova janela
        abrir_nova_janela()
    else:
        mensagem_erro.config(text="Usuário ou senha incorretos")

def abrir_nova_janela():
    # Fechar a janela de login
    janela_login.destroy()

    # Criar a nova janela
    nova_janela = tk.Tk()
    nova_janela.title("Gestão Financeira")
    nova_janela.geometry("300x300")
    
    # Adicionar três botões à nova janela
    botao1 = tk.Button(nova_janela, text="Despesas", command=abrir_janela_despesas)
    botao1.pack()
    botao2 = tk.Button(nova_janela, text="Contas Pagar", command=abrir_janela_contas_pagar)
    botao2.pack()
    botao3 = tk.Button(nova_janela, text="Contas Receber", command=abrir_janela_contas_receber)
    botao3.pack()


    # Executar a janela de login
    nova_janela.login.mainloop()


def criar_tabela_despesas():
    conn = sqlite3.connect("gestao.db")
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS despesas (
            id INTEGER PRIMARY KEY,
            descricao TEXT,
            valor REAL,
            data DATE
        )
    ''')
    
    conn.commit()
    conn.close()

# Função para listar todas as despesas
def listar_despesas():
    conn = sqlite3.connect("gestao.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, descricao, valor, data FROM despesas")
    despesas = cursor.fetchall()
    
    conn.close()
    
    return despesas


# Função para adicionar uma nova despesa
def adicionar_despesa(descricao, valor, data):
    conn = sqlite3.connect("gestao.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO despesas (descricao, valor, data) VALUES (?, ?, ?)", (descricao, valor, data))
    
    conn.commit()
    conn.close()

# Função para excluir uma despesa
def excluir_despesa(id):
    conn = sqlite3.connect("gestao.db")
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM despesas WHERE id=?", (id,))
    
    conn.commit()
    conn.close()


# Função para abrir a janela de despesas

def abrir_janela_despesas():
    criar_tabela_despesas  # Chame esta função para criar a tabela
    despesas_janela = tk.Tk()
    despesas_janela.title("Despesas")
    despesas_janela.geometry("800x800")
    
    # Elementos da interface de usuário
    label_descricao = tk.Label(despesas_janela, text="Descrição:")
    label_descricao.pack()
    entry_descricao = tk.Entry(despesas_janela)
    entry_descricao.pack()
    
    label_valor = tk.Label(despesas_janela, text="Valor:")
    label_valor.pack()
    entry_valor = tk.Entry(despesas_janela)
    entry_valor.pack()
    
    label_data = tk.Label(despesas_janela, text="Data:")
    label_data.pack()
    entry_data = tk.Entry(despesas_janela)
    entry_data.pack()
    
    def adicionar_despesa_handler():
        descricao = entry_descricao.get()
        valor = float(entry_valor.get())
        data = entry_data.get()
        adicionar_despesa(descricao, valor, data)
        atualizar_lista_despesas()
    
    button_adicionar = tk.Button(despesas_janela, text="Adicionar Despesa", command=adicionar_despesa_handler)
    button_adicionar.pack()
    
    lista_despesas = tk.Listbox(despesas_janela, width=50, height=10)
    lista_despesas.pack()

    
    def atualizar_lista_despesas():
        lista_despesas.delete(0, tk.END)
        despesas = listar_despesas()
        for despesa in despesas:
            lista_despesas.insert(tk.END, f"ID: {despesa[0]}, Descrição: {despesa[1]}, Valor: {despesa[2]}, Data: {despesa[3]}")
    
    atualizar_lista_despesas()
    
    def excluir_despesa_handler():
        selecionado = lista_despesas.curselection()
        if selecionado:
            id_text = lista_despesas.get(selecionado[0]).split()[1]
            id = int(id_text.strip(','))
            if isinstance(id, int):
                excluir_despesa(id)
                atualizar_lista_despesas()

    
    button_excluir = tk.Button(despesas_janela, text="Excluir Despesa Selecionada", command=excluir_despesa_handler)
    button_excluir.pack()
    
    despesas_janela.mainloop()

# Criar bd contas pagar;
def criar_tabela_contas_pagar():
    conn = sqlite3.connect("gestao.db")
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contas_pagar (
            id INTEGER PRIMARY KEY,
            descricao TEXT,
            valor REAL,
            data DATE
        )
    ''')
    
    conn.commit()
    conn.close()

def listar_contas_pagar():
    conn = sqlite3.connect("gestao.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, descricao, valor, data FROM contas_pagar")
    contas_pagar = cursor.fetchall()
    
    conn.close()
    
    return contas_pagar

def adicionar_conta_pagar(descricao, valor, data):
    conn = sqlite3.connect("gestao.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO contas_pagar (descricao, valor, data) VALUES (?, ?, ?)", (descricao, valor, data))
    
    conn.commit()
    conn.close()

def excluir_conta_pagar(id):
    conn = sqlite3.connect("gestao.db")
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM contas_pagar WHERE id=?", (id,))
    
    conn.commit()
    conn.close()

# Função contas pagar 

def abrir_janela_contas_pagar():
    criar_tabela_contas_pagar()  # Chame esta função para criar a tabela
    contas_pagar_janela = tk.Tk()
    contas_pagar_janela.title("Contas a Pagar")
    contas_pagar_janela.geometry("800x800")
    
    # Elementos da interface de usuário
    label_descricao = tk.Label(contas_pagar_janela, text="Descrição:")
    label_descricao.pack()
    entry_descricao = tk.Entry(contas_pagar_janela)
    entry_descricao.pack()
    
    label_valor = tk.Label(contas_pagar_janela, text="Valor:")
    label_valor.pack()
    entry_valor = tk.Entry(contas_pagar_janela)
    entry_valor.pack()
    
    label_data = tk.Label(contas_pagar_janela, text="Data:")
    label_data.pack()
    entry_data = tk.Entry(contas_pagar_janela)
    entry_data.pack()
    
    def adicionar_conta_pagar_handler():
        descricao = entry_descricao.get()
        valor = float(entry_valor.get())
        data = entry_data.get()
        adicionar_conta_pagar(descricao, valor, data)
        atualizar_lista_contas_pagar()
    
    button_adicionar = tk.Button(contas_pagar_janela, text="Adicionar Conta a Pagar", command=adicionar_conta_pagar_handler)
    button_adicionar.pack()
    
    lista_contas_pagar = tk.Listbox(contas_pagar_janela, width=50, height=10)
    lista_contas_pagar.pack()

    
    def atualizar_lista_contas_pagar():
        lista_contas_pagar.delete(0, tk.END)
        contas_pagar = listar_contas_pagar()
        for conta_pagar in contas_pagar:
            lista_contas_pagar.insert(tk.END, f"ID: {conta_pagar[0]}, Descrição: {conta_pagar[1]}, Valor: {conta_pagar[2]}, Data: {conta_pagar[3]}")
    
    atualizar_lista_contas_pagar()
    
    def excluir_conta_pagar_handler():
        selecionado = lista_contas_pagar.curselection()
        if selecionado:
            id_text = lista_contas_pagar.get(selecionado[0]).split()[1]
            id = int(id_text.strip(','))
            if isinstance(id, int):
                excluir_conta_pagar(id)
                atualizar_lista_contas_pagar()

    
    button_excluir = tk.Button(contas_pagar_janela, text="Excluir Conta a Pagar Selecionada", command=excluir_conta_pagar_handler)
    button_excluir.pack()
    
#Funções banco de Dados
def criar_tabela_contas_receber():
    conn = sqlite3.connect("gestao.db")
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contas_receber (
            id INTEGER PRIMARY KEY,
            descricao TEXT,
            valor REAL,
            data DATE
        )
    ''')
    
    conn.commit()
    conn.close()

def listar_contas_receber():
    conn = sqlite3.connect("gestao.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, descricao, valor, data FROM contas_receber")
    contas_receber = cursor.fetchall()
    
    conn.close()
    
    return contas_receber

def adicionar_conta_receber(descricao, valor, data):
    conn = sqlite3.connect("gestao.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO contas_receber (descricao, valor, data) VALUES (?, ?, ?)", (descricao, valor, data))
    
    conn.commit()
    conn.close()

def excluir_conta_receber(id):
    conn = sqlite3.connect("gestao.db")
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM contas_receber WHERE id=?", (id,))
    
    conn.commit()
    conn.close()

#Funções crud receber 
def abrir_janela_contas_receber():
    criar_tabela_contas_receber()
    receber_janela = tk.Tk()
    receber_janela.title("Contas Receber")
    receber_janela.geometry("800x800")
    
    label_descricao = tk.Label(receber_janela, text="Descrição:")
    label_descricao.pack()
    entry_descricao = tk.Entry(receber_janela)
    entry_descricao.pack()
    
    label_valor = tk.Label(receber_janela, text="Valor:")
    label_valor.pack()
    entry_valor = tk.Entry(receber_janela)
    entry_valor.pack()
    
    label_data = tk.Label(receber_janela, text="Data:")
    label_data.pack()
    entry_data = tk.Entry(receber_janela)
    entry_data.pack()
    
    def adicionar_conta_receber_handler():
        descricao = entry_descricao.get()
        valor = float(entry_valor.get())
        data = entry_data.get()
        adicionar_conta_receber(descricao, valor, data)
        atualizar_lista_contas_receber()
    
    button_adicionar = tk.Button(receber_janela, text="Adicionar Conta a Receber", command=adicionar_conta_receber_handler)
    button_adicionar.pack()
    
    lista_contas_receber = tk.Listbox(receber_janela, width=50, height=10)
    lista_contas_receber.pack()

    def atualizar_lista_contas_receber():
        lista_contas_receber.delete(0, tk.END)
        contas_receber = listar_contas_receber()
        for conta_receber in contas_receber:
            lista_contas_receber.insert(tk.END, f"ID: {conta_receber[0]}, Descrição: {conta_receber[1]}, Valor: {conta_receber[2]}, Data: {conta_receber[3]}")
    
    atualizar_lista_contas_receber()
    
    def excluir_conta_receber_handler():
        selecionado = lista_contas_receber.curselection()
        if selecionado:
            id_text = lista_contas_receber.get(selecionado[0]).split()[1]
            id = int(id_text.strip(','))
            if isinstance(id, int):
                excluir_conta_receber(id)
                atualizar_lista_contas_receber()
    
    button_excluir = tk.Button(receber_janela, text="Excluir Conta a Receber Selecionada", command=excluir_conta_receber_handler)
    button_excluir.pack()
    
    receber_janela.mainloop()

# Criar a janela de login
janela_login = tk.Tk()
janela_login.title("Gestão Financeira")
janela_login.geometry("400x250")


# Criar campos de entrada para usuário e senha
usuario_label = tk.Label(janela_login, text="Usuário:")
usuario_label.pack()
usuario_entry = tk.Entry(janela_login)
usuario_entry.pack()

senha_label = tk.Label(janela_login, text="Senha:")
senha_label.pack()
senha_entry = tk.Entry(janela_login, show="*")  # Para ocultar a senha
senha_entry.pack()

# Criar botão de login
botao_login = tk.Button(janela_login, text="Login", command=fazer_login)
botao_login.pack()

# Mensagem de erro
mensagem_erro = tk.Label(janela_login, text="", fg="red")
mensagem_erro.pack()


# Executar a janela de login
janela_login.mainloop()
