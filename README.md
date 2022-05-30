# Image Search Engine - Deploy Machine Learning on Cloud Using Azure App Services

This repository is a project submission for <a href="https://codewithoutbarriers.devpost.com/"><strong>Code Without Barriers Hackathon</strong></a> Sponsored by Microsoft. The goal of this project is to build image search engine in azure web service.

### 1. Use Deep Learning Model to Search for Similar Image from User Input 
- Extract features from <a href="https://www.kaggle.com/datasets/theaayushbajaj/cbir-dataset"><strong>Image Database</strong></a> using Deep learning model and save the features in pkl format as `features.pkl`
- Save the deep learning model (feature extractor) to extract new features from user input image and save as `model.h5`
- Calculate the eauclidean distance between features from user input and features from image database
- Choose the top nearest distance

### 2. Create HTML File as a Frontend of the Web App
- Save the file as `index.html` in the template folder

### 3. Create Flask APP to Build Web App in Python
- Save the file as `app.py`
- Run app.py file on local machine
<img src="https://github.com/ImIm20/image-search-engine/blob/main/images/Screenshot%202022-05-30%20201440.png" width=600>

- Copy the URL and open it in web browser
<img src="https://github.com/ImIm20/image-search-engine/blob/main/images/Screenshot%20(205).png" width=900>

### 4 Deploy the Web APP on Cloud using Azure App Services
- The steps to deploy on azure can be seen in this <a href="https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-portal%2Cterminal-bash%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cdeploy-instructions-zip-azcli"><strong>Link</strong></a>
- Copy the url provided by the Azure App Services and run it in your browser
<img src="https://github.com/ImIm20/image-search-engine/blob/main/images/Screenshot%20(221).png" width=900>

## Documentation
<img src="https://github.com/ImIm20/image-search-engine/blob/main/images/Screenshot%20(209).png" width=900>
<img src="https://github.com/ImIm20/image-search-engine/blob/main/images/Web%20capture_30-5-2022_145725_image-search-engine.azurewebsites.net.jpeg" width=700>
