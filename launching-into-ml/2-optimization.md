What is the main difference between RMSE and MSE?
- The loss metric output for RMSE is measured in the same units as the error making it easier to directly interpret

List performance metrics
- precison
- recall
- accuracy

An increase in what factor would drive down precision?
- f positives 

we had 10 actually available spaces and our model identified only 1 as available.
- Recall = 1/10 = 0.1
- recall = true p/ (true p/ false n)

10 cats. ML predicts 2 cats as cats(true p), 2 cats as tigers (as false n), 3 tigers as cats (false p)
- precision = true p / (true p + false p)
            = 2/ (2 + 3)
- recall = 2/ (2 + 4)

Which of the following is not a step in a typical model training loop?
- Take the Derivative of the Loss Function
- Take a step down the loss curve
- Calculate the Loss
- Increase the learning rate (X)
