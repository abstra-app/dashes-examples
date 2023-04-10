import pandas as pd
from abstra.dashes import redirect, get_user

csv_data = 'credit_analysis_data.csv'
df = pd.read_csv(csv_data)

# convert columns created_at and updated_at to formated date as sstring
df['created_at'] = pd.to_datetime(df['created_at'], unit='s').dt.strftime('%Y/%m/%d %H:%M:%S')
df['updated_at'] = pd.to_datetime(df['updated_at'], unit='s').dt.strftime('%Y/%m/%d %H:%M:%S')


def handle_table_action(event):
  payload = event.get('payload')
  action = payload.get('action')

  if action != 'Edit':
    return

  data = payload.get('data')
  
  redirect('/request', {"id": data.get('request_id')})