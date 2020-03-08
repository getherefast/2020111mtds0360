T = int(input('Quantidade de anos fumando: '))
Ci = int(input('Quantidade de cigarros por dia: '))
PCa = float(input('Preço da carteira de cigarros: '))
QtCa = Ci * T * 365 // 20
Qt = QtCa * PCa
print('Dinheiro gasto em cigarros em', T ,'anos:', Qt)