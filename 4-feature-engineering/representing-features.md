
Improving model accuracy with new features
--

- The data is based on 1990 census data from California. 
- This data is at the city block level, so these features reflect the total number of rooms in that block, or the total number of people who live on that block, respectively.

- data available at - https://storage.googleapis.com/ml_universities/california_housing_train.csv 

```
"longitude","latitude","housing_median_age","total_rooms","total_bedrooms","population","households","median_income","median_house_value"
-114.310000,34.190000,15.000000,5612.000000,1283.000000,1015.000000,472.000000,1.493600,66900.000000
-114.470000,34.400000,19.000000,7650.000000,1901.000000,1129.000000,463.000000,1.820000,80100.000000
-114.560000,33.690000,17.000000,720.000000,174.000000,333.000000,117.000000,1.650900,85700.000000
-114.570000,33.640000,14.000000,1501.000000,337.000000,515.000000,226.000000,3.191700,73400.000000
-114.570000,33.570000,20.000000,1454.000000,326.000000,624.000000,262.000000,1.925000,65500.000000
-114.580000,33.630000,29.000000,1387.000000,236.000000,671.000000,239.000000,3.343800,74000.000000
-114.580000,33.610000,25.000000,2907.000000,680.000000,1841.000000,633.000000,2.676800,82400.000000
-114.590000,34.830000,41.000000,812.000000,168.000000,375.000000,158.000000,1.708300,48500.000000
-114.590000,33.610000,34.000000,4789.000000,1175.000000,3134.000000,1056.000000,2.178200,58400.000000
```

```
datalab create model-accurany-vm --zone us-west1-a

%bash
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
rm -rf training-data-analyst/.git
```

goto https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive/04_features/a_features.ipynb

```python
import math
import shutil
import numpy as np
import pandas as pd
import tensorflow as tf

print(tf.__version__)
tf.logging.set_verbosity(tf.logging.INFO)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

df = pd.read_csv("https://storage.googleapis.com/ml_universities/california_housing_train.csv", sep=",")

# Examine and split the data
df.head()
# print out a quick summary of a few useful statistics on each column.
df.describe()

# Now, split the data into two parts -- training and evaluation.
np.random.seed(seed=1) #makes result reproducible
msk = np.random.rand(len(df)) < 0.8
traindf = df[msk]
evaldf = df[~msk]


# Training and Evaluation
# we'll be trying to predict median_house_value It will be our label

# We divide total_rooms by households to get avg_rooms_per_house 
# which we excect to positively correlate with median_house_value.

# We also divide population by total_rooms to get avg_persons_per_room 
# which we expect to negatively correlate with median_house_value.

def add_more_features(df):
  df['avg_rooms_per_house'] = df['total_rooms'] / df['households'] #expect positive correlation
  df['avg_persons_per_room'] = df['population'] / df['total_rooms'] #expect negative correlation
  return df

# Create pandas input function
def make_input_fn(df, num_epochs):
  return tf.estimator.inputs.pandas_input_fn(
    x = add_more_features(df),
    y = df['median_house_value'] / 100000, # will talk about why later in the course
    batch_size = 128,
    num_epochs = num_epochs,
    shuffle = True,
    queue_capacity = 1000,
    num_threads = 1
  )

# Create pandas input function
def make_input_fn(df, num_epochs):
  return tf.estimator.inputs.pandas_input_fn(
    x = add_more_features(df),
    y = df['median_house_value'] / 100000, # will talk about why later in the course
    batch_size = 128,
    num_epochs = num_epochs,
    shuffle = True,
    queue_capacity = 1000,
    num_threads = 1
  )

# Define your feature columns
def create_feature_cols():
  return [
    tf.feature_column.numeric_column('housing_median_age'),
    tf.feature_column.bucketized_column(tf.feature_column.numeric_column('latitude'), boundaries = np.arange(32.0, 42, 1).tolist()),
    tf.feature_column.numeric_column('avg_rooms_per_house'),
    tf.feature_column.numeric_column('avg_persons_per_room'),
    tf.feature_column.numeric_column('median_income')
  ]

# Create estimator train and evaluate function
def train_and_evaluate(output_dir, num_train_steps):
  estimator = tf.estimator.LinearRegressor(model_dir = output_dir, feature_columns = create_feature_cols())

  train_spec = tf.estimator.TrainSpec(input_fn = make_input_fn(traindf, None), 
                                      max_steps = num_train_steps)

  eval_spec = tf.estimator.EvalSpec(input_fn = make_input_fn(evaldf, 1), 
                                    steps = None, 
                                    start_delay_secs = 1, # start evaluating after N seconds, 
                                    throttle_secs = 5)  # evaluate every N seconds
  tf.estimator.train_and_evaluate(estimator, train_spec, eval_spec)

# Launch tensorboard
from google.datalab.ml import TensorBoard

OUTDIR = './trained_model'
TensorBoard().start(OUTDIR)

# Run the model
shutil.rmtree(OUTDIR, ignore_errors = True)
train_and_evaluate(OUTDIR, 2000)
```

