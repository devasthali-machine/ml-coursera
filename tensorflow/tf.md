
What is TensorFlow? (choose all that apply)

- TensorFlow is an open-source high-performance library for numerical computation that uses directed graphs

True or False: When you run a TensorFlow graph (like a + b), you immediately get the output of the graph (the sum of a and b)
- True - but only if you have tf.eager mode enabled


What do nodes in a TensorFlow graph represent?
- Mathematical operations

TensorFlow programs are directed graphs. What are some of the benefits?

- TensorFlow can insert send and receive nodes to distribute the graph across machines
- TensorFlow can optimize the graph by merging successive nodes where necessary

What is a tensor?
- A n-dimensional array of data (generalization of a vector)

True or False: You can only run TensorFlow on Google Cloud
- F

What is the high level API that allows for distributed training in TensorFlow?
- tf.estimator

How do you run a TensorFlow graph?
- Call run() on a tf.Session

Why would you call tf.summary.FileWriter?
- To output statistics and visualize them in a tool like TensorBoard

What is the shape of tf.constant([2, 3, 5])?
- It's a vector so it would be (3)

The iterative process where a TensorFlow model can crowdsource and combine model feedback from individual users is called what?
- Federated learning
