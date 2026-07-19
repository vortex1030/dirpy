# DIRPY

```
888 88e   ,e,                           
888 888b   "  888,8, 888 88e  Y8b Y888P 
888 8888D 888 888 "  888 888b  Y8b Y8P  
888 888P  888 888    888 888P   Y8b Y   
888 88"   888 888    888 88"     888    
                     888         888    
                     888         888    
```

**DIRPY** é uma ferramenta simples de enumeração de diretórios desenvolvida em Python.
Ela realiza testes de caminhos em aplicações web utilizando requisições HTTP GET e identifica possíveis diretórios e arquivos existentes através dos códigos de resposta HTTP.

> Projeto criado para fins educacionais e estudo de segurança web.

---

## Funcionalidades

* Scanner de diretórios baseado em wordlist.
* Suporte para URLs HTTP e HTTPS.
* Detecção automática de esquema (`http://` ou `https://`).
* Resolução de IP do domínio.
* Identificação do servidor web através do header `Server`.
* Tratamento de códigos HTTP:

  * `200` → Diretório encontrado.
  * `301/302/307/308` → Redirecionamento.
  * `403/405/501` → Possível diretório protegido.
  * `404` → Não encontrado.
* Timeout para evitar travamentos.
* Interface no terminal com cores.

---

## Requisitos

* Python 3.10+

Bibliotecas utilizadas:

* requests
* colorama

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu_usuario/DIRPY.git
```

Entre no diretório:

```bash
cd DIRPY
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Ou manualmente:

```bash
pip install requests colorama
```

---

## Uso

Execute:

```bash
python3 dirpy.py
```

Escolha a opção:

```
[1] dir scan
```

Informe o alvo:

```
Url: exemplo.com
```

Informe a wordlist:

```
File name or path: wordlist.txt
```

O scanner começará a testar os caminhos.

---

## Exemplo de saída

```
*DIRPY 1.4
*Author Vortex
============================================================
INFO ALVO
~ Site:https://example.com = [93.xxx.xxx.xxx]
~ Server:[nginx]
============================================================
METHOD GET

[+] Directory found /admin, status: 200

[~] Redirect page /login, status: 302

Forbidden/Unauthorized (possible protected dir) /private 403
```

---

## Estrutura do projeto

```
DIRPY/
│
├── dirpy.py
├── wordlist.txt
├── README.md
└── requirements.txt
```

---

## Tecnologias utilizadas

* Python
* Requests
* HTTP
* Socket
* Pathlib

---

## Melhorias futuras

Possíveis funcionalidades para versões futuras:

* [ ] Scan multithread.
* [ ] Suporte para extensões (`.php`, `.html`, `.txt`).
* [ ] Exportação dos resultados.
* [ ] Argumentos via CLI usando argparse.
* [ ] Barra de progresso.
* [ ] Detecção de WAF.
* [ ] Suporte para múltiplas URLs.

---

## Aviso

Esta ferramenta foi criada para **estudo, aprendizado e testes autorizados**.

Não utilize contra sistemas sem permissão.

O usuário é responsável pelo uso da ferramenta.

---

## Autor

**Vortex**

Projeto desenvolvido para aprendizado em Python e segurança web.
