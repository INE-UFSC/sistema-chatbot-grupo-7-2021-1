##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):
    def __init__(self, nome, comandos={}):
        self.__nome = nome
        self.__comandos = comandos #{'bom dia':'Bom dia meu nome é tal', 'Adeus':'tchau'}

    #nao esquecer o decorator
    @property
    def nome(self):
        return self.__nome

    #nao esquecer o decorator
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    def mostra_comandos(self):
        for pos,cmd in enumerate(self.comandos.keys()):
            print(f'{pos+1} - {cmd}')

    @abstractmethod
    def apresentacao(self):
        pass

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass