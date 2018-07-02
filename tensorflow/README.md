
1) What is TensorFlow? (choose all that apply)

- TensorFlow is an open-source high-performance library for numerical computation that uses directed graphs

2) True or False: When you run a TensorFlow graph (like a + b), you immediately get the output of the graph (the sum of a and b)
- True - but only if you have tf.eager mode enabled


3) What do nodes in a TensorFlow graph represent?
- Mathematical operations

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

Which of these abstraction levels treats TensorFlow as a numeric processing library?
- Python API
