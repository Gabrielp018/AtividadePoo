class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudarLados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornarLados(self):
        return self.lado_a, self.lado_b

    def calcularArea(self):
        return self.lado_a * self.lado_b

    def calcularPerimetro(self):
        return 2 * (self.lado_a + self.lado_b)

if __name__ == "__main__":
    comprimento = float(input("Informe o comprimento do local: "))
    largura = float(input("Informe a largura do local: "))

    meu_retangulo = Retangulo(comprimento, largura)

    area_total = meu_retangulo.calcularArea()
    perimetro_total = meu_retangulo.calcularPerimetro()

    tamanho_piso = float(input("Informe o tamanho do piso: "))
    tamanho_rodape = float(input("Informe o tamanho do rodapé: "))

    area_piso = tamanho_piso ** 2
    area_rodape = tamanho_rodape * perimetro_total

    quantidade_pisos = area_total / area_piso
    quantidade_rodapes = perimetro_total / tamanho_rodape

    print(f"Quantidade de pisos necessários: {quantidade_pisos:.2f}")
    print(f"Quantidade de rodapés necessários: {quantidade_rodapes:.2f}")
