class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
    
    def abastecer_por_valor(self, valor_abastecido):
        quantidade_litros = valor_abastecido / self.valor_litro
        self.quantidade_combustivel -= quantidade_litros
        return quantidade_litros
    
    def abastecer_por_litro(self, quantidade_litros):
        valor_pagar = quantidade_litros * self.valor_litro
        self.quantidade_combustivel -= quantidade_litros
        return valor_pagar
    
    def alterar_valor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro
    
    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel
    
    def alterar_quantidade_combustivel(self, nova_quantidade_combustivel):
        self.quantidade_combustivel = nova_quantidade_combustivel
    
bomba = BombaCombustivel("Gasolina", 5.0, 1000)

print("Tipo de Combustível:", bomba.tipo_combustivel)
print("Valor do Litro:", bomba.valor_litro)
print("Quantidade de Combustível:", bomba.quantidade_combustivel)

litros_abastecidos = bomba.abastecer_por_valor(50)
print(f"Litros abastecidos: {litros_abastecidos:.2f}")
print("Quantidade de Combustível após abastecimento:", bomba.quantidade_combustivel)

valor_pagar = bomba.abastecer_por_litro(10)
print(f"Valor a pagar: R${valor_pagar:.2f}")
print("Quantidade de Combustível após abastecimento:", bomba.quantidade_combustivel)

bomba.alterar_valor(4.8)
bomba.alterar_combustivel("Álcool")
bomba.alterar_quantidade_combustivel(800)

print("Tipo de Combustível:", bomba.tipo_combustivel)
print("Valor do Litro:", bomba.valor_litro)
print("Quantidade de Combustível:", bomba.quantidade_combustivel)
