import requests
from requests.exceptions import HTTPError


##exit codes
response = requests.get('https://api.github.com')

if response.status_code == 200:
    print(str(response) + 'Success!')
elif response.status_code == 404:
    print(str(response )+ 'Not Found.')

# j = 8
# l = 12
# k = 10

# for i in (j,  k, l):
#     print(i)

# person = {'name': 'Eric', 'age': 74, 'fuck': 'this', 'what':'is what?'}
# print("Hello, {name}. You are {age}. fuck {fuck}. This {what}".format(**person))

##requesting through loop with exception error formating
for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response1 = requests.get(url)
        response1.raise_for_status()
        print(response1.headers)
        print(response1.headers['Content-Type'])
        # print(response1.content)
        # print(response1.text)
    #     print(response1.json())
    except  HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')


## custom requests, read documentation
response2 = requests.get(
    'https://api.github.com/search/repositories',
    params={'q':'requests+language:python'},
    headers={'Accept':'application/vnd.github.v3.text-match+json'},
)


##formating requests API data because not all API use json formating
json_response = response2.json()
repository = json_response['items'][0]
# print(repository)
print(f'Repository name:{repository["name"]}')
print(f'Repository description:{repository["description"]}')
print(f"Text matches:{repository['text_matches']}")

response3 = requests.delete('https://httpbin.org/delete')
json_response = response3.json()
# print(json_response)
print(json_response['args'])


###parsing API with requests method json=, data= 
response4 = requests.post('https://httpbin.org/post', json= {'key':'value'})
json_response = response4.json()
print(json_response)
json_response['data']

print(json_response['headers']['Content-Type'])


###API authentication 
from getpass import getpass
import requests
requests.get('https://api.github.com/user', auth=('Tony363', getpass()))

from requests.auth import HTTPBasicAuth
from getpass import getpass
requests.get(
    'http://api.github.com/user',
    auth=HTTPBasicAuth('username', getpass())
)