import random

class JogoDeAdivinhacao:
    def _init_(self):
        self.numero_secreto = random.randint(1, 100)  # Número aleatório entre 1 e 100
        self.tentativas = 0

    def iniciar(self):
        print("Bem-vindo ao Jogo de Adivinhação!")
        print("Eu escolhi um número entre 1 e 100. Tente adivinhar!")

        while True:
            try:
                # Solicita ao jogador que insira um palpite
                palpite = int(input("Digite seu palpite: "))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue

            self.tentativas += 1

            if palpite < self.numero_secreto:
                print("O número secreto é maior. Tente novamente!")
            elif palpite > self.numero_secreto:
                print("O número secreto é menor. Tente novamente!")
            else:
                print(f"Parabéns! Você acertou o número secreto {self.numero_secreto} em {self.tentativas} tentativas.")
                break  # Encerra o jogo após o acerto