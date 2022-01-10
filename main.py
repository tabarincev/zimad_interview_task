import pandas as pd
import wget
import os


url = 'https://testiws.ximad.com/export/events.csv.gz'
filename = url.split('/')[-1]

if not os.path.exists(filename):
    wget.download(url, './%s' % (filename))

df = pd.read_csv(filename)

# Отбираем строки по условию event_name == launch или purchase
event_df = df['event_name']
launch_purchase = df.loc[(event_df == 'launch') | (event_df == 'purchase')]

# Преобразуем к datetime объекту колонку event_time
launch_purchase['event_time'] = pd.to_datetime(launch_purchase['event_time'])

# Группируем данные по дням
groupby_value = launch_purchase['event_time'].dt.date
day_sum = launch_purchase.groupby(groupby_value)['event_value'].agg(['sum', 
                                                                     'count'])

# Вычисляем метрику ARPDAU
day_sum['ARPDAU'] = day_sum['sum'] / day_sum['count']

print(day_sum)