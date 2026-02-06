import random
print('Vamos jogar Jokenpô!')
lista=['pedra', 'papel', 'tesoura']
print('''Digite uma das palavras abaixo:
[ 1 ] - Pedra
[ 2 ] - Papel
[ 3 ] - Tesoura''')
escolha=str(input('Digite sua escolha: ')).title()
if escolha=='Pedra':
    resultado=random.choice(lista).title()
    if resultado=='Papel':
        print(f'Você escolheu {escolha} e eu escolhi {resultado}, então EU ganhei!')
    elif resultado=='tesoura':
        print(f'Você escolheu {escolha} e eu escolhi {resultado}, então VOCÊ ganhou!')
    else:
        print(f'Nós dois escolhemos {escolha}, então deu empate.')
elif escolha=='Papel':
    resultado=random.choice(lista).title()
    if resultado=='Pedra':
        print(f'Você escolheu {escolha} e eu escolhi {resultado}, então VOCÊ ganhou! ')
    elif resultado=='Tesoura':
        print(f'Você escolheu {escolha} e eu escolhi {resultado}, entâo EU ganhei!')
    else:
        print(f'Nós dois escolhemos {escolha}, então deu empate.')
elif escolha =='Tesoura':
    resultado=random.choice(lista).title()
    if resultado=='Pedra':
        print(f'Você escolheu {escolha} e eu escolhi {resultado}, então EU ganhei!')
    elif resultado=='Papel':
        print(f'Você escolheu {escolha} e eu escolhi {resultado}, então VOCÊ ganhou!')
    else:
        print(f'Nós dois escolhemos {escolha}, então deu empate.')
else:
    print('OPÇÃO INVÁLIDA! \nTente novamente!')
