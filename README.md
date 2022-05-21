# Image Search Engine
This repository is a partially submission for code without barriers hackathon. 
The goal of this project is to build image search engine in azure web services.
Step by step solution:
 1. extract features from images and save the features in pkl format. (done)
 2. save deep learning model (feature extractor) to extract new features from user input image. (done)
 3. calculate the euclidean distances between the features from user input image and the features from database image. (done)
 4. choose the nearest distance from database image as the results. (done)
 5. register the model (feature extractor) in azure machine learning. (done)
 6. save the features from database image in azure machine learning. (done)
 7. deploy the app in azure web services. (not done yet)

For the steps 1-4 can be found in file vision-cop-image-search-engine.ipynb, and it can be run in jupyter notebook, colab, or azure machine learning SDK.
For the steps 5-7 can be found in file model deploy 2 (1).ipynb, and it can be run using azure machine learning SDK.
