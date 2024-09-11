peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

alturaQuadrada = altura * altura
imc = peso / alturaQuadrada

if imc <= 16.9:
    print('Muito abaixo do peso')
    
if imc >= 17 and imc <= 18.4:
    print('Abaixo do peso')

if imc >= 18.5 and imc <=24.9:
    print('Peso normal')

if imc >= 25 and imc <=29.9:
    print('Acima do peso')

if imc >= 30 and imc <= 34.9:
    print('Obesidade grau I')

if imc >= 35 and imc <= 40:
    print('Obesidade grau II')

if imc >= 40:
    print('Obesidade grau III')
