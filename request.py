import requests
from requests.exceptions import HTTPError

# response = requests.get('https://api.github.com')

# if response.status_code == 200:
#     print(str(response) + 'Success!')
# elif response.status_code == 404:
#     print(str(response )+ 'Not Found.')

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except  HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')
