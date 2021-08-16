from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

class Escola() :
    def __init__(self):
        self.__nome = "Escola dos Programadores do Edutech"

        fulano = Aluno("Fulano da Silva", "000.001.002-03", "1234", "3º B")
        bento = Aluno("Bento José", "001.002.003-04", "999.888", "4º B")
        jose = Professor("Jose da Silva", "999.888.777-66", "Geografia", "concursado")
        severino = Funcionario("Severino de Oliveira", "111.222.333-44", "Porteiro", "08h as 17h")

        self.__pessoas = [fulano, bento, jose, severino]

    def __getitem__(self, item):
        return self.__pessoas[item]

    def __len__(self):
        return len(self.__pessoas)

    def solicitaAcesso(self):
        codigo_acesso = input("Qual o seu código de acesso: ")
        for p in self.__pessoas :
            if(p.acessarEscola(codigo_acesso)):
                return True
        print('Acesso Negado!')
        return False;
