import os
import requests
import urllib3
from dotenv import load_dotenv

load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


OLLAMA_HOST = os.getenv("OLLAMA_HOST" , "https://llm-internal.softex:9001")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL" , "qwen3.5")

def resumir_texto (texto):
    url = f"{OLLAMA_HOST}/api/generate"
    instrucao = (
    "Atue como um assistente de resumo e organize esse texto, de forma que seja "
    "resumido com as principais ideias, em tópicos objetivos, com pontos chave, "
    "para entender o conteúdo. Não invente informações e não seja redundante, seja objetivo.\n\n"
    f"{texto}"
)
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": instrucao,
        "stream": False,
    }
    try:
        resposta = requests.post(url, json=payload, verify=False)
        resposta.raise_for_status()
        dados = resposta.json()
        return dados.get("response", "")
    except requests.exceptions.RequestException as erro :
        print(f"Erro ao conectar ao servidor: {erro}")
        return None

if __name__ == "__main__":
    texto_usuario = input(" Digite ou cole seu texto aqui:")
    resumo = resumir_texto(texto_usuario)
    print(resumo)