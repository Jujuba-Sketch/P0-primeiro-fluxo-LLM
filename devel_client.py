import os
import requests
from dotenv import load_dotenv
import sys

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL" , "gemini-4-hydrogen")
if not GEMINI_API_KEY:
    print("Erro: GEMINI_API_KEY não encontrada. Configure no arquivo .env antes de rodar.")
    sys.exit(1)

def resumir_texto (texto):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"
    params = {"key": GEMINI_API_KEY}
    instrucao = (
    "Atue como um assistente de resumo e organize esse texto, de forma que seja "
    "resumido com as principais ideias, em tópicos objetivos, com pontos chave, "
    "para entender o conteúdo. Não invente informações e não seja redundante, seja objetivo.\n\n"
    f"{texto}: \n{texto}"
    )

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": instrucao}
                ]
            }
        ]
    }

    try:
        resposta = requests.post(url, params = params , json = payload, timeout = 30)
        resposta.raise_for_status()
        dados = resposta.json()
        candidates = dados.get("candidates") or []
        if not candidates:
            print("Nenhuma resposta recebida do modelo.")
            return None
        content = candidates[0].get("content") or {}
        parts = content.get("parts") or []
        if not parts:
            print("A resposta da API não retornou conteúdo de texto.")
            return None
        return parts[0].get("text", "").strip()
        return dados.get("response", "")
    except requests.exceptions.RequestException as erro :
        print(f"Erro ao conectar ao servidor: {erro}")
        return None

if __name__ == "__main__":
    texto_usuario = input(" Digite ou cole seu texto aqui:")
    resumo = resumir_texto(texto_usuario)
    print(resumo)