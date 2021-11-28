OCR
----
- detect text, images to convert into text
- machine reading comprehension => what is text is about?
- Ex: 
Scanning printed or handwritten checks for bank deposits.
Digitizing forms, such as medical records or historical documents.

- computer vision service or general cognitive resource
- images can have typed, hand written => JPEG, PNG
- Azure OCR API: quick text extraction with regions of text and text lines 
- Read API: optimized for noisy documents =>returns Pages, Lines, Words 

exercise
--
- https://docs.microsoft.com/en-us/learn/modules/read-text-computer-vision/3-read-text-computer-vision?launch-lab=true
- When you use the OCR API to process an image, what hierarchy of information does it return?
- Because the Read API can work with larger documents, it works asynchronously so as not to block your application while it is reading the content and returning results to your application.
- 

Form recogniser/ Receipt Analysis
------------------
- https://docs.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/
- pre-trained models with receipts in English(restaurants, gas stations). can extract basic stuff like: time of transaction, total amount, taxes paid
- need Azure cognitive resources
- image must be JPEG, PNG, Bitmap, PDF. Min size is `50 * 50`
- https://docs.microsoft.com/en-us/learn/modules/analyze-receipts-form-recognizer/3-analyze-receipts?launch-lab=true
- You plan on training your custom model for Form Recognizer. What is the minimum number of samples that you need to train your model? => 5