train and evaluate logs

```
INFO:tensorflow:Running training and evaluation locally (non-distributed).
INFO:tensorflow:Start train and evaluate loop. The evaluate will happen after 5 secs (eval_spec.throttle_secs) or training is finished.
INFO:tensorflow:Calling model_fn.
INFO:tensorflow:Done calling model_fn.
INFO:tensorflow:Create CheckpointSaverHook.
INFO:tensorflow:Graph was finalized.
INFO:tensorflow:Running local_init_op.
INFO:tensorflow:Done running local_init_op.
INFO:tensorflow:Saving checkpoints for 1 into ./trained_model/model.ckpt.
INFO:tensorflow:loss = 530.2025, step = 1
INFO:tensorflow:global_step/sec: 148.239
INFO:tensorflow:loss = 52.032715, step = 101 (0.681 sec)
INFO:tensorflow:global_step/sec: 267.409
INFO:tensorflow:loss = 115.36275, step = 201 (0.369 sec)
INFO:tensorflow:global_step/sec: 295.495
INFO:tensorflow:loss = 61.91409, step = 301 (0.339 sec)
INFO:tensorflow:global_step/sec: 293.541
INFO:tensorflow:loss = 100.31825, step = 401 (0.341 sec)
INFO:tensorflow:global_step/sec: 269.872
INFO:tensorflow:loss = 101.17651, step = 501 (0.370 sec)
INFO:tensorflow:global_step/sec: 295.932
INFO:tensorflow:loss = 66.13982, step = 601 (0.338 sec)
INFO:tensorflow:global_step/sec: 284.78
INFO:tensorflow:loss = 55.435104, step = 701 (0.351 sec)
INFO:tensorflow:global_step/sec: 254.224
INFO:tensorflow:loss = 73.31679, step = 801 (0.395 sec)
INFO:tensorflow:global_step/sec: 275.567
INFO:tensorflow:loss = 45.28818, step = 901 (0.361 sec)
INFO:tensorflow:global_step/sec: 277.672
INFO:tensorflow:loss = 73.05077, step = 1001 (0.361 sec)
INFO:tensorflow:global_step/sec: 289.512
INFO:tensorflow:loss = 80.970406, step = 1101 (0.345 sec)
INFO:tensorflow:Saving checkpoints for 1118 into ./trained_model/model.ckpt.
INFO:tensorflow:Loss for final step: 52.60605.
INFO:tensorflow:Calling model_fn.
INFO:tensorflow:Done calling model_fn.
INFO:tensorflow:Starting evaluation at 2018-07-08-20:55:58
INFO:tensorflow:Graph was finalized.
INFO:tensorflow:Restoring parameters from ./trained_model/model.ckpt-1118
INFO:tensorflow:Running local_init_op.
INFO:tensorflow:Done running local_init_op.
INFO:tensorflow:Finished evaluation at 2018-07-08-20:55:58
INFO:tensorflow:Saving dict for global step 1118: average_loss = 0.6462896, global_step = 1118, loss = 81.097374
INFO:tensorflow:Calling model_fn.
INFO:tensorflow:Done calling model_fn.
INFO:tensorflow:Create CheckpointSaverHook.
INFO:tensorflow:Graph was finalized.
INFO:tensorflow:Restoring parameters from ./trained_model/model.ckpt-1118
INFO:tensorflow:Running local_init_op.
INFO:tensorflow:Done running local_init_op.
INFO:tensorflow:Saving checkpoints for 1119 into ./trained_model/model.ckpt.
INFO:tensorflow:loss = 234.93808, step = 1119
INFO:tensorflow:global_step/sec: 146.523
INFO:tensorflow:loss = 64.922424, step = 1219 (0.686 sec)
INFO:tensorflow:global_step/sec: 302.106
INFO:tensorflow:loss = 46.638298, step = 1319 (0.329 sec)
INFO:tensorflow:global_step/sec: 285.932
INFO:tensorflow:loss = 41.406128, step = 1419 (0.350 sec)
INFO:tensorflow:global_step/sec: 276.216
INFO:tensorflow:loss = 77.740486, step = 1519 (0.362 sec)
INFO:tensorflow:global_step/sec: 288.76
INFO:tensorflow:loss = 85.08585, step = 1619 (0.348 sec)
INFO:tensorflow:global_step/sec: 260.541
INFO:tensorflow:loss = 58.586273, step = 1719 (0.382 sec)
INFO:tensorflow:global_step/sec: 291.87
INFO:tensorflow:loss = 50.74377, step = 1819 (0.343 sec)
INFO:tensorflow:global_step/sec: 291.686
INFO:tensorflow:loss = 74.3121, step = 1919 (0.343 sec)
INFO:tensorflow:Saving checkpoints for 2000 into ./trained_model/model.ckpt.
INFO:tensorflow:Loss for final step: 62.122017.
INFO:tensorflow:Calling model_fn.
INFO:tensorflow:Done calling model_fn.
INFO:tensorflow:Starting evaluation at 2018-07-08-20:56:03
INFO:tensorflow:Graph was finalized.
INFO:tensorflow:Restoring parameters from ./trained_model/model.ckpt-2000
INFO:tensorflow:Running local_init_op.
INFO:tensorflow:Done running local_init_op.
INFO:tensorflow:Finished evaluation at 2018-07-08-20:56:03
INFO:tensorflow:Saving dict for global step 2000: average_loss = 0.6026247, global_step = 2000, loss = 75.61825
```

