class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudarLado(self, novo_tamanho_lado):
        self.tamanho_lado = novo_tamanho_lado

    def retornarLado(self):
        return self.tamanho_lado

    def calcularArea(self):
        return self.tamanho_lado ** 2

meu_quadrado = Quadrado(tamanho_lado=4)

print("Tamanho do lado:", meu_quadrado.retornarLado())

print("Área do quadrado:", meu_quadrado.calcularArea())

meu_quadrado.mudarLado(8)

print("Novo tamanho do lado:", meu_quadrado.retornarLado())

print("Nova área do quadrado:", meu_quadrado.calcularArea())
