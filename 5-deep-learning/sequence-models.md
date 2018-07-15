Suppose your training examples are sentences (sequences of words). 
Which of the following refers to the j^{th}jth word in the i^{th}ith training example?
-x(i)^<j>

2) Consider this RNN:

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/WVhjoPCuEee5Rg5IFJ7l8g_a7b6030c6e5a53b431fee7aaabecd9bd_Screen-Shot-2018-01-03-at-5.48.26-PM.png?expiry=1531785600000&hmac=5n4vFV1y7_4h90YN-0D6Itvjj4TJVWfN-aj5PnlM34I)

This specific type of architecture is appropriate when:
- Tx = Ty

3) To which of these tasks would you apply a many-to-one RNN architecture? (Check all that apply).
![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/K59CdPCvEee7LQrRPHr2wA_4549ad1b1b590371eb3502e158a02447_Screen-Shot-2018-01-03-at-5.54.27-PM.png?expiry=1531785600000&hmac=FQbAy1T5nOoO8XzHuOQ8P-JxVfujRYCU2ahbgP-YgyI)

- Sentiment classification (input a piece of text and output a 0/1 to denote positive or negative sentiment)
- Gender recognition from speech (input an audio clip and output a label indicating the speaker’s gender)
- Image classification (input an image and output a label) - X

4) You are training this RNN language model.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/cxeeLPCvEee7YRLKCWJ4hg_bca1b05c70eece156b470abb2d0f0cad_Screen-Shot-2018-01-03-at-5.56.30-PM.png?expiry=1531785600000&hmac=Pn5XkPFSwYbg26OvSd8Id6M2V5A_sjG8KgA4_yhN1XE)

At the t^th time step, what is the RNN doing? Choose the best answer.
- estimating P(y<t> | y<1>, y<2>, ... y<t-1>)
- in a language model we try to predict the next step based on the knowledge of all prior steps.

5)
- (i) Use the probabilities output by the RNN to randomly sample a chosen word for that time-step as \hat{y}^{<t>} 
y^​<t> . (ii) Then pass this selected word to the next time-step.

6) You are training an RNN, and find that your weights and activations are all taking on the value of NaN (“Not a Number”). Which of these is the most likely cause of this problem?
- Exploding gradient problem.

7) Suppose you are training a LSTM. You have a 10000 word vocabulary, and are using an LSTM with 100-dimensional activations a^{<t>}a 
<t>. What is the dimension of \Gamma_uΓ u​	  at each time step?
- 100
- Γu​ is a vector of dimension equal to the number of hidden units in the LSTM.

8) Here’re the update equations for the GRU.

Alice proposes to simplify the GRU by always removing the \Gamma_uΓ u​	 . I.e., setting \Gamma_uΓ u​	  = 1. Betty proposes to simplify the GRU by removing the \Gamma_rΓ r​	 . I. e., setting \Gamma_rΓr​	  = 1 always. Which of these models is more likely to work without vanishing gradient problems even when trained on very long input sequences?

- Betty’s model (removing \Gamma_rΓ 
r
​	 ), because if \Gamma_u \approx 0Γ 
u
​	 ≈0 for a timestep, the gradient can propagate back through that timestep without much decay.

9)
- From these, we can see that the Update Gate and Forget Gate in the LSTM play a role similar to _______ and ______ in the GRU. What should go in the the blanks?

10) You have a pet dog whose mood is heavily dependent on the current and past few days’ weather. You’ve collected data for the past 365 days on the weather, which you represent as a sequence as x^{<1>}, …, x^{<365>}x 
<1>,…,x <365>. You’ve also collected data on your dog’s mood, which you represent as y^{<1>}, …, y^{<365>}y 
<1>,…,y <365>. You’d like to build a model to map from x \rightarrow yx→y. Should you use a Unidirectional RNN or Bidirectional RNN for this problem?
- Unidirectional RNN, because the value of y^{<t>}y <t> depends only on x^{<1>}, …, x^{<t>}x <1>,…,x <t> , but not on x^{<t+1>}, …, x^{<365>}x <t+1> ,…,x <365>
