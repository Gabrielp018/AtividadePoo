class BichinhoVirtual:
    def __init__(self, nome, fome=0, saude=100, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
    
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
    
    def alterar_fome(self, novo_valor):
        self.fome = novo_valor
    
    def alterar_saude(self, novo_valor):
        self.saude = novo_valor
    
    def alterar_idade(self, novo_valor):
        self.idade = novo_valor
    
    def retornar_nome(self):
        return self.nome
    
    def retornar_fome(self):
        return self.fome
    
    def retornar_saude(self):
        return self.saude
    
    def retornar_idade(self):
        return self.idade
    
    def calcular_humor(self):
        return (self.fome + self.saude) / 2

bichinho = BichinhoVirtual("Zézin")
print(f"Nome: {bichinho.retornar_nome()}, Fome: {bichinho.retornar_fome()}, Saúde: {bichinho.retornar_saude()}, Idade: {bichinho.retornar_idade()}, Humor: {bichinho.calcular_humor()}")

bichinho.alterar_fome(60)
bichinho.alterar_saude(80)
bichinho.alterar_idade(1)
print(f"Nome: {bichinho.retornar_nome()}, Fome: {bichinho.retornar_fome()}, Saúde: {bichinho.retornar_saude()}, Idade: {bichinho.retornar_idade()}, Humor: {bichinho.calcular_humor()}")
