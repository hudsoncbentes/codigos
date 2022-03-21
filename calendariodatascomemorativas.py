import requests
import json
import pandas as pd

calendar = []
for year in range(2012, 2019):
    link =  'https://api.calendario.com.br/?'
    link += 'json=true'
    link += '&ano=' + str(year)
    link += '&estado=PE'
    link += '&cidade=RECIFE'
    link += '&data'
    link += '&token=YnV2ZUBrdWxtZW8uY29tJmhhc2g9Nzg2MDA1NTg'
    
    data = requests.get(link)
    calendar.extend(json.loads(data.content))

df = pd.DataFrame(calendar)
df.to_csv('calendario.csv', sep=';', index=False)