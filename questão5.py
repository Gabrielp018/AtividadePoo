class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
    
    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome
    
    def depósito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Valor inválido para depósito.")
    
    def saque(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

conta1 = ContaCorrente("321123", "Gabriel Pereira")
print(f"Número da Conta: {conta1.numero_conta}, Correntista: {conta1.nome_correntista}, Saldo: R${conta1.saldo:.2f}")

conta1.depósito(1000)
conta1.saque(500)
conta1.alterarNome("Gabriel Pereira")
print(f"Número da Conta: {conta1.numero_conta}, Correntista: {conta1.nome_correntista}, Saldo: R${conta1.saldo:.2f}")
