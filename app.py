#encoding: utf-8
from Bots.BotDelivery import BotDelivery
from Bots.BotFeliz import BotFeliz
from Bots.BotTriste import BotTriste
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Zangiano da Silva"),BotFeliz('Felizciano'),BotTriste('nietzsche Pereira'), BotDelivery('McDonalds Bot')]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
