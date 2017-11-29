# -*- coding: utf8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import pyttsx



bot = ChatBot("test")

conv = ["oi","olá","olá","bom dia","boa tarde","boa noite","me chamo Bolt python e você?","eu estou bem","o que gosta de fazer","gosto de computação","quem te criou?","meu criador se chama Washington","adoraria ter um corpo","gosto de aprender com humanos","estou buscando dados","ate mais","tem amigos?","que ser meu amigo?","desconectando..."]
en = pyttsx.init()
en.setProperty("voice",b"brazil")


bot.set_trainer(ListTrainer)
bot.train(conv)

while True:
   quest = input("você: ")
   response = bot.get_response(quest)
   print("Bolt:",response)
   if quest == "tchau" :

      break
   en.say(response)
   en.runAndWait()

conversa = open("conversa.txt",'w')
conversa.write(str(conv))
conversa.close()
