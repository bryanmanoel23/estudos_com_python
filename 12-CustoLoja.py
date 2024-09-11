produto = int(input('Informe quantas unidades do produto você deseja adquirir: '))

valorProduto = float(input('Informe o custo por unidade: '))

call = float(input('A ligação durou quantos minutos ? Sabendo que cada minuto da ligação custa 0.1388 centavos por minuto: '))

taxaEntrega = float(input('Informe o valor da taxa de entrega: '))

percurso = float(input('Informe a distância que vai percorrer para chegar até a mercadoria: '))

valorAdcional = float(input('Existe algum valor adicional ? informe: '))

valorGasolina = float(input('Qual valor do litro da gasolina ? '))

kmPorLitro = float(input('Quantos km por litro o carro ao qual vai fazer o percurso anda: '))

valorProduto = produto * valorProduto

pix = valorProduto + call + taxaEntrega

totalGasolina = (percurso * 2) / kmPorLitro * valorGasolina

totaldispesas = pix + totalGasolina + valorAdcional

##o fator divisor foi (5) levando em consideração o valor de cada blusa, tempo da ligação, taxa de entrega, total gasto da gasolina, e o valor pago ao motorista

mediaBlusas = valorProduto + totaldispesas / 5

totalProduto = mediaBlusas / produto

precoVenda = totalProduto * 2

print('O valor do pix foi de {} reais'.format(pix))

print('O valor de cada blusa foi de {} reais'.format(totalProduto))

print('Para ganhar o dobro em cada unidade devem ser vendidas por {} reais'.format(precoVenda))


