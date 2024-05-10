import google.generativeai as genai
import sys
import os

# Configurar a API key de forma segura
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    sys.exit("API Key não configurada corretamente.")

genai.configure(api_key=GOOGLE_API_KEY)

# Iniciar o modelo generativo
model = genai.GenerativeModel()

# Função para gerar respostas a perguntas médicas
def ask_medical_question(question):
    try:
        # Gerar resposta do modelo
        response = model.generate_content(question)

        # Verificar tipo de resposta e extrair texto
        if isinstance(response, dict) and 'text' in response:
            answer_text = response['text']
        else:
            answer_text = "Erro ao obter resposta do modelo."
    except Exception as e:
        answer_text = f"Desculpe, ocorreu um erro: {str(e)}"
        log_error(e)  # Função hipotética para registrar erros

    # Imprimir resposta
    print(f"Resposta: {answer_text}\n")
    return answer_text

def log_error(error):
    # Implementar registro de logs de erro
    pass

# Loop de perguntas e respostas
def chat_loop():
    history = []  # Adiciona uma lista para armazenar o histórico do chat
    prompt = input("Digite sua pergunta médica ou 'sair' para encerrar: ").strip().lower()
    while prompt not in ['fim', 'sair', 'encerrar']:
        if prompt == "":
            print("Por favor, digite uma pergunta válida.")
        else:
            response = ask_medical_question(prompt)
            history.append((prompt, response))  # Adiciona a pergunta e a resposta ao histórico
        prompt = input("Digite sua pergunta médica ou 'sair' para encerrar: ").strip().lower()

    print("Chat encerrado. Obrigado por usar nosso serviço!")
    return history  # Retorna o histórico do chat no final

# Iniciar o loop de chat
if __name__ == "__main__":
    chat_history = chat_loop()
    
