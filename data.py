#importa o metodo datatime da biblioteca local do python
from datetime import datetime

#Guar da data e hora atueal na variavel data
data = datetime.now()

#Formata para o padrão de gravação no banco de dados  
data_formatada = data.strftime('%Y-%m-%d %H:%M:%S')
 

#Imprime a data e hora no terminal
print("Data formatada:", data_formatada)
