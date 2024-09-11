nome = input('Informe seu nome: ')

idade = int(input('Informe sua idade: '))
            
sexo = input('Informe seu sexo: ')
            
nota = float(input('Informe a nota da prova: '))

faltas = int(input('Informe o número de faltas: '))

##Independente da nota que ele tiver, se suas faltas forem menores que 10 o aluno é aprovado 

if nota > 40 :
            
    print('Aprovado !')
            
if nota <= 40 and faltas < 10:

    print('Aprovado !')
else:
    print('Infelizmente você foi reprovado !')
