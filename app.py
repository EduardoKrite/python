import tkinter as TK
from tkinter import messagebox
import os



app= TK.Tk()
app.title("Entrata para os comntario")
app.geometry("500x500") 


# Cria o acesso
usuario = {"Admin","123456"}

def vericador():
    usuario = login.get()
    senha = password.get()
    if usuario !="Admin" or senha != "123456":

        messagebox.showerror("Erro" , "Senha e Login! Você Precisa corrigir!")
    else:
        messagebox.showerror("Bem-vindo" , "Aprovado")
        
        app.destroy()  # Fecha a janela atual
        os.system("python pag2.py")
        # Nenhum código adicional é necessário aqui para ir para pag2, pois pag2.abrir() já está sendo chamado.
    

#Cria o login

bem_vindo = TK.Label(app, text="Login", font=("Arial",40),fg="#000000")
bem_vindo.pack()

login = TK.Label(app, text="login:", font=("Arial", 15),fg="#000000" )
login.place(x=70,y=160)
login = TK.Entry(app,width=60)
login.place(x=70,y=190)

password = TK.Label(app, text="Senha:", font=("Arial", 15),fg="#000000" )
password.place(x=70,y=220)
password = TK.Entry(app, show="*",width=60)
password.place(x=70,y=250)

bontoes = TK.Button(app,text="Entra", width= 20, height=3, background="blue", command=vericador)
bontoes.place(x=180,y=300)
 






app.mainloop()


