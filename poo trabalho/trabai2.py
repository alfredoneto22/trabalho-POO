from jogo import JogoDeAdivinhacao  # Importando a classe do arquivo jogo.py

class Main:
    def __init__(self):
        self.jogo = JogoDeAdivinhacao()  # Cria uma instância do jogo

    def rodar(self):
        self.jogo.iniciar()  # Inicia o jogo de adivinhação

# Código para rodar o jogo
if __name__ == "__main__":
    main = Main()  # Cria uma instância da classe Main
    main.rodar()  # Executa o método que inicia o jogo