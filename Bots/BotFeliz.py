from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome):
        comandos = {'Bom dia': 'Oiii, Bom Dia :D', 'Qual seu nome?':'Meu nome é {} ! :) '.format(nome), 'Quero um conselho':'Nunca faça hoje o que você pode deixar para amanhã!', 'Adeus':'Espero que tenha um ótimo dia, volte logo!'}
        super().__init__(nome, comandos)

    def apresentacao(self):
        self.boas_vindas()
    
    def executa_comando(self,cmd):
        return self.comandos[cmd]

    def boas_vindas(self):
        return 'O dia está lindo hoje não? Estou muito feliz...'

    def despedida(self):
        return self.comandos['Adeus']