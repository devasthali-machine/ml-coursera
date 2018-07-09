
You are training a model to predict how long it will take to sell a house. The list price of the house, with numeric $20,000 to $500,000 values, is one of the inputs to the model. Which of these is a good practice?
- Rescale the real valued feature like a price to a range from 0 to 1

Which of these tools are commonly used for data pre-processing?
- apache beam
- big-query
- tf

Which one of these is NOT something you would commonly do in data preprocessing?
- Compute time-windowed statistics (e.g. number of products sold in previous hour) for use as input features
- Tune your ML model hyperparameters - X
- Compute vocabularies for categorical columns
- Compute aggregate statistics for numeric columns
- Remove examples that you don’t want to train on - X

In your TensorFlow model you are calculating the distance between two points on a map as a new feature. How do you ensure the preprocessing you're doing for model training is also do the exact same way in prediction?

```python
def add_feat_engineered(features):
    lats = features['pickup_lat']
    
    distance = tf.sqrt (lat_diff * lat_diff + lon_diff * lon_diff )
    features['euclidean'] = distance

    return features
```

- Wrap features in training/evaluation input function AND wrap features in serving input function:

The below code preprocesses the latitude and longitude using feature columns. What is the point of the 38.0 and 42.0 in the column buckets?

```python
lat_buckets = np.linespace(38.0, 42.0, n_buckets).tolist()
```

- https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html
- Latitudes must be between 38 and 42 will be discretized into the specified number of bins.

What is a one advantage of using TensorFlow to preprocess your code instead of building an Apache Beam pipeline?
- In TensorFlow you will have access to helper APIs to help automatically bucketize and process features instead of writing your own java or python code
- In TensorFlow the same pipelines can be used in both training and serving

What is one key advantage of preprocessing your features using Apache Beam?
- The same code you use to preprocess features in training and evaluation can also be used in serving