# Because this is a simple linear model, we can determine feature importance by printing and 
# inspecting the learned weights in our checkpoint file.

```python
from tensorflow.python.tools import inspect_checkpoint
inspect_checkpoint.print_tensors_in_checkpoint_file("trained_model/model.ckpt-2000", tensor_name='linear/linear_model/housing_median_age/weights', all_tensors=False)
inspect_checkpoint.print_tensors_in_checkpoint_file("trained_model/model.ckpt-2000", tensor_name='linear/linear_model/median_income/weights', all_tensors=False)
inspect_checkpoint.print_tensors_in_checkpoint_file("trained_model/model.ckpt-2000", tensor_name='linear/linear_model/avg_rooms_per_house/weights', all_tensors=False)
inspect_checkpoint.print_tensors_in_checkpoint_file("trained_model/model.ckpt-2000", tensor_name='linear/linear_model/avg_persons_per_room/weights', all_tensors=False)
inspect_checkpoint.print_tensors_in_checkpoint_file("trained_model/model.ckpt-2000", tensor_name='linear/linear_model/latitude_bucketized/weights', all_tensors=False)
```

Quiz
----

What is one-hot encoding?
- One hot encoding is a process by which categorical variables are converted into a form that could be provided to neural networks to do a better job in prediction.

What do you use the tf.feature_column.bucketized_column function for?
- https://www.tensorflow.org/api_docs/python/tf/feature_column/bucketized_column
- To discretize floating point values into a smaller number of categorical bins

Which of these offers the best way to encode categorical data that is already indexed, i.e. has integers in [0-N]?
- tf.feature_column.categorical_column_with_identity
- https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_identity


