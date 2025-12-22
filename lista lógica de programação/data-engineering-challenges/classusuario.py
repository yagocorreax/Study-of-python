from datetime import date

class usuario:
    
    def __init__ (self, primeiro_nome, sobrenome, ultimo_nome, ano_nascimento, email, number_cellphone):
        self.primeiro_nome = primeiro_nome
        self.sobrenome= sobrenome
        self.ultimo_nome = ultimo_nome
        self.ano_nascimento = ano_nascimento
        self.email = email
        self.number_cellphone = number_cellphone

    def nome_completo(self):
        return f"{self.primeiro_nome} {self.sobrenome} {self.ultimo_nome}"
    
    def calcular_idade(self):
        ano_atual = date.today().year
        return ano_atual - self.ano_nascimento





