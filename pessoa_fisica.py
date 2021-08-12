from abc import ABCMeta, abstractmethod

class PessoaFisica(metaclass = ABCMeta) :
    def __init__(self, texto_nome, numero_cpf):
        self.__nome = texto_nome
        self.__cpf = numero_cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @abstractmethod
    def __str__(self):
        pass
