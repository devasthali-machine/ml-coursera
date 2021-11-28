custom vision
-----------------
- image classification
- object detection: class of each object in image with co-ordinates. Ex: self driving cars, MRIs, xrays reading 
- The model training process is an iterative process in which the Custom Vision service repeatedly trains the model using some of the data, but holds some back to evaluate the model.

- training resources
- prediction resources
- to use both you can use Azure Cognitive resources

Image tagging for training
---------------------------

- tag objects in image with boundaries

Evaluation
----------

- P
- R
- MAP


- Compared to the image classification capability, what additional features does the object detection capability offer? =>  bounding box that indicates the object’s location
- Object detection returns a probability score for each object that it classifies. What is this score also called? => Confidence
- Before you can train an object detection model, you must tag the classes and bounding box coordinates in a set of training images. => T
- You plan on using object detection. After you have trained your model, you want to assess the performance of the model. Which performance metrics are available for you to analyze?
- Object detection is a form of machine learning-based computer vision in which a model is trained to recognize individual types of objects in an image, and to identify their location in the image. => T
- You are using the object detection capability toevaluate the performance metrics of the trained model. You observe that the recall metric has a value of 0.7. What does this mean? => The model identified the class in 70% of the images 
- What key considerations should you make when tagging training images for object detection?
1) Making sure the bounding boxes are defined tightly around each object
2) Having images of the objects in question for multiple angles
3) Ensuring sufficient images of the objects in question  
- Question 1
You have built a solution that detects objects in images. You are using the same endpoint and key to predict as you usedwhen you trained the model. What type of service are you using? => Cognitive Service
