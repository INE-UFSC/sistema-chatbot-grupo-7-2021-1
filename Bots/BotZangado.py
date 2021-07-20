from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome):
        comandos = {'Bom dia': 'F*da-se', 'Qual seu nome?':'Te interessa?', 'Quero um conselho':'Vai embora!', 'Adeus':'Espero que não volte!'}
        super().__init__(nome, comandos)

    def apresentacao(self):
        self.boas_vindas()
    
    def executa_comando(self,cmd):
        return self.comandos[cmd]

    def boas_vindas(self):
        return f'Não quero papo hoje...'

    def despedida(self):
        return self.comandos['Adeus']