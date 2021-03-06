from pessoa_fisica import PessoaFisica

class Aluno(PessoaFisica):
    def __init__(self, nome, cpf, numero_cgm, turma):
        super().__init__(nome, cpf)
        self.__cgm = numero_cgm
        self.__turma = turma

    @property
    def cgm(self):
        return self.__cgm

    @property
    def turma(self):
        return self.__turma

    def __str__(self):
        return "Aluno: "+super().nome+" | CPF: "+super().cpf+" | CGM: "+self.__cgm+" | Turma: "+self.turma;

    def acessarEscola(self, codigo_acesso):
        if(codigo_acesso == self.__cgm):
            print("Boa aula aluno(a) "+super().nome)
            return True
        else :
            return False