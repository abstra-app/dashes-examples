import pandas as pd
from abstra.dashes import redirect

csv_data = 'credit_analysis_data.csv'
df = pd.read_csv(csv_data)

def handle_table_action(event):
  payload = event.get('payload')
  action = payload.get('action')

  if action != 'Edit':
    return

  data = payload.get('data')
  
  redirect('/request', {"id": data.get('request_id')})