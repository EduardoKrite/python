import tkinter as tk
import os
from tkinter import messagebox

janela = tk.Tk()
janela.title("Tarefas")
janela.geometry("500x500")



def abrir():
    janela.destroy()
    os.system('app.py')


def enviar():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    obs = entry_obs.get("1.0", tk.END)

    with open("Trarefas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Nome: {nome}\nEmail: {email}\nTelefone: {telefone}\nObservação: {obs}")

    messagebox.showinfo("Aprovado", "Parabéns, aprovado!")
    

def limpar():
    entry_nome.delete(0,tk.END)
    entry_email.delete(0,tk.END)
    entry_telefone.delete(0,tk.END)
    entry_obs.delete("1.0",tk.END)

tk.Label( text="Digite o seu Nome:", font=("Arial",10)).place( x=30, y=80)
entry_nome = tk.Entry( width=70)
entry_nome.place(x=30, y=100)

tk.Label( text="Digite o seu Email:", font=("Arial",10)).place( x=30, y=120)
entry_email = tk.Entry( width=70)
entry_email.place(x=30, y=140)

tk.Label( text="Seu Telefone:", font=("Arial",10)).place( x=30, y=160)
entry_telefone = tk.Entry( width=70)
entry_telefone.place(x=30, y=180)

tk.Label( text= "Digite o que você gosta de Fazer: ", font=("Arial",10)).place (x=30, y=200)
entry_obs = tk.Text (width=70,height=10)
entry_obs.place(x=30, y=220)

tk.Label(janela, text="Digite a suas trarefas:...", font=("Arial", 18)).pack(pady=50)
tk.Button(janela, text="Fechar", background="red" ,command=janela.destroy).place(x=30,y=450)
tk.Button(janela, text="Salvar", background="green" ,command=enviar).place(x=250,y=450)
tk.Button(janela, text="Limpar", background="blue" ,command=limpar).place(x=450,y=450)

janela.mainloop()

