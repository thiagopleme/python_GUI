# Consultar CEP - Webservice - Resposta com JSON

#Bibliotecas
import matplotlib as mplt
import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

#Funções 
def consulta_cep():
    cep = entrada_cep.get().strip()
    if not cep:
        messagebox.showwarning("Aviso", "Favor insirir um CEP válido!")

    #Chamada do Webservice
    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")    #Requisição pelo CEP
        
        if response.status_code == '200':
            dados = response.json()

            endereco = {
                        f"Logradouro: {dados.get('logradouro', 'N/A')} \n"
                        f"Bairro: {dados.get('bairro', 'N/A')} \n"
                        f"Cidade: {dados.get('cidade', 'N/A')} \n"
                        f"Estado: {dados.get('estado', 'N/A')} \n"
                        f"UF: {dados.get('uf', 'N/A')} \n"
                        f"Região: {dados.get('regiao', 'N/A')} \n"
                        f"DDD: {dados.get('ddd', 'N/A')} \n"
            }
            label_resp.config(text=endereco)
            messagebox.showinfo("Aviso!", "CEP válido")

        else:
            messagebox.showerror("Aviso!", "CEP inválido")

    except Exception as erro:
        messagebox.showerror("Aviso!", "Erro na conexão!" + "\n\nErro: " + str(erro))

#Criação da janela 
form = tk.Tk()
form.title("Consulta CEP")
form.geometry("600x350+100+100")
form.iconbitmap("ponto.ico")
form.configure(background="white")

#Imagem
imagem = Image.Open("maps.ico")
imagem = imagem.resize((60,60))
imagem_tk = ImageTk.PhotoImage(imagem)

#Posicionar a imagem 
label_imagem = tk.Label(form, image = imagem_tk)
label_imagem.grid(row = 0, column= 0, padx= 5, pady= 5)

#Rótulo e entrada
label_cep = tk.Label(form, text="Digite o seu cep", justify="right", font=("Arial", 10))
label_cep.grid(row = 0, column= 1, padx= 5, pady= 5)
label_cep.configure(background="white")

#Entrada
entrada_cep = tk.Entry(form, width=20)
entrada_cep.grid(row = 0, column= 2, padx= 5, pady= 5)

#Botão
btn_consultar = tk.Button(form, text="Consultar", command=consulta_cep)
btn_consultar.grid(row = 0, column= 3, padx= 5, pady= 5)

#Rótulo - reposta
label_resp = tk.Label(form, text="", justify="left", font=("Arial", 10))
label_resp.grid(row = 1, column= 1, padx= 5, pady= 5)
label_resp.configure(background="white")

#Looping da interface
form.mainloop()
