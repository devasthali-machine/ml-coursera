
in this nb, lets refactor to call `train_and_evaluate` instead of hand-coding our ML pipeline

```
datalab create m --zone us-west1-a

%bash
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
rm -rf training-data-analyst/.git
```

train.csv

```
$ head taxi-train.csv 
12.0,-73.987625,40.750617,-73.971163,40.78518,1,0
4.5,-73.96362,40.774363,-73.953485,40.772665,1,1
4.5,-73.989649,40.756633,-73.985597,40.765662,1,2
10.0,-73.9939498901,40.7275238037,-74.0065841675,40.7442398071,1,3
2.5,-73.950223,40.66896,-73.948112,40.668872,6,4
7.3,-73.98511,40.742173,-73.96586,40.759668,4,5
8.1,-73.997638,40.720887,-74.012937,40.716323,2,6
41.5,-74.004283,40.740476,-73.897273,40.817774,2,7
5.3,-73.984345,40.755862,-73.98152,40.750347,1,8
13.5,-73.9615020752,40.7683258057,-73.9846801758,40.7363166809,1,9
```

```python
import datalab.bigquery as bq
import tensorflow as tf
import numpy as np
import shutil
from google.datalab.ml import TensorBoard
print(tf.__version__)

# Read data created in Lab1a, but this time make it more general, so that we are reading in batches. 
# Instead of using Pandas, we will use add a filename queue to the TensorFlow graph.

CSV_COLUMNS = ['fare_amount', 'pickuplon','pickuplat','dropofflon','dropofflat','passengers', 'key']
LABEL_COLUMN = 'fare_amount'
DEFAULTS = [[0.0], [-74.0], [40.0], [-74.0], [40.7], [1.0], ['nokey']]

def read_dataset(filename, mode, batch_size = 512):
  def _input_fn():
    def decode_csv(value_column):
      columns = tf.decode_csv(value_column, record_defaults = DEFAULTS)
      features = dict(zip(CSV_COLUMNS, columns))
      label = features.pop(LABEL_COLUMN)
      return features, label

    # Create list of file names that match "glob" pattern (i.e. data_file_*.csv)
    filenames_dataset = tf.data.Dataset.list_files(filename)
    # Read lines from text files
    textlines_dataset = filenames_dataset.flat_map(tf.data.TextLineDataset)
    # Parse text lines as comma-separated values (CSV)
    dataset = textlines_dataset.map(decode_csv)
    
    # Note:
    # use tf.data.Dataset.flat_map to apply one to many transformations (here: filename -> text lines)
    # use tf.data.Dataset.map      to apply one to one  transformations (here: text line -> feature list)
    
    if mode == tf.estimator.ModeKeys.TRAIN:
        num_epochs = None # indefinitely
        dataset = dataset.shuffle(buffer_size = 10 * batch_size)
    else:
        num_epochs = 1 # end-of-input after this

    dataset = dataset.repeat(num_epochs).batch(batch_size)
    
    return dataset.make_one_shot_iterator().get_next()
  return _input_fn
    

def get_train():
  return read_dataset('./taxi-train.csv', mode = tf.estimator.ModeKeys.TRAIN)

def get_valid():
  return read_dataset('./taxi-valid.csv', mode = tf.estimator.ModeKeys.EVAL)

def get_test():
  return read_dataset('./taxi-test.csv', mode = tf.estimator.ModeKeys.EVAL)

# Create features out of input data
INPUT_COLUMNS = [
    tf.feature_column.numeric_column('pickuplon'),
    tf.feature_column.numeric_column('pickuplat'),
    tf.feature_column.numeric_column('dropofflat'),
    tf.feature_column.numeric_column('dropofflon'),
    tf.feature_column.numeric_column('passengers'),
]

def add_more_features(feats):
  # Nothing to add (yet!)
  return feats

feature_cols = add_more_features(INPUT_COLUMNS)

# Serving input function
# Defines the expected shape of the JSON feed that the model
# will receive once deployed behind a REST API in production.
def serving_input_fn():
  feature_placeholders = {
    'pickuplon' : tf.placeholder(tf.float32, [None]),
    'pickuplat' : tf.placeholder(tf.float32, [None]),
    'dropofflat' : tf.placeholder(tf.float32, [None]),
    'dropofflon' : tf.placeholder(tf.float32, [None]),
    'passengers' : tf.placeholder(tf.float32, [None]),
  }
  # You can transforma data here from the input format to the format expected by your model.
  features = feature_placeholders # no transformation needed
  return tf.estimator.export.ServingInputReceiver(features, feature_placeholders)

# tf.estimator.train_and_evaluate

def train_and_evaluate(output_dir, num_train_steps):
  estimator = tf.estimator.LinearRegressor(
                       model_dir = output_dir,
                       feature_columns = feature_cols)
  train_spec=tf.estimator.TrainSpec(
                       input_fn = read_dataset('./taxi-train.csv', mode = tf.estimator.ModeKeys.TRAIN),
                       max_steps = num_train_steps)
  exporter = tf.estimator.LatestExporter('exporter', serving_input_fn)
  eval_spec=tf.estimator.EvalSpec(
                       input_fn = read_dataset('./taxi-valid.csv', mode = tf.estimator.ModeKeys.EVAL),
                       steps = None,
                       start_delay_secs = 1, # start evaluating after N seconds
                       throttle_secs = 10,  # evaluate every N seconds
                       exporters = exporter)
  tf.estimator.train_and_evaluate(estimator, train_spec, eval_spec)

OUTDIR = 'taxi_trained'
TensorBoard().start(OUTDIR)


# Run training    
shutil.rmtree(OUTDIR, ignore_errors = True) # start fresh each time
train_and_evaluate(OUTDIR, num_train_steps = 2000)


# to list Tensorboard instances
TensorBoard().list()

# to stop TensorBoard fill the correct pid below
#TensorBoard().stop(27855)
#print("Stopped Tensorboard")

```

https://www.tensorflow.org/api_docs/python/tf/estimator/export/ServingInputReceiver
