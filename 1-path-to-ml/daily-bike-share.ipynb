#Replace with your endpoint
endpoint = 'http://572e15eb-df29-4f21-805d-7ab38d2d9e0f.eastus2.azurecontainer.io/score' 
#Replace with your key 
key = 'YOUR_KEY'

import json 
import requests 

## 
## An array of features based on five-day weather forecast 
## 

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

#If we got a valid response, display the predictions 

if response.status_code == 200: 
    y_prediction = json.loads(response.json()) 
    print("Predictions:") 

    for i in range(len(x_feature_data)): 
        print (" Day: {}. Predicted rentals: {}".format(i+1, max(0, round(y_prediction["result"][i])))) 

else: 
    print(response)
