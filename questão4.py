class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)
    
    def engordar(self, peso_ganho):
        self.peso += peso_ganho
    
    def emagrecer(self, peso_perdido):
        self.peso -= peso_perdido
    
    def crescer(self, altura_ganha):
        self.altura += altura_ganha

# Exemplo de uso da classe
pessoa1 = Pessoa("João", 18, 70, 170)
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, Peso: {pessoa1.peso}, Altura: {pessoa1.altura}")

pessoa1.envelhecer(2)
pessoa1.engordar(5)
pessoa1.emagrecer(3)
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, Peso: {pessoa1.peso}, Altura: {pessoa1.altura}")
