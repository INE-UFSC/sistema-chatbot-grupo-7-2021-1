#encoding: utf-8
from Bots.BotFeliz import BotFeliz
from Bots.BotTriste import BotTriste
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"),BotFeliz('Felizciano'),BotTriste('nietzsche Pereira')]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
