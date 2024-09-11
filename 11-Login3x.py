email = input('Informe seu email:')
password = input('Informe sua senha:')

count = 1

tentativas = 3

while count < tentativas:

    if password == '123456':

        print('Parabéns senha certa')
    
        count = 3
    
    else:
        print('Senha incorreta, restam 2 tentativas')
        
        password = input('Informe sua senha:')

        count = count + 1
    
        if password == '123456':

            print('Parabéns senha certa')

            count = 3

        else:

            print('Senha incorreta, restam 1 tentativas')
        
            password = input('Informe sua senha:')

            count = count + 1
        
            if password == '123456':
    
                print('Parabéns senha certa')

                count = 3
            
            else:
                print('Você excedeu o número de tentativas, tente novamente mais tarde')

                count = count + 1
