from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        url = 'https://email-sending-bot.onrender.com/send_email'
        email_list = request.form['content']
        email_list = email_list.replace(" ", "").split(",")
        email = request.form['email']
        senha = request.form['senha']
        assunto = request.form['ass']
        mensagem = request.form['mensagem']
        data = {
            "email": email,
            "senha": senha,
            "destinatarios": email_list,
            "assunto": assunto,
            "mensagem": mensagem
            }
        result = requests.post(url=url, json=data)
        return render_template("send_email.html", email_list = email_list)
    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)