- predictive model to predict unknown values
- time consuming and resource intensive
- bicycle rental. features(x)= weather, label(y) = number of rentals => regression
- x = sugar levels, y = diabitic/non-diabitic    => classification
- both are examples of "supervised learning" with historic data

- if there is dataset of features, but no known labels. For example, customers visiting webpagesi(features).
group items into clusters of segments/groups.
This is known as unsupervised learning.

- create Azure resource at: https://portal.azure.com/
- once created go to https://ml.azure.com/ and select previously created workspace

EDA = Exploration and Data Analysis
----

- bicycle rental data: https://aka.ms/bike-rentals. Data is taken from https://www.capitalbikeshare.com/system-data
- create dataset in Azure ml: https://ml.azure.com/

Train a model
--------------

Azure provides Automated ML which supports the supervised learning 
1) classification
2) regression
3) regression with time-series element (aka Time series forecasting): to predict numeric values at a future point in time


- create Automated ML experiment with 
- Predicted vs. True: a diagonal trend in which the predicted value correlates closely to the true value
- Residual Histogram shows the frequency of residual value ranges. Residuals represent variance between predicted and true values that can't be explained by the model - in other words, errors

Deploy a Model as a Service(MAaS)
---------------------------------

- click on the run models
- deploy as web service

```bash
curl -H "content-type: application/json" "http://572e15eb-df29-4f21-805d-7ab38d2d9e0f.eastus2.azurecontainer.io/score" -d '{
  "data": [
    {
      "day": 12,
      "mnth": 1,
      "year": 2011,
      "season": 1,
      "holiday": 0,
      "weekday": 6,
      "workingday": 0,
      "weathersit": 2,
      "temp": 0.344167,
      "atemp": 0.363625,
      "hum": 0.805833,
      "windspeed": 0.160446
    }
  ]
}'
"{\"result\": [366.8014393071335]}"
```

```
x_feature_data = [
    [1,1,2022,1,0,6,0,2,0.344167,0.363625,0.805833,0.160446], 
    [2,1,2022,1,0,0,0,2,0.363478,0.353739,0.696087,0.248539], 
    [3,1,2022,1,0,1,1,1,0.196364,0.189405,0.437273,0.248309], 
    [4,1,2022,1,0,2,1,1,0.2,0.212122,0.590435,0.160296], 
    [5,1,2022,1,0,3,1,1,0.226957,0.22927,0.436957,0.1869]] 

#Convert the array to JSON format 
input_json = json.dumps({"data": x_feature_data})  

#Set the content type and authentication for the request 
headers = {"Content-Type":"application/json", 
        "Authorization":"Bearer " + key} 

#Send the request 
response = requests.post(endpoint, input_json, headers=headers) 
```

```
Predictions:
 Day: 1. Predicted rentals: 511
 Day: 2. Predicted rentals: 394
 Day: 3. Predicted rentals: 151
 Day: 4. Predicted rentals: 191
 Day: 5. Predicted rentals: 131
```


- Machine learning is a technique that uses statistics to create a model that can predict unknown values. F (uses both maths and stats)
- What model is best suited for predicting categories or classes? -> classification
- The “Predicted vs. True” chart shows a diagonal trend in which the predicted value correlates closely to the true value.
- If you want to automatically pre-process the features before training, what setting should you use? -> Enable featurization
- In a residual histogram, what do residuals represent? -> 

- A hospital wants to categorize patients that are pregnant as low-risk or high-risk regarding complications based on data like patient age and known medical conditions. What kind of machine learning model should the hospital use? -> Classification

- A meteorological institute wants to predict, based on data from the past, how much it will rain next Sunday. What machine learning model is the best fit for this case? -> Time series forecasting
- A toy company wants to predict the daily demand in order to assure that they have the necessary stock to honour all orders. What machine learning model can be used in this case? -> Regression
- Azure Machine Learning includes an automated machine learning capability that leverages the scalability of cloud compute to automatically try multiple pre-processing techniques and model-training algorithms in parallel to find the best performing supervised machine learning model for your data.

- A bike rental company can use historic data to train a model that predicts daily rental demand in order to make sure sufficient staff and cycles are available.
- What setting should you configure if you want to end the experiment if the model achieves a certain score or less on normalized root mean squared error metric? -> Metric score threshold 

