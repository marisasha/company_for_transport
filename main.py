import pandas as pd
import json

df = pd.read_excel('prices.xlsx')

data = df.to_dict(orient='list')

json_data = json.dumps(data, ensure_ascii=False)


data_dict = json.loads(json_data)
transplate_name = data_dict["Наименование"]
transplate_price = data_dict["Цена"]

df.iloc[:, 0] = ''
df.iloc[:, 1] = ''

df.to_excel('prices.xlsx', index=False)