from aluno import Aluno
from Professor import professor

aluno = Aluno("Fulano da Silva", "000.001.002-03", "1234", "3º B")
professor = professor("Jose da Silva", "999.888.777-66", "Geografia", "concursado")

pessoas = [aluno, professor]

for pessoa in pessoas :
    print(pessoa)