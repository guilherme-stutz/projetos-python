from datetime import date
ano=int(input('Digite seu ano de nascimento: '))
hoje=int(date.today().year)
idade=int(hoje-ano)
if idade<=9:
    print(f'Você tem {idade} anos, e sua categoria é MIRIM.')
elif idade<=14:
    print(f'Você tem {idade} anos, e sua categoria é INFANTIL.')
elif idade<=19:
    print(f'Você tem {idade} anos, e sua categoria é JÚNIOR.')
elif idade<=25:
    print(f'Você tem {idade} anos, e sua categoria é SÊNIOR. ')
elif idade>25:
    print(f'Você tem {idade} anos, e sua  categoria é MASTER.')
print('Boa sorte na competição!!')
