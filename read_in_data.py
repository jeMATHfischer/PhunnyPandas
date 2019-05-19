import requests
import pandas as pd
import io

url = 'https://api.production.mtomady.com/hack_hpi/claims?page=1'
payload = {}
headers = {'Authorization':'Token uVXKbFwkmKPEyJYeWagJUHtYEAoAWP4NtrzRtQFFvCHjVVT'}
r = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)

#df = pd.read_json(io.StringIO(response.decode('utf-8')))
#print(df.head())

j = r.json()
#print(j)
df = pd.DataFrame.from_dict(j['claims'])
print(df.head())
