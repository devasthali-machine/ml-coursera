
- we will explore data corresponding to taxi rides in New York City to build a ML model in support of a fare-estimation tool. 
- The idea is to suggest a likely fare to taxi riders so that they are not surprised, and so that they can protest if the charge is much higher than expected.

- dataset is available at https://bigquery.cloud.google.com/table/nyc-tlc:yellow.trips?tab=preview, 

```json
  {
    "vendor_id": "CMT",
    "pickup_datetime": "2015-02-07 00:05:40 UTC",
    "dropoff_datetime": "2015-02-07 00:40:35 UTC",
    "pickup_longitude": "-73.9864730834961",
    "pickup_latitude": "40.745235443115234",
    "dropoff_longitude": "-74.125823974609375",
    "dropoff_latitude": "40.649356842041016",
    "rate_code": "5",
    "passenger_count": "1",
    "trip_distance": "12.8",
    "payment_type": "CRD",
    "fare_amount": "0.0",
    "extra": "0.0",
    "mta_tax": "0.0",
    "imp_surcharge": "0.3",
    "tip_amount": "0.0",
    "tolls_amount": "75.45",
    "total_amount": "75.75",
    "store_and_fwd_flag": "N"
  },
```

```bash
datalab create creating-ml-dataset --zone us-west1-a

%bash
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
rm -rf training-data-analyst/.git
```

go to https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive/02_generalization/create_datasets.ipynb

```python
import google.datalab.bigquery as bq
import seaborn as sns
import pandas as pd
import numpy as np
import shutil

# Extract sample data from BigQuery
rawdata = """
SELECT
  pickup_datetime,
  pickup_longitude, pickup_latitude, 
  dropoff_longitude, dropoff_latitude,
  passenger_count,
  trip_distance,
  tolls_amount,
  fare_amount,
  total_amount
FROM
  `nyc-tlc.yellow.trips`
WHERE
  MOD(ABS(FARM_FINGERPRINT(CAST(pickup_datetime AS STRING))),EVERY_N) = 1
"""

query = rawdata.replace("EVERY_N", "100000")
print query
trips = bq.Query(query).execute().result().to_dataframe()
print "Total dataset is {} taxi rides".format(len(trips))
trips[:10]

# Let's explore this dataset and clean it up as necessary.
ax = sns.regplot(x = "trip_distance", y = "fare_amount", ci = None, truncate = True, data = trips)

# Let's examine whether the toll amount is captured in the total amount.
tollrides = trips[trips['tolls_amount'] > 0]
tollrides[tollrides['pickup_datetime'] == '2014-05-20 23:09:00']

# Let's also look at the distribution of values within the columns.
trips.describe()

# Finally, let's actually look at the start and end of a few of the trips.

def showrides(df, numlines):
  import matplotlib.pyplot as plt
  lats = []
  lons = []
  goodrows = df[df['pickup_longitude'] < -70]
  for iter, row in goodrows[:numlines].iterrows():
    lons.append(row['pickup_longitude'])
    lons.append(row['dropoff_longitude'])
    lons.append(None)
    lats.append(row['pickup_latitude'])
    lats.append(row['dropoff_latitude'])
    lats.append(None)

  sns.set_style("darkgrid")
  plt.plot(lons, lats)

showrides(trips, 10)
showrides(tollrides, 10)

# Let's change the BigQuery query appropriately. In production, we'll have to carry out the same preprocessing on the real-time input data.
```
