import requests


url = "https://jsonplaceholder.typicode.com/posts"




new_data ={
    'name':'morning star',
    'work':'it man'
}


response = requests.put(f'{url}/1',new_data)

print("print response:" , response.json())