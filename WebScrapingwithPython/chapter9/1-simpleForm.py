import requests

params = {'firstname': 'Chi', 'lastname': 'Feng'}
r = requests.post('http://pythonscraping.com/files/processing.php', data=params)
print(r.text)