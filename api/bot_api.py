import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def disparar_emails(lista, ass, msg, email, senha):
    result = []
    for mail in lista:
        result.append(enviar_email(mail, ass, msg, email, senha))
    return result
        
def enviar_email(destinatario, assunto, corpo, email, senha):
    try:
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(email, senha)
        remetente = email

        msg = MIMEMultipart()
        msg["From"] = remetente
        msg["To"] = destinatario
        msg["Subject"] = assunto
        msg.attach(MIMEText(corpo, "plain", "utf-8"))

        smtp_server.sendmail(remetente, destinatario, msg.as_string())
        smtp_server.quit()
        return f"Email enviado com sucesso para {destinatario}"
        
        
    except Exception as e:
        return print(f"Erro ao enviar email: {e}")