import requests

want = 'RUB'
have = 'USD'
amount = '1'

api_url = f'https://api.api-ninjas.com/v1/convertcurrency?want={want}&have={have}&amount={amount}'
response = requests.get(api_url, headers={'X-Api-Key': '4SoIYFF/wUGebBUctahlCw==bcrvqJr8ipkudGiH'})
answer = response.json()
for key in answer.keys():
    if key == 'new_amount':
        answer_amount = answer.get(key)
        print(answer_amount)
