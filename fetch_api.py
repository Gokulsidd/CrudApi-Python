import requests


url = 'http://hapi.fhir.org/baseR4/Observation?_format=json&_pretty=true'
response = requests.get(url)
data = response.json()
file =open('listdata.json' , 'w')
file.write(data)
