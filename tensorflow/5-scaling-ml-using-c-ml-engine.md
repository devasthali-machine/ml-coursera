In this notebook, we take a previously developed TensorFlow model to predict taxifare rides and package it up so that it can be run in Cloud MLE. For now, we'll run this on a small dataset. 

```
datalab create cloud-ml-e --zone us-west1-a

%bash
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
rm -rf training-data-analyst/.git

```

https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive/03_tensorflow/e_cloudmle.ipynb

True or False: In the packaging model recommended in this module, the task.py file you create contains the actual ML model in TensorFlow
- False - this is actually contained in model.py


