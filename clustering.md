- form of ML that identifies groups based on features of items

You want to train a model where there is no previously known cluster value (or label) from which to train the model. 
Which type of machine learning would you use?

EDA
----

https://github.com/MicrosoftDocs/ml-basics/blob/master/data/penguins.csv

```
CulmenLength,CulmenDepth,FlipperLength,BodyMass,Species
39.1,18.7,181,3750,0
39.5,17.4,186,3800,0
40.3,18,195,3250,0
,,,,0
36.7,19.3,193,3450,0
39.3,20.6,190,3650,0
```

![](azure-clustering-ml-normalize-data.png)

Train model
--------------

- The model we're training will use the features to group the data into clusters, 
so we need to train the model using a clustering algorithm: K-Means Clustering 
- K-Means algorithm groups items into the number of clusters you specify - a value referred to as K.
K = 3 in this example
- After using 70% of the data to train the clustering model, you can use the remaining 30% to test it by using the model to assign the data to clusters

![](azure-clustering-ml-train-data.png)

Evaluate trained model
--

The performance metrics in each row are: 
- Average Distance to Other Center
- Average Distance to Cluster Center
- Number of Points
- Maximal Distance to Cluster Center

inference a trained model
-------------------------

![](azure-clustering-ml-inference-data.png)

```
CulmenLength,CulmenDepth,FlipperLength,BodyMass
39.1,18.7,181,3750
49.1,14.8,220,5150
46.6,17.8,193,3800
```

deploy an inferenced model
---------------------------

```python
endpoint = 'YOUR_ENDPOINT' #Replace with your endpoint
key = 'YOUR_KEY' #Replace with your key

import urllib.request
import json
import os

data = {
    "Inputs": {
        "WebServiceInput0":
        [
            {
                    'CulmenLength': 49.1,
                    'CulmenDepth': 4.8,
                    'FlipperLength': 1220,
                    'BodyMass': 5150,
            },
        ],
    },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ key)}

req = urllib.request.Request(endpoint, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    json_result = json.loads(result)
    output = json_result["Results"]["WebServiceOutput0"][0]
    print('Cluster: {}'.format(output["Assignments"]))

except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers to help debug
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
```

