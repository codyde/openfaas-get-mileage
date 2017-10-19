# OpenFaaS function for calling Google Map Distance API

* Platform - Written for use with the [OpenFaaS](https://github.com/openfaas/faas) function as a service platform, across all container schedulers (Docker Swarm/Kubernetes)
* Language - Written for Python3 

## Example Output

```bash
curl http://openfaas.url.com/function/get-mileage -d '[{
        "date": "10/4",
        "start": "Roseville, Ca",
        "end": "Disneyland, Ca"
    },{
        "date": "10/4",
        "start": "Roseville, Ca",
        "end": "Sacramento, Ca"
    },{
        "date": "10/4",
        "start": "Sacramento Train Museum",
        "end": "BJs Brewery Roseville Ca"
    }]'
{u'date': u'10/4', u'start': u'641 Oakborough Ave Roseville Ca', u'end': u'California natural resources agency'}
{u'date': u'10/4', u'start': u'California natural resources agency', u'end': u'641 Oakborough Ave Roseville Ca'}
{u'date': u'10/5', u'start': u'641 Oakborough Ave Roseville ca', u'end': u'1416 ninth street sacramento ca'}
+------+----------------------------------------------+----------------------------------------------+----------------+
| Date |                Starting Point                |                 Ending Point                 | Miles Traveled |
+------+----------------------------------------------+----------------------------------------------+----------------+
| 10/4 | 641 Oakborough Ave, Roseville, CA 95747, USA | 1416 9th St  1311, Sacramento, CA 95814, USA |    19.5 mi     |
| 10/4 | 1416 9th St  1311, Sacramento, CA 95814, USA | 641 Oakborough Ave, Roseville, CA 95747, USA |    22.9 mi     |
| 10/5 | 641 Oakborough Ave, Roseville, CA 95747, USA |    1416 9th St, Sacramento, CA 95814, USA    |    19.5 mi     |
+------+----------------------------------------------+----------------------------------------------+----------------+
```

## Requirements: 
* Google Maps Distance Matrix API Key (https://developers.google.com/maps/documentation/distance-matrix/intro) 
* Edit stack-example.yml to include API key in environment variables (or create an environment.yml file and use that) 
* Edit stack-example.yml to include your Docker Hub repository 
* Push to OpenFaaS

The expected format for travel details is follows... (python list is expected) 

```python
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
```

## Features 

* Utilizes Google API's to make calls. Able to resolve text entries into logical addresses. 
* Returns date, source address, detination address, and mileage. 

## Modifications 

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