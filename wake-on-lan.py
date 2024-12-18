# Instalação do módulo necessário:
# Execute no terminal: pip install wol

import tkinter as tk
from tkinter import messagebox, Menu
from wol import wol

# Função para enviar o pacote Wake-on-LAN
def wake_on_lan(mac_address):
    """
    Envia um pacote mágico para o endereço MAC fornecido usando o módulo wol.

    Args:
        mac_address (str): Endereço MAC do dispositivo que será ligado remotamente.
    """
    try:
        wol.send_magic_packet(mac_address)  # Envia o pacote mágico
        messagebox.showinfo("Sucesso", "Pacote Wake-on-LAN enviado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao enviar o pacote: {e}")

# Função chamada pelo botão "Ligar PC Remoto"
def ligar_pc_remoto():
    """
    Obtém o endereço MAC da entrada do usuário e chama a função
    para enviar o pacote Wake-on-LAN.
    """
    mac = entry_mac.get().strip()  # Remove espaços extras

    if not mac:
        messagebox.showwarning("Atenção", "Por favor, insira um endereço MAC válido.")
        return

    wake_on_lan(mac)  # Chama a função para enviar o pacote

# Função para sair da aplicação
def sair():
    """
    Fecha a janela principal da aplicação.
    """
    janela.destroy()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Wake-on-LAN")  # Título da janela
janela.geometry("400x200")  # Dimensão da janela

# Configuração do menu superior
menu_bar = Menu(janela)
menu_arquivo = Menu(menu_bar, tearoff=0)
menu_arquivo.add_command(label="Sair", command=sair)
menu_bar.add_cascade(label="Ficheiro", menu=menu_arquivo)
janela.config(menu=menu_bar)

# Rótulo e campo de entrada para o endereço MAC
label_mac = tk.Label(janela, text="Endereço MAC:")
label_mac.pack(pady=10)
entry_mac = tk.Entry(janela, width=30)
entry_mac.pack(pady=5)

# Botão para enviar o pacote Wake-on-LAN
botao_ligar = tk.Button(janela, text="Ligar PC Remoto", command=ligar_pc_remoto)
botao_ligar.pack(pady=10)

# Botão para sair da aplicação
botao_sair = tk.Button(janela, text="Sair", command=sair)
botao_sair.pack(pady=10)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
