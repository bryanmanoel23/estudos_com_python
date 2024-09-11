valorMedicamento = float(input('Informe o valor do medicamento que deseja calcular o reajuste: '))

if valorMedicamento <=  249.99:
   porcetagem = 20 * valorMedicamento / 100
   reajuste = porcetagem + valorMedicamento
   print('Valor do medicamento {} reais o reajuste do valor do medicamento foi {} reais'.format(reajuste, porcetagem))
   
if valorMedicamento >= 250.00 and valorMedicamento <= 289.99:
    porcetagem = 15 * valorMedicamento / 100
    reajuste = porcetagem + valorMedicamento
    print('Valor do medicamento {} reais o reajuste do valor do medicamento foi {} reais'.format(reajuste, porcetagem))

if valorMedicamento >= 290 and valorMedicamento <= 349.99:
    porcetagem = 10 * valorMedicamento / 100
    reajuste = porcetagem + valorMedicamento
    print('Valor do medicamento {} reais o reajuste do valor do medicamento foi {} reais'.format(reajuste, porcetagem))

if valorMedicamento >= 350:
    porcetagem = 5 * valorMedicamento / 100
    reajuste = porcetagem + valorMedicamento
    print('Valor do medicamento {} reais o reajuste do valor do medicamento foi {} reais'.format(reajuste, porcetagem))
