from abstra.dashes import get_query_params, redirect
from datetime import datetime
import pandas as pd
import math

request_status = ''
comments = ''
esg_score = ''
legal_assessment = ''
internal_assessment = ''

params = get_query_params()
request_id = params.get('id', 1)

csv_data = 'credit_analysis_data.csv'
df = pd.read_csv(csv_data, na_filter=False, keep_default_na=False)
row = df.loc[df['request_id'] == request_id]

# Extract the values from the pandas row
request_status = row['request_status'].values[0]
esg_score = row['ESG_score'].values[0]
legal_assessment = row['legal_assessment'].values[0]
internal_assessment = row['internal_assessment'].values[0]
comments = row['comments'].values[0]
prospect_name = row['prospect_name'].values[0]
created_date = datetime.fromtimestamp(row['created_at'].values[0]).strftime('%Y/%m/%d %H:%M:%S')
updated_at = datetime.fromtimestamp(row['updated_at'].values[0]).strftime('%Y/%m/%d %H:%M:%S')

def update_request():
    # update csv row with new values
    df.loc[df['request_id'] == request_id, 'request_status'] = request_status
    df.loc[df['request_id'] == request_id, 'ESG_score'] = esg_score
    df.loc[df['request_id'] == request_id, 'legal_assessment'] = legal_assessment
    df.loc[df['request_id'] == request_id, 'internal_assessment'] = internal_assessment
    df.loc[df['request_id'] == request_id, 'comments'] = comments
    df.loc[df['request_id'] == request_id, 'updated_at'] = math.floor(datetime.now().timestamp())
    df.to_csv(csv_data, index=False)
    redirect('/requests')

