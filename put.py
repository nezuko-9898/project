#Edit using put method

import requests


url = 'https://jsonplaceholder.typicode.com/posts/1'


update_data = {

    'title ':'Hello',
    'body'   : 'hello morning',
    'userid' :1
}


response = requests.put(url,update_data)

print('Response :',response.json() )
