# Salve sua classe em JSON
# Salve os dados da sua classe em JSON

import json
pessoas_cadastradas = {}
class Pessoa:

    
    arquiv_de_cadastrados = "record.json"

    def __init__(self, nome, idade, sexo, cpf):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf

    def questionario(self):
        print("Questionário de cadastro de pessoas \n")
        self.nome = input("Digite o nome da pessoa a ser cadastrada: \n")
        self.idade = input("Digite a idade da pessoa a ser cadastrada: \n")
        self.sexo = input("Digite o sexo da pessoa a ser cadastrada: \n")
        self.cpf = input("Digite o CPF da pessoa a ser cadastrada: \n")
        return (self.nome, self.idade, self.sexo, self.cpf)

while True:
    comando = str.lower(input("Digite [A]dicionar para adicionar usuário ou [S]air para sair do modo de cadastro \n"))
    # Criando uma instância da classe Pessoa
    if comando =="a":
        pessoa1 = Pessoa("", "", "", "")  # Os valores iniciais estão vazios, pois serão preenchidos pelo questionário
        pessoa1.questionario()  # Preenche os dados do objeto
        # Adicionando a pessoa ao dicionário de pessoas cadastradas
        pessoas_cadastradas[pessoa1.nome] = pessoa1.__dict__
        print(pessoas_cadastradas)
        print(pessoas_cadastradas)
        with open('record.json', 'w+', encoding='utf8') as arquivo:
            json.dump(pessoas_cadastradas, arquivo, ensure_ascii=False,indent=2,)
    elif comando != "s" and "a":
        print("Opção inválida, digite [A] ou [S]")
    elif comando == "s":
        print(pessoas_cadastradas)
        break
        