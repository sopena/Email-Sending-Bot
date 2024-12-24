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

@app.get("/")
def read_root():
    return {"message": "API funcionando corretamente!"}

@app.post("/send_email")
def send_emails(user_entry: UserEntry):
    user_data = user_entry.dict()

    result = disparar_emails(user_data["destinatarios"], user_data["assunto"], user_data["mensagem"], user_data['email'], user_data['senha'])
    return result

# cd api
# uvicorn main:app --reload