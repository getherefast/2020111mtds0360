T = int(input('Quantidade de anos fumando: '))
Ci = int(input('Quantidade de cigarros por dia: '))
PCa = float(input('Preço da carteira de cigarros: '))
QtCi = Ci * T * 365
QtCa = QtCi // 20
Y = QtCi % 20
if Y > 0 :
    X = PCa
else :
    X = 0
Qt = QtCa * PCa + X
print('Dinheiro gasto em cigarros em', T ,'anos:', Qt)
