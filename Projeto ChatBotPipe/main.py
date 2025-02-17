#pip install nltk numpy tensorflow

from chatbot import ChatBot
myChatBot = ChatBot()

#apenas carregar um modelo pronto
#myChatBot.loadModel()

#criar o modelo
myChatBot.createModel()

print("=======================================")
print("Livia Lumi Miyabara - 22.122.045-2")
print("Marcio Forner N. Almeida- 22.122.040-3")
print("Thiago Garcia - 22.122.003-1")
print("========================================")
print("Bem-vindo(a) ao chatbot do PIPE/FAPESP!")
print("========================================")

pergunta = input("Como posso te ajudar? \n")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   ["+intencao[0]['intent']+"]")

while (intencao[0]['intent']!="despedida"):
    pergunta = input("Posso lhe ajudar com algo a mais?\n")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta + "   [" + intencao[0]['intent'] + "]")

print("Foi um prazer atendê-lo")
