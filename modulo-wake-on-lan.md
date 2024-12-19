Abaixo está uma lista em formato Markdown contendo **todos os módulos e ferramentas relacionados ao Wake-on-LAN**, com explicações, exemplos de uso e compatibilidade com **Windows 10 em português europeu**.

---

# Lista de Módulos e Ferramentas de Wake-on-LAN

## 1. **`pywakeonlan`**
- **Descrição**: Um módulo simples e eficiente para enviar pacotes mágicos usando Python.
- **Compatibilidade**: Funciona em **Windows** e sistemas Linux.
- **Instalação**:
  ```bash
  pip install pywakeonlan
  ```
- **Exemplo de Uso**:
  ```python
  from wakeonlan import send_magic_packet

  # Enviar pacote mágico para o endereço MAC
  send_magic_packet('00:1A:2B:3C:4D:5E')
  ```
- **Vantagens**:
  - Simples de usar.
  - Compatível com Python 3.x.
  - Funciona no Windows sem dependências adicionais.
- **Limitações**:
  - Não permite controle detalhado sobre as camadas Ethernet.

---

## 2. **`wakeonlan`**
- **Descrição**: Um módulo Python para enviar pacotes mágicos, muito semelhante ao `pywakeonlan`.
- **Compatibilidade**: Funciona em **Windows** e sistemas Linux.
- **Instalação**:
  ```bash
  pip install wakeonlan
  ```
- **Exemplo de Uso**:
  ```python
  from wakeonlan import send_magic_packet

  # Enviar pacote mágico para o endereço MAC
  send_magic_packet('00:1A:2B:3C:4D:5E')
  ```
- **Vantagens**:
  - Fácil de usar e configurar.
  - Boa documentação.
- **Limitações**:
  - Similar ao `pywakeonlan`, sem grandes diferenças.

---

## 3. **`wol`**
- **Descrição**: Um módulo alternativo para enviar pacotes mágicos, mas o desenvolvimento parece estar descontinuado.
- **Compatibilidade**: Funciona no **Windows**, mas pode apresentar problemas de compatibilidade com Python 3.x.
- **Instalação**:
  ```bash
  pip install wol
  ```
- **Exemplo de Uso**:
  ```python
  import wol

  # Enviar pacote mágico para o endereço MAC
  wol.send_magic_packet('00:1A:2B:3C:4D:5E')
  ```
- **Vantagens**:
  - Simples de usar.
- **Limitações**:
  - O código original usa sintaxe do Python 2, exigindo correções manuais.
  - Funcionalidade limitada comparada a outros módulos.

---

## 4. **`etherwake`**
- **Descrição**: Uma ferramenta de linha de comando para enviar pacotes mágicos diretamente pela camada Ethernet.
- **Compatibilidade**: Funciona **somente em Linux**. Não é suportada no **Windows**.
- **Instalação** (em sistemas Linux):
  ```bash
  sudo apt install etherwake
  ```
- **Exemplo de Uso**:
  ```bash
  sudo etherwake 00:1A:2B:3C:4D:5E
  ```
- **Vantagens**:
  - Controle direto sobre a camada Ethernet.
  - Muito eficiente.
- **Limitações**:
  - Não funciona no Windows.
  - Requer permissões de superusuário (root).

---

## 5. **`WakeMeOnLan`**
- **Descrição**: Uma ferramenta GUI gratuita da NirSoft que permite enviar pacotes mágicos de forma simples.
- **Compatibilidade**: Funciona no **Windows**.
- **Download**: [WakeMeOnLan - NirSoft](https://www.nirsoft.net/utils/wake_on_lan.html)
- **Exemplo de Uso**:
  1. Abra o programa.
  2. Adicione o endereço MAC e IP do dispositivo.
  3. Clique em "Wake Up Selected Computers".
- **Vantagens**:
  - Fácil de usar com interface gráfica.
  - Não requer instalação (executável portátil).
- **Limitações**:
  - Não é integrável diretamente com scripts Python.

---

## 6. **`wolcmd`**
- **Descrição**: Uma ferramenta de linha de comando para enviar pacotes Wake-on-LAN em sistemas Windows.
- **Compatibilidade**: Funciona em **Windows**.
- **Download**: [Depicus - wolcmd](https://www.depicus.com/wake-on-lan/wake-on-lan-cmd)
- **Exemplo de Uso**:
  ```bash
  wolcmd 00:1A:2B:3C:4D:5E 192.168.1.255 255.255.255.0 9
  ```
- **Vantagens**:
  - Rápido e simples para uso em scripts batch.
- **Limitações**:
  - Não possui interface gráfica.

---

## 7. **Ferramentas Adicionais**
### a) **Wake-on-LAN para Android**
- **Descrição**: Aplicativos como "Wake On Lan" na Play Store permitem enviar pacotes mágicos usando dispositivos móveis.
- **Compatibilidade**: Android.
- **Vantagens**:
  - Controle remoto por dispositivos móveis.
- **Limitações**:
  - Não integrável diretamente com scripts Python.

### b) **Wake-on-LAN para iOS**
- **Descrição**: Aplicativos semelhantes estão disponíveis na App Store.
- **Compatibilidade**: iOS.
- **Vantagens**:
  - Controle remoto via iPhone/iPad.

---

# Conclusão

### Ferramentas Recomendadas para Windows 10:
1. **Para Python**: Use **`pywakeonlan`** ou **`wakeonlan`**.
2. **Para GUI**: Use **WakeMeOnLan**.
3. **Para Linha de Comando**: Use **`wolcmd`**.
