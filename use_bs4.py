import requests
from bs4 import BeautifulSoup

url = "https://detik.com"
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success ! Response = {response.status_code}')
        # print(f'Content = {response.text}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'Hasil pemaggilan {url}')
        print(f'Titel: {soup.title.string}')
    else:
        print('Ups, ada error ni')
except Exception as e:
    print(f'There is an error {e}')
print('Program ended')
