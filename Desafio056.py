maiorih=0
nomevelho=''
somai=0
mediai=0
totmulher20=0
q=int(input('Digite quantas pessoas irão participar: '))
for p in range(1,q+1):
    print('-'*10,f'{p}ª PESSOA', '-'*10)
    nome=str(input('Nome: ')).title()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo (M/F): ')).upper()
    somai= somai + idade
    if p==1 and sexo=='M':
        maiorih=idade
        nomevelho=nome
    if sexo=='M' and idade > maiorih:
        maiorih = idade
        nomevelho = nome
    if sexo=='F' and idade<20:
        totmulher20 = totmulher20 + 1
mediai = somai / q

print(f'\nA média da idade dos {q} participantes é de {mediai} anos.')
print(f'O homem mais velho tem {maiorih} anos e se chama {nomevelho}.')
print(f'Ao todo {totmulher20} mulher(es) tem menos de 20 anos.')
