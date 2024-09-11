sexo = input('Informe seu sexo, Masculino digite (M) Feminino digite (F)')

if sexo == 'F' or sexo == 'f':
    
         print('Você não precisa se alistar')
         
if sexo == 'M'or sexo == 'm':

    idade = int(input('Informe sua idade')) 
    
    if idade < 18 :
        
        print('Dispensado')
    
    if idade >= 18 and idade <= 50:
        
        print('Você foi selecionado para ir para a Ucrânia')
    
    if idade >= 51:
        
        print('Você vai para Israel')
