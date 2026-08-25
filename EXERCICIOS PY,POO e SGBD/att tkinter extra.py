import tkinter as tk
from tkinter import filedialog

def open_file():
    caminhoarq = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
    if caminhoarq:
        with open(caminhoarq, 'r') as file:
            content = file.read()
        txtarea.delete(1.0, "end-1c")  
        txtarea.insert("end", content)

app = tk.Tk()
app.title("Ver arquivos txt")

open_button = tk.Button(app, text="Abrir Arquivo", command=open_file)
open_button.pack(pady=10)

txtarea = tk.Text(app, wrap=tk.WORD, height=20, width=50)
txtarea.pack()

app.mainloop()
