from random import randint
cp=randint(0,10)
quantos=0
print('-'*60)
print('Vou pensar em um número de 0-10 e quero que você adivinhe!')
print('-'*60)
n=int(input('Digite o número que voce acha que estou pensando: '))
while cp != n:
    if cp != n:
        quantos+=1
    if cp > n:
        print('Mais...')
    if cp < n:
        print('Menos...')
    n = int(input('Tente novamente: '))
print(f'Parabéns, você acertou! \nE conseguiu em {quantos + 1} tentativa(s).')
