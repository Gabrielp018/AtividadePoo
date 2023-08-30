class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def imprimir(self):
        print(f"({self.x}, {self.y})")

class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura
    
    def encontrar_centro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)

def exibir_menu():
    print("1. Criar Retângulo")
    print("2. Alterar Retângulo")
    print("3. Mostrar Centro do Retângulo")
    print("0. Sair")

retangulo = None

while True:
    exibir_menu()
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        x = float(input("Digite a coordenada x do vértice inferior esquerdo: "))
        y = float(input("Digite a coordenada y do vértice inferior esquerdo: "))
        largura = float(input("Digite a largura do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        retangulo = Retangulo(Ponto(x, y), largura, altura)
        print("Retângulo criado.")
    elif opcao == 2:
        if retangulo:
            x = float(input("Digite a coordenada x do vértice inferior esquerdo: "))
            y = float(input("Digite a coordenada y do vértice inferior esquerdo: "))
            largura = float(input("Digite a largura do retângulo: "))
            altura = float(input("Digite a altura do retângulo: "))
            retangulo.ponto_inicial = Ponto(x, y)
            retangulo.largura = largura
            retangulo.altura = altura
            print("Retângulo alterado.")
        else:
            print("Crie um retângulo primeiro.")
    elif opcao == 3:
        if retangulo:
            centro = retangulo.encontrar_centro()
            print("Centro do Retângulo:")
            centro.imprimir()
        else:
            print("Crie um retângulo primeiro.")
    elif opcao == 0:
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Digite uma opção válida.")
