import requests



class BaseR4:
    
    def __init__(self , base_url):
        self.base_url = base_url
    
    
    def create_data(self , resource):
        url = f'{self.base_url}/Observation'
        response = requests.post(url , json=resource)
        print(f'Created Successfully -- status code {response.status_code}')
        print(response.json())
    
    def get_all_data(self):
        url = f'{self.base_url}/Observation' 
        response = requests.get(url)
        print(response.json())
  
    
    def get_data(self, id):
        url = f'{self.base_url}/Observation/{id}'
        response = requests.get(url)
        print(response.status_code)
        print(response.json())
        
        
    def update_data(self , id , resource):
        url = f'{self.base_url}/Observation/{id}'
        response = requests.patch(url , json=resource)
        print(f'Updated Successfully -- status code {response.status_code}')
        print (response.json())
        
              
    def delete_data(self , id):
        url = f'{self.base_url}/Observation/{id}' 
        data_list = requests.get(self.base_url).json()
        response = requests.delete(url)
        print(f'Deleted Successfully -- status code {response.status_code}')
        print(data_list)
    

observation = BaseR4("http://hapi.fhir.org/baseR4") 

test_data = {
  "resourceType": "Observation",
  "id": "7367336",
  "meta": {
    "versionId": "1",
    "lastUpdated": "2023-01-25T14:27:16.793+00:00",
    "source": "#Jg8aq0KOu3syjJgi"
  },
  "status": "final",
  "code": {
    "coding": [ {
      "system": "http://loinc.org",
      "code": "8867-4",
      "display": "Heart rate"
    } ]
  },
  "subject": {
    "reference": "Patient/7304958"
  },
  "effectivePeriod": {
    "start": "2022-12-16T08:51:00.000+01:00",
    "end": "2022-12-16T08:51:00.000+01:00"
  },
  "valueQuantity": {
    "value": 59.0,
    "unit": "beats/min",
    "system": "http://unitsofmeasure.org",
    "code": "/min"
  }
}

# get_all = observation.get_all_data()

# get = observation.get_data(7515633)

# create_data = observation.create_data(test_data)

# update_data = observation.update_data(7367353 , test_data)

# delete_data = observation.delete_data(7367336)