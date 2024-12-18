import tkinter as tk
from tkinter import messagebox, Menu
import socket
import struct
import datetime

# Função personalizada para enviar o pacote mágico e gravar no log
def enviar_pacote_wol(mac_address, ip_address):
    """
    Envia um pacote mágico (Wake-on-LAN) para o endereço MAC fornecido e registra em note.log.

    Args:
        mac_address (str): Endereço MAC do dispositivo a ser ligado remotamente.
        ip_address (str): Endereço IP do dispositivo de destino.
    """
    try:
        # Remover separadores do endereço MAC
        mac_address = mac_address.replace(":", "").replace("-", "")
        if len(mac_address) != 12:
            raise ValueError("Endereço MAC inválido.")

        # Construir o pacote mágico
        mac_bytes = bytes.fromhex(mac_address)
        pacote_magico = b'\xff' * 6 + mac_bytes * 16

        # Criar socket e enviar o pacote
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            porta = 9  # Porta padrão para Wake-on-LAN
            s.sendto(pacote_magico, (ip_address, porta))

        # Gravar no log
        registrar_log(ip_address, porta, pacote_magico)
        messagebox.showinfo("Sucesso", "Pacote Wake-on-LAN enviado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao enviar o pacote mágico: {e}")

# Função para registrar os detalhes no log
def registrar_log(ip_address, porta, pacote_magico):
    """
    Registra os detalhes do envio no ficheiro note.log.

    Args:
        ip_address (str): Endereço IP do dispositivo de destino.
        porta (int): Porta usada para o envio.
        pacote_magico (bytes): Dados do pacote mágico enviado.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | IP: {ip_address} | Porta: {porta} | Pacote: {pacote_magico.hex()}\n"

    # Gravar no ficheiro note.log
    with open("note.log", "a") as log_file:
        log_file.write(log_entry)

    # Exibir no terminal
    print(log_entry)

# Função chamada pelo botão "Ligar PC Remoto"
def ligar_pc_remoto():
    """
    Obtém o endereço IP e MAC da entrada do usuário e chama a função
    para enviar o pacote Wake-on-LAN.
    """
    mac = entry_mac.get().strip()  # Remove espaços extras
    ip = entry_ip.get().strip()  # Remove espaços extras

    if not mac or not ip:
        messagebox.showwarning("Atenção", "Por favor, insira um endereço MAC e IP válidos.")
        return

    enviar_pacote_wol(mac, ip)  # Chama a função para enviar o pacote

# Função para sair da aplicação
def sair():
    """
    Fecha a janela principal da aplicação.
    """
    janela.destroy()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Wake-on-LAN")  # Título da janela
janela.geometry("400x250")  # Dimensão da janela

# Configuração do menu superior
menu_bar = Menu(janela)
menu_arquivo = Menu(menu_bar, tearoff=0)
menu_arquivo.add_command(label="Sair", command=sair)
menu_bar.add_cascade(label="Ficheiro", menu=menu_arquivo)
janela.config(menu=menu_bar)

# Rótulo e campo de entrada para o endereço IP
label_ip = tk.Label(janela, text="Endereço IP:")
label_ip.pack(pady=5)
entry_ip = tk.Entry(janela, width=30)
entry_ip.pack(pady=5)

# Rótulo e campo de entrada para o endereço MAC
label_mac = tk.Label(janela, text="Endereço MAC:")
label_mac.pack(pady=5)
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
