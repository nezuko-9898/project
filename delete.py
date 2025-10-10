# Delete method using   delete

import requests

url = "https://jsonplaceholder.typicode.com/posts"



response = requests.delete(url)

print('Response :',response.json())