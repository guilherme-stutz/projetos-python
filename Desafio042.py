a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceiro segmento: '))
if a+b>c and a+c>b and b+c>a:
    print('Os segmentos PODEM formar um triângulo.')
    if a==b==c:
        print('Todos os lados são iguais, portanto EQUILÁTERO.')
    elif a==b or a==c or b==c:
        print('Tem dois lados iguais, portanto ISÓSCELES.')
    elif a!=b and a!=c  and b!=c:
        print('Todos os lados são diferentes, portanto ESCALENO.')
else:
    print('Os segmentos NÃO PODEM formar um triângulo.')
