'''
hello kura-yantra
'''

from __future__ import print_function

import tensorflow as tf

# Simple hello world using TensorFlow

# Create a Constant op
# The op is added as a node to the default graph.
#
# The value returned by the constructor represents the output
# of the Constant op.
feature_hello = tf.constant('Hello, kura-yantra!')

# Start tf session
sess = tf.Session()

# Run the op
print(sess.run(feature_hello))
