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


