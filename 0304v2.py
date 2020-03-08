Qt = float(input('Quantidade a sacar: '))
Q50 = Qt // 50.0
Q10 = (Qt % 50.0) // 10.0
Q5 = ((Qt % 50.0) % 10.0) // 5.0
Q2 = (((Qt % 50.0) % 10.0) % 5.0)// 2.0
print('Quantidade respectiva de notas de 50.0, 10.0, 5.0 e 2.0 reais a ser retiradas: ', Q50, Q10, Q5, Q2)
