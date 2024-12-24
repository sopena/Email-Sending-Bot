# Email Sending Bot

API que envia mensagens automáticas para uma lista de e-mails.

## Funcionalidades 🚀
- Envio automático de e-mails para uma lista de destinatários.
- Personalização do conteúdo da mensagem.

## Tecnologias Utilizadas 💻
- Python
- SMTP
- Render

## Como Usar 🔧

### 1. Clonar Repositório
Primeiro, clone o repositório para sua máquina local:

git clone [https://github.com/seuusuario/Email-Sending-Bot](https://github.com/sopena/Email-Sending-Bot)

### 2. Instalar Dependências
Instale as dependências necessárias com o pip:

pip install -r requirements.txt

### 3. Configuração
Defina as variáveis de ambiente necessárias no arquivo ".env" (EMAIL, PASSWORD)

OBS: A senha que será utilizada não é a senha do seu email e sim uma senha apropriada para esse uso, segue abaixo o tutorial para gerar essa senha.

Como gerar sua senha? 

- Entre no link: https://myaccount.google.com/security e ative averificação de duas etapas.
- Após isso entre neste outro link: https://myaccount.google.com/apppasswords e crie um app.
- Feito isso você terá recebido sua senha.

### 4. Rodando Servidor Localmente 
- Abra o terminal no diretório do projeto
- Entre na pasta api com o comando "cd api"
- Feito isso, digite "uvicorn main:app" no terminal
- Agora faça um Post usando Postman ou qualquer outra plataforma de teste de api -> (http://127.0.0.1:8000/send_email)
