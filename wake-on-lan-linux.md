O módulo **`etherwake`** não é projetado para funcionar nativamente no **Windows 10**, pois depende de funcionalidades específicas do Linux para enviar pacotes mágicos Wake-on-LAN diretamente na camada Ethernet. 

No entanto, existem alternativas que funcionam no Windows, como:

### 1. **Alternativas no Windows:**
   - **Módulo `wakeonlan`**:
     É uma solução 100% compatível com o Windows. Ele utiliza pacotes UDP em vez de comandos de nível Ethernet e é fácil de instalar e usar.

   - **Módulo `wol`**:
     Outra opção para Windows, que também trabalha com pacotes mágicos, mas pode apresentar problemas de compatibilidade com versões modernas do Python (como mencionado anteriormente).

   - **Soluções externas:**
     Ferramentas de linha de comando como **`wolcmd`** ou **`WakeMeOnLan`** da NirSoft podem ser chamadas de scripts Python usando o módulo `subprocess`.

---

### 2. **Por que `etherwake` não funciona no Windows?**
   - O **`etherwake`** é uma ferramenta de rede que interage diretamente com a interface de rede Ethernet para enviar pacotes mágicos.
   - Ele depende de bibliotecas e chamadas de sistema disponíveis apenas em sistemas baseados em Unix/Linux.

   **Alternativa Linux:** Se você precisar usar `etherwake`, pode configurá-lo em uma máquina virtual Linux ou em um Raspberry Pi e acessar remotamente a ferramenta a partir do Windows.

---

### Conclusão:
Use **`wakeonlan`** ou **`wol`** para enviar pacotes Wake-on-LAN no Windows 10. Caso precise da funcionalidade de nível Ethernet que `etherwake` oferece, será necessário trabalhar em um ambiente Linux.