# Enterface- A website to detect the elements of a website

## Streamlit:
In the Streamlit application we drag and drop two files:
1. Original Image (Image with which the comparison will be done)
2. Comparison Image (The designed image)

After the images are dropped, an OCR(Optical Character Recognition) will run on the images. 

The OCR will provide us with the metadata of the application. The meatdata will be parsed through a python file- through which we can gain information about the website.

The metadata would then be converted into a list of words, which would then be compared to an excel file having:
- Name of the Website 
- Category of the Website

We convert the excel file into a dictionary
> By using a dictionary we reduce the time complexity to O(1).

After the comparison is complete, we display the name and category of the websites.

In the main program, we divide the functionalities into different python files. 

Our application runs on Streamlit.

## YOLOv8:
For loading the model we are using YOLO V8 best.pt file, which is a PY-Torch file.
Through the pytorch file will be able to load the pretrained model. 

This model has been trained on the input of- Elements of a Website. 
So the sole purpose of this model is to detect and show the website elements:
- button
- field
- heading
- iframe
- image
- label
- link
- text

After the Model loads and categorizes the new input, we load the image using Pillow.
We also use OpenCV to change the visual look of our image. 
Finally, the model predicts and display it on our Streamlit application.

The results we get from the predictions are tensors of:
- xyxy – the coordinates of the box as an array [x1,y1,x2,y2]
- cls – the ID of object type
- conf – the confidence level of the model about this object. 

We then utilize OpenCV to render a rectangle around the image.

## Cosine Similarity:
Cosine similarity is a popular similarity metric we use to find the similarity between multiple vectors. 
In this project we have used this metric to generate a similarity score between the two input images. 

The input vectors for this metric are:
- Bunding box coordinates
- Height and weight of each class type

They are aggregated respectively to their classes.

The cosine similarity metric is used to generate the final score between the images. 
If the score is:
- Below 0.25: Not Similar 
- More than 0.25 but less then 0.75: Somewhat Similar
- More than 0.75: Similar in nature

## To run the application:
In the terminal of app.py file
> streamlit run app.py