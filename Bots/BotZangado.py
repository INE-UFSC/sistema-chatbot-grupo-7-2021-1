from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome):
        comandos = {'Bom dia': 'Grrr..tenho mais o que fazer.', 'Qual seu nome?':'{}... Quer brigar?'.format(nome), 'Quero um conselho':'Tenho cara de conselheiro?', 'Adeus':'Espero que não volte!'}
        super().__init__(nome, comandos)

    def apresentacao(self):
        self.boas_vindas()
    
    def executa_comando(self,cmd):
        return self.comandos[cmd]

    def boas_vindas(self):
        return 'Não quero papo hoje...'

    def despedida(self):
        return self.comandos['Adeus']