import requests, urllib

r = requests.post('http://10.0.0.5:8000',data = {'ddta':'sneha', 'dta':'here'})


print(r.text)
