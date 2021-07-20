from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa = nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots = lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        print(f'Olá esse é o sistema de chatbots da empresa {self.__empresa}')
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print('Os chats disponíveis no momento são: ')
        print('\u001b[36;1m',end='')
        print('-'*60)
        print('\u001b[0;1m', end='')
        for pos,bot in enumerate(self.__lista_bots):
            print(f'{pos} - Bot: {bot.nome} - Mensagem de apresentação: {bot.boas_vindas()}')
            print('\u001b[36;1m',end='')
            print('- '*30)
            print('\u001b[0;1m',end='')
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        escolha = int(input('\nDigite o número do chat bot desejado: '))
        print('\u001b[36;1m',end='')
        print('-'*60)
        print('\u001b[0;1m', end='')
        self.__bot = self.__lista_bots[escolha]
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):
        while True:
            self.__bot.mostra_comandos()
            escolha = self.le_envia_comando()
            if escolha == 4:
                break

        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        escolha = int(input('\nDigite o comando desejado (ou -1 para fechar o programa): '))
        if escolha == -1:
            exe = self.__bot.despedida()
            print('\u001b[36;1m',end='')
            print('-'*60)
            print('\u001b[0;1m', end='')
            print(f'\n--> {self.__bot.nome} diz: {exe}\n')
            print('\u001b[36;1m',end='')
            print('-'*60)
            print('\u001b[0;1m', end='')
            quit()
        for pos,cmd in enumerate(self.__bot.comandos.keys()):
            if escolha-1 == pos:
                exe = self.__bot.executa_comando(cmd)
                print('\u001b[36;1m',end='')
                print('-'*60)
                print('\u001b[0;1m', end='')
                print(f'\n--> {self.__bot.nome} diz: {exe}\n')
                print('\u001b[36;1m',end='')
                print('-'*60)
                print('\u001b[0;1m', end='')
                break
        return escolha
        
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        print('\u001b[36;1m',end='')
        print('='*60)
        self.boas_vindas()
        print('='*60)
        print('\u001b[0;1m')
        while True:
            self.mostra_menu()
            self.escolhe_bot()
            self.__bot.boas_vindas()
            self.mostra_comandos_bot()
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
