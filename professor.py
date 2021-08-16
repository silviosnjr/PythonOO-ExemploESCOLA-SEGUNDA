from pessoa_fisica import PessoaFisica

class Professor(PessoaFisica):
    def __init__(self, nome, cpf, formacao, tipo_vinculo):
        super().__init__(nome, cpf)
        self.__formacao = formacao
        self.__tipo_vinculo = tipo_vinculo

    @property
    def formacao(self):
        return self.__formacao

    @property
    def tipo_vinculo(self):
        return self.__tipo_vinculo

    def __str__(self):
        return "Professor: "+super().nome+" | CPF: "+super().cpf+" | Formação: "+self.__formacao+" | Vínculo: "+self.__tipo_vinculo

    def acessarEscola(self, codigo_acesso):
        if (codigo_acesso == super().cpf):
            print("Boa aula professor(a) "+super().nome)
            return True
        else:
            return False