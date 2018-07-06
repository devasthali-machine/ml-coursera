What model would you typically want to call on first for duration-of-pregnancy/weight gain in pounds" dataset?
- Linear Regression

You've just got 80% of the data using the below query for training. 
How could you modify the query below to get a new 10% dataset for validation?

```
#standardSQL
SELECT
 date,
 airline,
 departure_airport,
 departure_schedule,
 arrival_airport,
 arrival_delay
FROM
`bigquery-samples.airline_ontime_data.flights`

WHERE
 MOD(ABS(FARM_FINGERPRINT(date)),10) = 8 or MOD(ABS(FARM_FINGERPRINT(date)),10) = 9
```

https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive/02_generalization/repeatable_splitting.ipynb

Repeatability is important in machine learning. 
If you do the same thing now and 5 minutes from now and get different answers, then it makes experimentation is difficult. 

In other words, you will find it difficult to gauge whether a change you made has resulted in an improvement or not.

```
datalab create repeatable-splitting-vm --zone us-west1-a

%bash
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
rm -rf training-data-analyst/.git
```

```python
import google.datalab.bigquery as bq

# We want to predict the arrival delay of an airline based on the departure delay. 
# For simplicity, we'll do this model only for flights between Denver and Los Angeles.
# Naive random split (not repeatable)

compute_alpha = """
#standardSQL
SELECT 
   SAFE_DIVIDE(SUM(arrival_delay * departure_delay), SUM(departure_delay * departure_delay)) AS alpha
FROM
(
   SELECT RAND() AS splitfield,
   arrival_delay,
   departure_delay
FROM
  `bigquery-samples.airline_ontime_data.flights`
WHERE
  departure_airport = 'DEN' AND arrival_airport = 'LAX'
)
WHERE
  splitfield < 0.8
"""

results = bq.Query(compute_alpha).execute().result().to_dataframe()
alpha = results['alpha'][0]
print alpha

#0.975946622849491

# What is wrong with calculating RMSE on the training and test data as follows?

compute_rmse = """
#standardSQL
SELECT
  dataset,
  SQRT(AVG((arrival_delay - ALPHA * departure_delay)*(arrival_delay - ALPHA * departure_delay))) AS rmse,
  COUNT(arrival_delay) AS num_flights
FROM (
  SELECT
    IF (RAND() < 0.8, 'train', 'eval') AS dataset,
    arrival_delay,
    departure_delay
  FROM
    `bigquery-samples.airline_ontime_data.flights`
  WHERE
    departure_airport = 'DEN'
    AND arrival_airport = 'LAX' )
GROUP BY
  dataset
"""
bq.Query(compute_rmse.replace('ALPHA', str(alpha))).execute().result()

# How do we correctly train and evaluate?
# Here's the right way to compute the RMSE using the actual training and held-out (evaluation) data. Note how much harder this feels.
# Although the calculations are now correct, the experiment is still not repeatable.

# Try running it several times; do you get the same answer?

train_and_eval_rand = """
#standardSQL
WITH
  alldata AS (
  SELECT
    IF (RAND() < 0.8,
      'train',
      'eval') AS dataset,
    arrival_delay,
    departure_delay
  FROM
    `bigquery-samples.airline_ontime_data.flights`
  WHERE
    departure_airport = 'DEN'
    AND arrival_airport = 'LAX' ),
  training AS (
  SELECT
    SAFE_DIVIDE( SUM(arrival_delay * departure_delay) , SUM(departure_delay * departure_delay)) AS alpha
  FROM
    alldata
  WHERE
    dataset = 'train' )
SELECT
  MAX(alpha) AS alpha,
  dataset,
  SQRT(AVG((arrival_delay - alpha * departure_delay)*(arrival_delay - alpha * departure_delay))) AS rmse,
  COUNT(arrival_delay) AS num_flights
FROM
  alldata,
  training
GROUP BY
  dataset
"""

bq.Query(train_and_eval_rand).execute().result()

# Using HASH of date to split the data

compute_alpha = """
#standardSQL
SELECT 
   SAFE_DIVIDE(SUM(arrival_delay * departure_delay), SUM(departure_delay * departure_delay)) AS alpha
FROM
  `bigquery-samples.airline_ontime_data.flights`
WHERE
  departure_airport = 'DEN' AND arrival_airport = 'LAX'
  AND MOD(ABS(FARM_FINGERPRINT(date)), 10) < 8
"""
results = bq.Query(compute_alpha).execute().result().to_dataframe()
alpha = results['alpha'][0]
print alpha

# 0.9758039143620403

compute_rmse = """
#standardSQL
SELECT
  IF(MOD(ABS(FARM_FINGERPRINT(date)), 10) < 8, 'train', 'eval') AS dataset,
  SQRT(AVG((arrival_delay - ALPHA * departure_delay)*(arrival_delay - ALPHA * departure_delay))) AS rmse,
  COUNT(arrival_delay) AS num_flights
FROM
    `bigquery-samples.airline_ontime_data.flights`
WHERE
    departure_airport = 'DEN'
    AND arrival_airport = 'LAX'
GROUP BY
  dataset
"""
print bq.Query(compute_rmse.replace('ALPHA', str(alpha))).execute().result().to_dataframe().head()

#  dataset       rmse  num_flights
#0    eval  12.764685        15671
#1   train  13.160712        64018
```
