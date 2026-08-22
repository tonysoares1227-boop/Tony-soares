def nossa_ia(pergunta):
    pergunta = pergunta.lower()

    if "olá" in pergunta or "oi" in pergunta:
        return "Olá! Eu sou a nossa primeira IA. 🚀"

    if "seu nome" in pergunta:
        return "Meu nome ainda está sendo construído por nós! 🤖"

    if "ajuda" in pergunta:
        return "Claro! Estou aqui para ajudar. Digite sua pergunta."

    return "Entendi sua pergunta. Ainda estou aprendendo, mas vamos evoluir juntos! 💪"


print("🤖 Nossa IA está funcionando!")
print("Digite uma pergunta:")

while True:
    pergunta = input("> ")

    if pergunta.lower() == "sair":
        print("Até logo! 🚀")
        break

    resposta = nossa_ia(pergunta)
    print(resposta)
