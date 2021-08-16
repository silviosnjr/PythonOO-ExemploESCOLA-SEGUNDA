from pessoa_fisica import PessoaFisica

class Funcionario(PessoaFisica):
    def __init__(self, nome, cpf, cargo, horario):
        super().__init__(nome, cpf)
        self.__cargo = cargo
        self.__horario = horario

    @property
    def cargo(self):
        return self.__cargo

    @property
    def horario(self):
        return self.__horario

    def __str__(self):
        return "Funcionário: "+super().nome+" | CPF: "+super().cpf+" | Cargo: "+self.__cargo+" | Horário: "+self.__horario;

    def acessarEscola(self, codigo_acesso):
        if (codigo_acesso == super().cpf):
            print("Bom trabalho ,"+super().nome)
            return True
        else :
            return False