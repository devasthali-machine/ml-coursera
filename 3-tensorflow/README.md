
Part1
------

1) What is TensorFlow? (choose all that apply)

- TensorFlow is an open-source high-performance library for numerical computation that uses directed graphs

2) True or False: When you run a TensorFlow graph (like a + b), you immediately get the output of the graph (the sum of a and b)
- True - but only if you have tf.eager mode enabled


3) What do nodes in a TensorFlow graph represent?
- Nodes represent Mathematical operations
- Edges represent tensors

4) TensorFlow programs are directed graphs. What are some of the benefits?

- TensorFlow can insert send and receive nodes to distribute the graph across machines
- TensorFlow can optimize the graph by merging successive nodes where necessary

5) What is a tensor?
- A n-dimensional array of data (generalization of a vector)

6) True or False: You can only run TensorFlow on Google Cloud
- F

7) What is the high level API that allows for distributed training in TensorFlow?
- tf.estimator

8) How do you run a TensorFlow graph?
- Call run() on a tf.Session

9) Why would you call tf.summary.FileWriter?
- To output statistics and visualize them in a tool like TensorBoard

10) What is the shape of tf.constant([2, 3, 5])?
- It's a vector so it would be (3)

11) The iterative process where a TensorFlow model can crowdsource and combine model feedback from individual users is called what?
- Federated learning

12) Which of these abstraction levels treats TensorFlow as a numeric processing library?
- Python API

Part 2
------

1) What are some of the key goals of the estimator API?
- Create production-ready machine learning models using an API
- Train on large datasets that do not fit in memory
- Quickly monitor your training metrics in Tensorboard

2) What is one of the largest benefits of the estimator API?
- It abstracts away boilerplate code which saves you time

_Hyperparameters are model-specific properties that are ‘fixed’ before you even train and test your model on data. One example is the decision tree._

3) What is the right way to call a linear regression model with tf.estimator?
- tf.estimator.LinearRegressor - https://www.tensorflow.org/api_docs/python/tf/estimator/LinearRegressor

4) Inputs to the estimator model are in the form of:
- feature columns, Feature columns tell the model what inputs to expect

5) Numeric inputs can be passed to a linear regressor as-is, but categorical columns are often:
- One-hot encoded - https://www.kaggle.com/dansbecker/using-categorical-data-with-one-hot-encoding

```
tf.feature_column.categorical_column_with_vocabulary_list("type", ["house", "apt"])
```

6) What is the size of the training dataset (features + labels) in this example?

```
def train_input_fn():
 features = {"sq_footage": [ 1000, 2000, 3000, 1000, 2000, 3000],
 "type": ["house", "house", "house", "apt", "apt", "apt"]}

 # prices in thousands
 labels = [ 500, 1000, 1500, 700, 1300, 1900]
 return features, labels
```
- 6 rows, 3 columns

7) In this example, what extra parameters does the DNNRegressor take that the LinearRegressor doesn't?

```python
model = tf.estimator.DNNRegressor(featcols,
hidden_units=[3, 2])
```

- https://www.tensorflow.org/versions/r1.3/get_started/estimator
-There really two decisions that must be made regarding the hidden layers: 
* how many hidden layers to actually have in the neural network and 
* how many neurons will be in each of these layers. 
- https://www.tensorflow.org/get_started/premade_estimators
- answer to question: hidden_units

8) In what situation do you have to delete the model directory before starting training?

- If you have changed the model structure from the previous time, for example, you used a DNNRegressor with [64,32] last time and now you are using [32, 16]
- The old checkpoints are no longer valid for your new model structure. So, you have to start afresh

9) What is the difference between steps and max_steps in epochs?

```python
def pandas_train_input_fn(df): # a Pandas dataframe
 return tf.estimator.inputs.pandas_input_fn(
 x = df,
 y = df['price'],
 batch_size=128,
 num_epochs=10,
 shuffle=True
 )
model.train(pandas_train_input_fn(df))
model.train(pandas_train_input_fn(df), steps=1000)
model.train(pandas_train_input_fn(df), max_steps=1000)
```

- Training happens until input is exhausted or number of steps is reached 
- epoch: the number of times you run over the data set extracting batches to feed the learning algorithm.
- steps: batches
- max_steps: another argument for LinearRegressor.train() method. This argument defines the maximum number of steps (batches) can process in the LinearRegressor() objects lifetime.

https://stackoverflow.com/a/44543550/432903

Say you have 1000 data examples. 
Setting 
batch size = 100, 
epoch = 1 and 
steps = 200 gives a process with one pass (one epoch) over the entire data set. 
In each pass it will feed the algorithm a batch with 100 examples. The algorithm will run 200 steps in each batch. In total, 10 batches are seen. 

If you change the epoch to 25, then it will iterate this 25 times, and you get 25x10 batches seen altogether.

- Steps means "train these many additional steps". 
- max_steps means "train up to these many steps total, starting from how many ever steps have been completed so far"
