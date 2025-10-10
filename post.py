import requests

# Create data using Post method

url = 'https://jsonplaceholder.typicode.com/posts'


new_data = {

    'title':'Hello',
    'body' :'Mr morning star',
    'userId': 1
}


response = requests.post(url,new_data)


print('Rsponse :',response.json())