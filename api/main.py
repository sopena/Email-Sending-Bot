from fastapi import FastAPI
from pydantic import BaseModel
from bot_api import disparar_emails

app = FastAPI()

class UserEntry(BaseModel):
    email: str
    senha: str
    destinatarios: list
    assunto: str
    mensagem: str

@app.post("/send_email")
def send_emails(user_entry: UserEntry):
    user_data = user_entry.dict()

    result = disparar_emails(user_data["destinatarios"], user_data["assunto"], user_data["mensagem"], user_data['email'], user_data['senha'])
    for i in result: print(i)

# cd api
# uvicorn main:app --reload