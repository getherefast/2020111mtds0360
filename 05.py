hn = int(input('Horario Normal de Trabalho: '))
hx = int(input('Horario Extra de Trabalho: '))
Hn = 10.0*hn
Hx = 15.0*hx
St = Hn + Hx
Sl = St*0.10
print ('Salario bruto', St,'Salario liquido', Sl)