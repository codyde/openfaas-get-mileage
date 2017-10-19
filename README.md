## OpenFaaS function for calling Google Map Distance API

* Language - Written for Python3 

# Requirements: 
* Google Maps Distance Matrix API Key (https://developers.google.com/maps/documentation/distance-matrix/intro) 
* Edit stack-example.yml to include API key in environment variables (or create an environment.yml file and use that) 
* Edit stack-example.yml to include your Docker Hub repository 
* Push to OpenFaaS

The expected format for travel details is follows... (python list is expected) 

[
    {
        "date": "10/4",
        "start": "Roseville, Ca",
        "end": "Disneyland, Ca"
    },
    {
        "date": "10/4",
        "start": "Roseville, Ca",
        "end": "Sacramento, Ca"
    },
    {
        "date": "10/4",
        "start": "Sacramento Train Museum",
        "end": "BJs Brewery Roseville Ca"
    }
]

# Features 

* Utilizes Google API's to make calls. Able to resolve text entries into logical addresses. 
* Returns date, source address, detination address, and mileage. 

# Modifications 

Review https://developers.google.com/maps/documentation/distance-matrix/intro for details 

Switch from Miles to Kilometers by modifying the following block within handler.py from 

```python
payload = {
            'origins' : '|'.join(origins),
            'destinations' : '|'.join(destinations), 
            'mode' : 'driving',
            'units': 'imperial',
            'api_key' : api_key
        }
```
to 

```python
payload = {
            'origins' : '|'.join(origins),
            'destinations' : '|'.join(destinations), 
            'mode' : 'driving',
            'units': 'metric',
            'api_key' : api_key
        }
```