import requests

apiUrl = 'https://webexapis.com/v1/rooms'
access_token = 'NTA1ZmMzNTItODlkZi00M2E5LThiZmMtOWQ5MzZiNzI1NDczMTg2YjBlYzQtMjgx_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'

httpHeaders = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }
queryParams = { 'sortBy': 'lastactivity', 'max': '2' }

response = requests.get( url = apiUrl, headers = httpHeaders, params = queryParams )

print( response.status_code )
print( response.text )

