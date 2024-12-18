# wake-on-lan-0
 wake-on-lan with the module wol
 Aqui está o script modificado para usar o módulo `wol` no lugar de `wakeonlan`. Inclui comentários passo a passo e explicações detalhadas.

### Explicação Passo a Passo:

1. **Instalação do módulo `wol`:**
   - Abra o terminal e execute:
     ```bash
     pip install wol
     ```
   - O módulo `wol` fornece uma função simples para enviar pacotes mágicos Wake-on-LAN.

2. **Função `wake_on_lan`:**
   - Recebe um endereço MAC como entrada.
   - Usa a função `send_magic_packet` do módulo `wol` para enviar o pacote.
   - Mostra mensagens ao usuário sobre o sucesso ou erro na operação.

3. **Interface gráfica com `tkinter`:**
   - Cria uma janela com:
     - Campo para inserir o endereço MAC do dispositivo a ser ligado.
     - Botão para enviar o pacote Wake-on-LAN.
     - Botão para sair do programa.
     - Menu no topo com uma opção para sair.

4. **Função `ligar_pc_remoto`:**
   - Obtém o endereço MAC do campo de entrada.
   - Chama a função `wake_on_lan` para enviar o pacote.

5. **Função `sair`:**
   - Fecha a janela principal da aplicação.

6. **Testando o Script:**
   - Certifique-se de que o dispositivo remoto tem suporte ao Wake-on-LAN e está configurado para isso.
   - Insira o endereço MAC no formato correto (e.g., `00:1A:2B:3C:4D:5E`).
   - Clique no botão "Ligar PC Remoto" para enviar o pacote mágico.

---

### Principais Diferenças:
- Substituí o módulo `wakeonlan` pelo módulo `wol`.
- A lógica geral permanece a mesma, pois ambos os módulos trabalham de forma semelhante.

