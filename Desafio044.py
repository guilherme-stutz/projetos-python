print('\033[34m==========\033[m\033[1;33mNOME DA EMPRESA\033[m\033[34m==========\033[m')
preco=float(input('Qual o valor da compra: R$ '))
print('''\033[33m---\033[m\033[1;34mFORMAS DE PAGAMENTO\033[m\033[33m---\033[m
[ 1 ] - À vista no dinheiro/cheque: 10% de DESCONTO
[ 2 ] - À vista no cartão: 5% de DESCONTO
[ 3 ] - Em até 2x no cartão: Preço NORMAL
[ 4 ] - 3x ou mais: 20% de JUROS''')
opcao=int(input('Digite uma das opções acima: '))
if opcao==1:
    desconto=preco*10/100
    print(f'Sua compra de R${preco:.2f} vai sair por R${preco-desconto:.2f}.')
elif opcao==2:
    desconto=preco*5/100
    print(f'Sua compra de R${preco:.2f} vai sair por R${preco-desconto:.2f}')
elif opcao==3:
    print(f'Sua compra de R${preco:.2f} vai sair por R${preco:.2f}.\nSerão 2x de R${preco/2:.2f}.')
elif opcao==4:
    juros=preco*20/100
    parcelas=int(input('Quantas parcelas vão ser: '))
    print(f'Sua compra de R${preco:.2f} vai sair por R${preco+juros:.2f}.\nSerão {parcelas}x de R${(preco+juros)/parcelas:.2f}.')
else:
    print('Opção inválida! Tente novamente.')
