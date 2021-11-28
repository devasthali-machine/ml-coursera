- Computer vision is a field of  AI that trains computers to interpret and understand the visual world.
The goal of computer vision is to extract useful information from images.
- the benefits of Computer Vision in our day-to-day lives: language translation, 
reading cars license plate, [cancer detection](https://www.researchgate.net/publication/332778132_Application_of_Computer_Vision_and_Deep_Learning_in_Breast_Cancer_Assisted_Diagnosis), [Tumor Detection](https://viso.ai/deep-learning/mask-r-cnn/)

- An AI application bases its predictions about the contents of image by processing the pixel numerical values to use as features when training machine learning models.

- Interpret image, suggest tags, categorize, identify objects, brands in image etc.
- uses OCR to identify printed/ hand written 


https://docs.microsoft.com/en-us/learn/modules/analyze-images-computer-vision/3-analyze-images
- For example, suppose the retailer "FarWest Traders" has decided to implement a "smart store", in which AI services monitor the store to identify customers 
requiring assistance, and direct employees to help them. By using the Computer Vision service, images taken by cameras throughout the store can be analyzed 
to provide meaningful descriptions of what they depict.
- https://github.com/MicrosoftLearning/AI-900-AIFundamentals

- capabilities listed below are covered by Computer Vision: Interpret an image and suggest an appropriate caption, Categorize an image , Read the text in an image
- You are building a solution that uses Computer Vision and you want to associate the images you process with metadata that summarizes the attributes of the image. 
What feature should you use? => Tags
- You want to determine if celebrities appear in a set of pictures. What feature of Computer Vision should you use? => Tags can be associated with the images as metadata 
that summarizes attributes of the images.
- You are planning on creating a solution that will scan images to extract pieces of text from them. 
Which capability from Computer Vision should you use? => OCR
- https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/category-taxonomy


Image classification
----------------------
- Classification use features/ labels to classify data.
- Image classification uses set of categorized images (array of pixel values) to train a model. 
Patterns in image pixel values are used to determine which class a particular image belongs, and 
a model is trained to match the patterns in the pixel values to a set of class labels.
- Image classification uses Deep Learning techniques CNN
- training effective CNN is a complex task 
- uses: Product identification in store, Disaster Investigation (eg. Bridges), Medical diagnosis(Xray images to detect Cancer, tumor)
- can use Azure custom vision or Azure cognitive service for training and predicting model
- make sure images for training are enough, from many different angles.
- evaluation metrics for trained model
1) P: % of class predictions are correct. 8 correct out of 10 = 80%
2) R: correctly identified 
3) Average P: 

MS Azure has
1) Computer visiion: form recogniser, text, face detection
2) Custom vision: custom object detection

- exercise: https://docs.microsoft.com/en-us/learn/modules/classify-images-custom-vision/3-create-image-classifier
- golai-grocery-checkout
- Image classification is a capability that is part of which cognitive service in Azure? => Custom Vision 
- You are using Custom Vision and you want to evaluate the performance of your trained model. Which metric indicates the percentage of the correct class predictions? => Precision
- You are planning on creating an AI solution that will use Computer Vision capabilities.To access the APIs, what two pieces of information do you need to use? => An endpoint, A key
- You want to build a solution that needs to detect images that contain adult content or depict violent, gory scenes. Which service would you use to achieve the task? => Computer Vision
- You plan on creating a solution that will scan a gallery of photos for images that contain product placement. Which capability of Computer Vision should you use? => Detect brands
- You want to use the Computer Vision service with images where the dominant foreground color is red. Which of the following capabilities should you use? => Detect image color schemes
- To train a classification model, you must upload images to your training resource and label them with the appropriate class labels. Y
- You are training your image classification model and you realize that some images are not classified correctly. What should you do to improve the model? => Add additional images to the training set
- You are creating a solution that needs to identify if celebrities are present in images and also to determine their age. What capabilities should you take into account? => Detect faces, Detect domain-specific content 
- You are creating a solution that needs to extract handwritten text from several image scans. Which Computer Vision capability should you use? => Optical character recognition
