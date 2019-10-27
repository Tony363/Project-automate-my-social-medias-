import requests
from requests.exceptions import HTTPError

# response = requests.get('https://api.github.com')

# if response.status_code == 200:
#     print(str(response) + 'Success!')
# elif response.status_code == 404:
#     print(str(response )+ 'Not Found.')

j = 8
l = 12
k = 10

for i in (j,  k, l):
    print(i)

# for url in ['https://api.github.com', 'https://api.github.com/invalid']:
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         print(response.content)
#         print(response.json())
#     except  HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')
#     except Exception as err:
#         print(f'Other error occurred: {err}')
#     else:
#         print('Success!')
