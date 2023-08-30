class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []
    
    def comer(self, alimento):
        self.bucho.append(alimento)
    
    def ver_bucho(self):
        return self.bucho
    
    def digerir(self):
        if self.bucho:
            self.bucho = []
            print(f"{self.nome} digeriu o alimento.")
        else:
            print(f"{self.nome} não tem nenhum alimento no estômago para digerir.")

macaco1 = Macaco("Pedro")
macaco2 = Macaco("Joana")

alimentos = ["banana", "melão", "maçã"]

for alimento in alimentos:
    macaco1.comer(alimento)
    macaco2.comer(alimento)

print(f"Bucho de {macaco1.nome}: {macaco1.ver_bucho()}")
print(f"Bucho de {macaco2.nome}: {macaco2.ver_bucho()}")

macaco1.digerir()
macaco2.digerir()

print(f"Bucho de {macaco1.nome}: {macaco1.ver_bucho()}")
print(f"Bucho de {macaco2.nome}: {macaco2.ver_bucho()}")
