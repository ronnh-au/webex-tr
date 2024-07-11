import requests

apiUrl = 'https://webexapis.com/v1/messages'
access_token = 'NTA1ZmMzNTItODlkZi00M2E5LThiZmMtOWQ5MzZiNzI1NDczMTg2YjBlYzQtMjgx_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
httpHeaders = { 'Content-type': 'application/json', 'Authorization': 'Bearer ' + access_token }

body = { 'toPersonEmail': 'gifbot@webex.bot', 'text': 'Hello' }

response = requests.post( url = apiUrl, json = body, headers = httpHeaders )

print( response.status_code )
print( response.text )

messages = [
    '**Warning!!!**',
    '_Warning!!!_',
    '[Danger, Will Robinson!!!](https://en.wikipedia.org/wiki/Lost_in_Space#Catchphrases)'
    ]

for message in messages:

    body = { 'toPersonEmail': 'gifbot@webex.bot', 'markdown': message }
    response = requests.post( url = apiUrl, json = body, headers = httpHeaders )

    print( response.status_code )
    print( response.text )
