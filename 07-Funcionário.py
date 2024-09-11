salario = float(input('Informe o valor do seu salário: '))

inss = 11 * salario /100

ir = 15 * salario / 100

if salario <= 2640:
    ir = 0
    
    salarioliquido = salario - inss

    print('Valor do salário informado no sistema: {} ,valor do INSS {} ,salários menores que 2640,00 reais não são cobrados imposto de renda em 2024 ! ,valor salário líquido {}  '.format(salario, inss,salarioliquido))
    
else:

    salarioliquido = salario - inss - ir


    print('Valor do salário informado no sistema: {} ,valor do INSS {} ,valor do IR {} ,valor salário líquido {}  '.format(salario, inss,ir,salarioliquido))
