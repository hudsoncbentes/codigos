# CALENDARIO ============================================================
from datetime import date, timedelta
import json
#========================================================================
data_inicio = date(2021, 1, 1)
data_fim = date(2021, 2, 3)

delta = data_fim - data_inicio

lista_datas = []
for i in range(delta.days + 1):
    day = data_inicio + timedelta(days=i)
    lista_datas.append(day.strftime('%d/%m/%y'))
    
calendario = lista_datas