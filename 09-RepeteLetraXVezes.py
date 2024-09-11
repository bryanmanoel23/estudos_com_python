loop = int(input('Informe o número de vezes que deseja que o valor informado se repita'))
informacao = input('Informe o valor que vai se repetir {} vezes'.format(loop))

count = 1

while count <= loop:
    print(count, informacao)

    count = count + 1
