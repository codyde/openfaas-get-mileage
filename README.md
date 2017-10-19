## OpenFaaS function for calling Google Map Distance API


# Requirements: 
You'll need to get a Google Maps Distance Matrix API Key from here https://developers.google.com/maps/documentation/distance-matrix/intro and include that in your environment variables within the stack-example.yml file 

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

```json
payload = {
            'origins' : '|'.join(origins),
            'destinations' : '|'.join(destinations), 
            'mode' : 'driving',
            'units': 'imperial',
            'api_key' : api_key
        }
```
to 

```json
payload = {
            'origins' : '|'.join(origins),
            'destinations' : '|'.join(destinations), 
            'mode' : 'driving',
            'units': 'metric',
            'api_key' : api_key
        }
```