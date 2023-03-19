import pprint

payload = {
   'api_key': 'w8rwT4fzEBUrOgQqJOJyfVRFocWce5oBnoE5NVNI',
   'start_date': '2022-03-09',
   'end_date': '2022-03-11'
}

endpoint = 'https://api.nasa.gov/planetary/apod'

try:
   r = requests.get(endpoint, params=payload)
   data = r.json()
   pprint(data)
except:
   print('please try again')
