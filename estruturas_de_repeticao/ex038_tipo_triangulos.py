# Verificar se as retas formam um triangulo, se sim, qual?
print('Vamos analisar 3 retas? preciso saber a medida delas!')

# Pegar as medidas
pri_reta = input('Medida da primeira reta:').strip().split()
seg_reta = input('Medida da segunda reta:').strip().split()
ter_reta = input('Medida da terceira reta:').strip().split()

# Transformar as medidas para FLOAT
pri_reta = float(pri_reta[0])
seg_reta = float(seg_reta[0])
ter_reta = float(ter_reta[0])

# Saber qual é o MENOR:
if seg_reta < pri_reta and seg_reta < ter_reta:
    menor = seg_reta
elif ter_reta < pri_reta and ter_reta < seg_reta:
    menor = ter_reta
else:
    menor = pri_reta
# Saber quem é o MAIOR:
if seg_reta > pri_reta and seg_reta > ter_reta:
    maior = seg_reta # Maior é a reta 2
elif ter_reta > pri_reta and ter_reta > seg_reta:
    maior = ter_reta # Maior é a reta 3
else:
    maior = pri_reta
# Saber quem é o MEDIANO:
if seg_reta > menor and seg_reta < maior:
    media = seg_reta
elif ter_reta > menor and ter_reta < maior:
    media = ter_reta
else:
    media = pri_reta

# Verificar se FAZEM UM TRIANGULO:
if menor + media > maior:
    # Definir equilatero(=TUDO IGUAL=) e escaleno(!TUDO DIFERENTE=)
    equilatero = pri_reta == seg_reta and pri_reta == ter_reta
    escaleno = pri_reta != seg_reta and pri_reta != ter_reta and seg_reta != ter_reta
    # Verificar o TIPO de TRIANGULO:
    if equilatero == True: # Para um equilatero
        print('Este triangulo é um equilatero')
    elif escaleno == True: # Para um escaleno
        print('Este é um triangulo escaleno')
    else: # Para o isoceles
        print('Este é um triangulo isoceles')
else: # Caso não possa formar um triangulo
    print('NÃO forma um triangulo')
# Fim
print('__FIM__')