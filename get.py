import requests

#Read data using GET Method

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(f'{url}/1')

print("Response",response.json())