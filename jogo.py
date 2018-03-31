class Robo:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def subir(self):
        self.y += 10
        return self.x, self.y
    
    def descer(self):
        if self.y >= 10:
            self.y -= 10
            return self.x, self.y
        else: 
            print('Ops, comando inválido')
            return self.x, self.y
    
    def andar_esquerda(self):
        if self.x >= 10:
            self.x -= 10
            return self.x, self.y
        else: 
            print('Ops, comando inválido')
            return self.x, self.y
        
    def andar_direita(self):
        self.x += 10
        return self.x, self.y
    
    
r2d2 = Robo(0, 0)

print('------------------------------------------')
print('         MEU JOGO - ROBO                  ')
print('------------------------------------------')
print(' Código das operações: ')
print(' 1. Descer')
print(' 2. Subir')
print(' 3. Direita')
print(' 4. Esquerda')
print(' 0. Sair')
print('------------------------------------------')
nome = input('Qual o seu nome? ')
print('JOGADOR(A): ' + nome) 
print('------------------------------------------')

movimento = ''

while movimento != 0:
    movimento = int(input("Digite o código da operação desejada: "))

    if movimento == 0:
        print('Fim da execução')
        print('')
        break
    elif movimento == 1:
        print('Estou descendo: ' + str(r2d2.descer()))
        print('')
    elif movimento == 2:
        print('Estou subindo: ' + str(r2d2.subir()))
        print('')
    elif movimento == 3:
        print('Estou andando para direita: ' + str(r2d2.andar_direita()))
        print('')
    elif movimento == 4:
        print('Estou andando para esquerda: ' + str(r2d2.andar_esquerda()))    
        print('')
    else:
        print('Comando inválido')    
        print('')