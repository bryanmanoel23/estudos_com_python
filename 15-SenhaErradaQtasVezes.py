password = input('Informe sua senha: ')

count = 0
while password != 'Senh@24':
    
    print('Senha incorreta, tente novamente !')
    
    password = input('Informe sua senha: ')
    
    count += 1
print('Voce errou {} vezes a senha antes de digitar ela corretamente'.format(count))
