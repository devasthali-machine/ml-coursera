- predictive models are used to predict unknown values
- training ML models are time consuming and resource intensive
- ML example: bicycle rental. features(x)= weather, label(y) = number of rentals => regression
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


creating ML model training pipeline using designers
---
ML model steps can be designed using ML designers like Azure ML designer or https://cloud.google.com/ai-platform/docs/ml-solutions-overview

regression performance metrics: 
- Mean Absolute Error (MAE): The average difference between predicted values and true values
- Root Mean Squared Error (RMSE): The square root of the mean squared difference between predicted and true values
- Relative Squared Error (RSE): A relative metric between 0 and 1 based on the square of the differences between predicted and true values
- Relative Absolute Error (RAE)
- Coefficient of Determination (R2)

ML model inference pipeline
---------------------------

- After creating and running a pipeline to train the model, you need a second pipeline that performs the same data transformations for new data, and then uses the trained model to inference  (in other words, predict) label values based on its features. This will form the basis for a predictive service that you can publish for applications to use. 

- The inference pipeline assumes that new data will match the schema of the original training data, so the "Automobile price data (Raw) dataset" from the training pipeline is included.
- However, this input data includes the price label that the model predicts, which is unintuitive to include in new car data for which a price prediction has not yet been made. 
- Delete this module and replace it with an Enter Data Manually module from the Data Input and Output section, containing the following CSV data, which includes feature values without labels for three cars.  
```
symboling,normalized-losses,make,fuel-type,aspiration,num-of-doors,body-style,drive-wheels,engine-location,wheel-base,length,width,height,curb-weight,engine-type,num-of-cylinders,engine-size,fuel-system,bore,stroke,compression-ratio,horsepower,peak-rpm,city-mpg,highway-mpg
3,NaN,alfa-romero,gas,std,two,convertible,rwd,front,88.6,168.8,64.1,48.8,2548,dohc,four,130,mpfi,3.47,2.68,9,111,5000,21,27
3,NaN,alfa-romero,gas,std,two,convertible,rwd,front,88.6,168.8,64.1,48.8,2548,dohc,four,130,mpfi,3.47,2.68,9,111,5000,21,27
1,NaN,alfa-romero,gas,std,two,hatchback,rwd,front,94.5,171.2,65.5,52.4,2823,ohcv,six,152,mpfi,2.68,3.47,9,154,5000,19,26
```

- "Inference pipeline" does not need "Evaluation model" when predicting from new data, so delete this module.

Preictive Service Deployment
---------------

```python
endpoint = 'YOUR_ENDPOINT' #Replace with your endpoint
key = 'YOUR_KEY' #Replace with your key

import urllib.request
import json
import os

# Prepare the input data
data = {
    "Inputs": {
        "WebServiceInput0":
        [
            {
                    'symboling': 3,
                    'normalized-losses': None,
                    'make': "alfa-romero",
                    'fuel-type': "gas",
                    'aspiration': "std",
                    'num-of-doors': "two",
                    'body-style': "convertible",
                    'drive-wheels': "rwd",
                    'engine-location': "front",
                    'wheel-base': 88.6,
                    'length': 168.8,
                    'width': 64.1,
                    'height': 48.8,
                    'curb-weight': 2548,
                    'engine-type': "dohc",
                    'num-of-cylinders': "four",
                    'engine-size': 130,
                    'fuel-system': "mpfi",
                    'bore': 3.47,
                    'stroke': 2.68,
                    'compression-ratio': 9,
                    'horsepower': 111,
                    'peak-rpm': 5000,
                    'city-mpg': 21,
                    'highway-mpg': 27,
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
    y = json_result["Results"]["WebServiceOutput0"][0]["predicted_price"]
    print('Predicted price: {:.2f}'.format(y))

except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers to help debug the error
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
```

- Suppose you created a machine learning model and you want to train it. Which compute target should you use? => Compute Clusters 
- After creating and running a pipeline to train the model, you need a second pipeline that performs the same data transformations for new data, and then uses the trained model to predict label values based on its features. => True, An inference pipeline will form the basis for a predictive service that you can publish for applications to use.

- You are creating a training pipeline for a regression model and you want to make sure that the dataset is complete, otherwise you need to perform various operations to fix the data. Which module should you add to the pipeline? => Clean missing data
- You are creating a training pipeline for a regression model and your dataset contains hundreds of columns. For a particular part of your model, you want to use data only from some specific columns. Which module should you add to the pipeline? => Select columns in a dataset 
- You created a machine learning model and trained it. Now you want to run the model to predict data. Which compute target should you use? => Inference Clusters
