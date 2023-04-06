from abstra.dashes import get_query_params
import pandas as pd

request_status = ''
comments = ''
esg_score = ''
legal_assessment = ''
internal_assessment = ''

params = get_query_params()
request_id = params.get('id', 1)

csv_data = 'credit_analysis_data.csv'
df = pd.read_csv(csv_data)
row = df.loc[df['request_id'] == request_id]

print(row)

# extract the values from the row
request_status = row['request_status'].values[0]
comments = row['comments'].values[0]
esg_score = row['ESG_score'].values[0]
legal_assessment = row['legal_assessment'].values[0]
internal_assessment = row['internal_assessment'].values[0]

# # extract the values from the row into a dictionary
# request = row.to_dict('records')[0]

# print(request)



# {'value': None, 'payload': {'data': {'index': 1, 'prospect_id': 3931, 'prospect_name': 'B Company', 'created_date': '02/01/2023', 'legal_assessment': 'Cleared', 'ESG_score': 'Excellent', 'internal_assessment': 'Low risk', 'request_status': 'Approved', 'comments': None}, 'index': 1}}



# def update_request():
