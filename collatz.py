import matplotlib.pyplot as plt
import pandas as pd
import csv

iniciais=[]
saidas=[]
for b1 in range(1,11):
  valor_apl=b1
  valor_apl=int(valor_apl)
  valor_ger=0
  saidas.append(valor_apl)
  valor=[]
  valorb=[]

  while valor_apl !=1:
    if valor_ger==0:
      pass
      #valor.append(valor_apl)
      #valor_ger+=1
      #print("valores: ")
    if valor_apl%2==0:
      #print (str(valor_apl))
      valor_apl=(valor_apl/2)
      valor.append(valor_apl)
    else:
      #print (str(valor_apl))
      valor_apl=valor_apl*3+1
      valor.append(valor_apl)
    valor_ger+=1
    
  #print("1.0")
  #print ("Chegou em 1 após "+str(valor_ger)+" gerações")
  for x in range(valor_ger):
    valorb.append(x)
  #plt.scatter(valorb,valor)
  
  iniciais.append(valor_ger)
print(iniciais)
f = open('dados.csv', 'w')
writer = csv.writer(f)
writer.writerow(saidas)
writer.writerow(iniciais)
#writer.writerow(iniciais)

f.close()
