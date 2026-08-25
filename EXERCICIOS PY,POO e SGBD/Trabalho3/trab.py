from tkinter import *
from tkinter import filedialog, simpledialog
import sqlite3
import io

def criar_tabela_dados(conexao):
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS dados (info TEXT)")

def criar_tabela_compras(conexao):
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS compras (codigo INTEGER, quantidade INTEGER)")

def salvar_sqlite(dados):
    with sqlite3.connect('dados.db') as conexao:
        criar_tabela_dados(conexao)
        cursor = conexao.cursor()
        for dado in dados:
            cursor.execute("INSERT INTO dados (info) VALUES (?)", (dado,))

def salvar_compra(codigo, quantidade):
    with sqlite3.connect('dados.db') as conexao:
        criar_tabela_compras(conexao)
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO compras (codigo, quantidade) VALUES (?, ?)", (codigo, quantidade))

def carregar_sqlite():
    with sqlite3.connect('dados.db') as conexao:
        criar_tabela_dados(conexao)
        criar_tabela_compras(conexao)
        cursor_dois = conexao.cursor()
        cursor_dois.execute("SELECT * FROM dados")
        dados_recuperados = [row[0] for row in cursor_dois.fetchall()]
        cursor_dois.execute("SELECT * FROM compras")
        compras_recuperadas = cursor_dois.fetchall()
    return dados_recuperados, compras_recuperadas

conn = sqlite3.connect('dados.db')

with io.open('Chamada.sql', 'w') as f:
    for linha in conn.iterdump():
        f.write('%s\n' % linha)

print('Backup realizado com sucesso.')
print('Salvo como clientes_dump.sql')

conn.close()


def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
    )
    pathh.delete(0, END)
    pathh.insert(END, tf)
    with open(tf, 'r') as file:
        file_cont = file.read()
        txtarea.delete(1.0, END)
        txtarea.insert(END, file_cont)

    dados = file_cont.split()
    salvar_sqlite(dados)

    dados_recuperados = carregar_sqlite()
    info_label.config(text=f"Dados recuperados: {dados_recuperados}")

def remove():
    codigo = simpledialog.askinteger("Input", "Digite o código do produto:")
    qtds = simpledialog.askinteger("Input", "Qual a quantidade de produtos deseja comprar?")

    salvar_compra(codigo, qtds)

    info_text = f"Código do Produto: {codigo}\nQuantidade a Comprar: {qtds}\n"
    info_label.config(text=info_text)

    lista = []

    with open("text.txt", "r") as r:
        for line in r:
            parts = line.split()
            if len(parts) >= 3:
                codiguin, descricao, quantidade = parts[:3]
                if int(codiguin) == codigo:
                    quantidade = max(0, int(quantidade) - qtds)
                    line = f"{codiguin} {descricao} {quantidade}\n"
            lista.append(line)

    with open("text.txt", "w") as r:
        r.writelines(lista)

master = Tk()
master.title("Escolha de arquivo")
master.geometry("400x550")
master['bg'] = '#ff99ff'

frame = Frame(master)
frame.pack(pady=20)

ver_sb = Scrollbar(frame, orient=VERTICAL)
ver_sb.pack(side=RIGHT, fill=BOTH)

hor_sb = Scrollbar(frame, orient=HORIZONTAL)
hor_sb.pack(side=BOTTOM, fill=BOTH)

txtarea = Text(frame, width=40, height=15)
txtarea.pack(side=LEFT)

txtarea.config(yscrollcommand=ver_sb.set)
ver_sb.config(command=txtarea.yview)

txtarea.config(xscrollcommand=hor_sb.set)
hor_sb.config(command=txtarea.xview)

pathh = Entry(master)
pathh.pack(expand=True, fill=X, padx=10)

info_label = Label(master, text="", font=("Arial", 12), fg="white", bg="#ff99ff")
info_label.pack()

botao = Button(master, text="ESTOQUE", command=openFile)
botao.pack(side=LEFT)

botao2 = Button(master, text="COMPRAR", command=remove)
botao2.pack(side=RIGHT)

master.mainloop()
