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
