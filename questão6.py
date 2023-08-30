class TV:
    def __init__(self, canal_inicial=1, volume_inicial=10):
        self.canal = canal_inicial
        self.volume = volume_inicial
    
    def mudar_canal(self, novo_canal):
        if 1 <= novo_canal <= 50:
            self.canal = novo_canal
            print(f"Canal alterado para {self.canal}")
        else:
            print("Canal inválido. Deve estar entre 1 e 50.")
    
    def aumentar_volume(self):
        if self.volume < 50:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}")
        else:
            print("Volume máximo alcançado.")
    
    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}")
        else:
            print("Volume mínimo alcançado.")

tv = TV()

while True:
    print("\n--- Televisor ---")
    print(f"Canal: {tv.canal}")
    print(f"Volume: {tv.volume}")
    print("1. Mudar Canal")
    print("2. Aumentar Volume")
    print("3. Diminuir Volume")
    print("0. Desligar")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        novo_canal = int(input("Escolha o novo número do canal: "))
        tv.mudar_canal(novo_canal)
    elif opcao == 2:
        tv.aumentar_volume()
    elif opcao == 3:
        tv.diminuir_volume()
    elif opcao == 0:
        print("Desligando...")
        break
    else:
        print("Opção inválida. Escolha uma opção válida.")
