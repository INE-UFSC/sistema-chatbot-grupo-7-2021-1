from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self, nome):
        comandos = {'Bom dia': 'Bom dia? O que tem de bom no dia?', 'Qual seu nome?':'Meu nome é {} ! :) '.format(nome), 'Quero um conselho':'Siga a tua angústia, ela é o caminho rumo a ti mesmo.', 'Adeus':'Adeus, espero que encontre a felicidade...'}
        super().__init__(nome, comandos)

    def apresentacao(self):
        self.boas_vindas()
    
    def executa_comando(self,cmd):
        return self.comandos[cmd]

    def boas_vindas(self):
        return ' Nossa dor vem da distância entre aquilo que somos e aquilo que idealizamos ser... Ola? '

    def despedida(self):
        return self.comandos['Adeus']