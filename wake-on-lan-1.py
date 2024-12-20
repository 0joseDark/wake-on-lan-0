import tkinter as tk
from tkinter import messagebox, Menu
from wakeonlan import send_magic_packet

# Função para enviar o pacote Wake-on-LAN
def wake_on_lan(mac_address):
    try:
        send_magic_packet(mac_address)
        messagebox.showinfo("Sucesso", "Pacote Wake-on-LAN enviado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao enviar o pacote: {e}")

# Função para ligar o PC remoto
def ligar_pc_remoto():
    mac = entry_mac.get()
    if not mac:
        messagebox.showwarning("Atenção", "Por favor, insira um endereço MAC.")
        return
    wake_on_lan(mac)

# Função para sublinhar texto selecionado
def sublinhar_texto(event):
    widget = event.widget
    if isinstance(widget, tk.Entry):
        widget.select_range(0, tk.END)

# Função para copiar texto selecionado
def copiar_texto():
    janela.clipboard_clear()
    try:
        texto_selecionado = janela.focus_get().selection_get()
        janela.clipboard_append(texto_selecionado)
    except:
        messagebox.showwarning("Atenção", "Nenhum texto selecionado para copiar!")

# Função para colar texto
def colar_texto():
    try:
        texto = janela.clipboard_get()
        widget = janela.focus_get()
        if isinstance(widget, tk.Entry):
            widget.insert(tk.END, texto)
    except:
        messagebox.showwarning("Atenção", "Não foi possível colar o texto!")

# Função para sair da aplicação
def sair():
    janela.destroy()

# Criar a janela principal
janela = tk.Tk()
janela.title("Wake-on-LAN")
janela.geometry("400x250")

# Criar o menu
menu_bar = Menu(janela)
menu_arquivo = Menu(menu_bar, tearoff=0)
menu_arquivo.add_command(label="Sair", command=sair)
menu_editar = Menu(menu_bar, tearoff=0)
menu_editar.add_command(label="Copiar", command=copiar_texto)
menu_editar.add_command(label="Colar", command=colar_texto)
menu_bar.add_cascade(label="Ficheiro", menu=menu_arquivo)
menu_bar.add_cascade(label="Editar", menu=menu_editar)
janela.config(menu=menu_bar)

# Rótulos e campos de entrada
label_ip = tk.Label(janela, text="Endereço IP (opcional):")
label_ip.pack(pady=5)
entry_ip = tk.Entry(janela, width=30)
entry_ip.pack(pady=5)

label_mac = tk.Label(janela, text="Endereço MAC:")
label_mac.pack(pady=5)
entry_mac = tk.Entry(janela, width=30)
entry_mac.pack(pady=5)

# Vincular eventos de sublinhar texto
entry_ip.bind("<Button-1>", sublinhar_texto)
entry_mac.bind("<Button-1>", sublinhar_texto)

# Botões
botao_ligar = tk.Button(janela, text="Ligar PC Remoto", command=ligar_pc_remoto)
botao_ligar.pack(pady=10)

botao_sair = tk.Button(janela, text="Sair", command=sair)
botao_sair.pack(pady=10)

# Iniciar o loop principal da interface
janela.mainloop()
