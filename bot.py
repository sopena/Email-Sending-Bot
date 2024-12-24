import smtplib
import email as mail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import schedule
import os

load_dotenv()
email = os.getenv("EMAIL")
senha = os.getenv("PASSWORD")

def disparar_emails(lista, ass, msg):
    with open(lista, 'r', encoding="utf-8") as arquivo:
        emails = arquivo.readlines()
        for email in emails:
            enviar_email(email.strip(), ass, msg)
        
def enviar_email(destinatario, assunto, corpo):
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
        print(f"Email enviado com sucesso para {destinatario}")
        smtp_server.quit()
        
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
        

lista = r"C:\Users\sopena\Documents\Programacao\Projetos\EmailBot\email_list.txt"
assunto = "Assunto Automático"
msg = "Oi, esse é um email enviado pelo bot!"

disparar_emails(lista, assunto, msg)