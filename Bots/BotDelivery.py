from Bots.Bot import Bot

class BotDelivery(Bot):
    def __init__(self, nome):
        comandos = {'Bom dia': 'Bom dia, gostaria de experimentar o especial do dia?', 'Qual seu nome?':'Meu nome é {}, posso anotar seu pedido?'.format(nome), 'Quero um conselho':'Não servimos conselhos, apenas hamburguer e batata frita...', 'Adeus':'Até mais, volte sempre!...'}
        super().__init__(nome, comandos)

    def apresentacao(self):
        self.boas_vindas()
    
    def executa_comando(self,cmd):
        return self.comandos[cmd]

    def boas_vindas(self):
        return 'Estou aqui para atender seu pedido!'

    def despedida(self):
        return self.comandos['Adeus']
