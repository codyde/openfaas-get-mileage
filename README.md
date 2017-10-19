# OpenFaaS function for calling Google Map Distance API

* Platform - Written for use with the [OpenFaaS](https://github.com/openfaas/faas) function as a service platform, across all container schedulers (Docker Swarm/Kubernetes)
* Language - Written for Python3 

## Public Docker Hub Image 

* https://hub.docker.com/r/codydearkland/get-mileage/

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
{u'date': u'10/4', u'start': u'Roseville, Ca', u'end': u'Disneyland, Ca'}
{u'date': u'10/4', u'start': u'Roseville, Ca', u'end': u'Sacramento, Ca'}
{u'date': u'10/4', u'start': u'Sacramento Train Museum', u'end': u'BJs Brewery Roseville Ca'}
+------+-----------------------------------------+-----------------------------------------------+----------------+
| Date |              Starting Point             |                  Ending Point                 | Miles Traveled |
+------+-----------------------------------------+-----------------------------------------------+----------------+
| 10/4 |            Roseville, CA, USA           |   1313 Disneyland Dr, Anaheim, CA 92802, USA  |     429 mi     |
| 10/4 |            Roseville, CA, USA           |              Sacramento, CA, USA              |    18.8 mi     |
| 10/4 | 125 I Street, Sacramento, CA 95814, USA | 1200 Roseville Pkwy, Roseville, CA 95678, USA |    23.1 mi     |
+------+-----------------------------------------+-----------------------------------------------+----------------+
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