class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor

minha_bola = Bola(cor="branca", circunferencia=8, material="borracha")

print("Cor atual da bola:", minha_bola.mostraCor())

minha_bola.trocaCor("azul")

print("Nova cor da bola:", minha_bola.mostraCor())
