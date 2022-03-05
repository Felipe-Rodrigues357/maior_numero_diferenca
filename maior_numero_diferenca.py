n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
maior = 0
dif = 0
if n1 > n2:
    maior = n1
    dif = n1 - n2
elif n1 < n2:
    maior = n2
    dif = n2 - n1
else:
    print(f'Os números são iguais e sua diferença é 0')
print(f'O Maior número é {maior} e a diferença entre eles é {dif}')