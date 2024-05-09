import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyA7CYrTtyMzBctjh-XXNdRLFXCERHNhBDc"
genai.configure(api_key=GOOGLE_API_KEY)

# Listar os modelos disponiveis.
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

generation_config = {
    "candidate_count": 1,
    "temperature": 0.5,
}

safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

# Inicializando o modelo
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

reponse = model.generate_content("Vamos aprender conteúdo de IA. Me dê sugestôes.")
print(reponse.text)

chat = model.start_chat(history=[])

prompt = input("Esperando prompt: ")

while prompt != "fim":
  response = chat.send_message(prompt)
  print("resposta: ", response.text, "\n")
  prompt = input("Esperando prompt: ")