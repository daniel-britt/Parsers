import requests
import json

url = 'http://api.plos.org/search?q=title:%22Drosophila%22%20and%20body:%22RNA%22&fl=id,abstract'
page = requests.get(url).json()

i = len(page["response"]["docs"])
x = 0
#print(page["response"]["docs"][0]['id'])
while i > x:
    print(page["response"]["docs"][x]["abstract"])
    print('\n')
    x = x + 1
