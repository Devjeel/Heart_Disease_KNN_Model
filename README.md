## To run this code on your machine

Clone or download this project 

use this command to clone: `git clone https://github.com/Devjeel/Heart_Disease_KNN_Model.git` 

> before running the program, install necessary dependencies using following command : `pip install -r requirements.txt`

now run the flask server `server.py` file and trigger the JSON input with `request.py` file.

## Algorithm
Algorithm used: Scikit-Learn, Classification, K-NearestNeighbors

## Score Evaluation 
Improved Accuracy: `0.86813`

MAE Score: `0.13187`

## Dataset

Data source: <a href='https://www.kaggle.com/ronitf/heart-disease-uci' title='Kaggle Link'>Kaggle Dataset</a>

  
  ### Columns Info.
  ```
  #age = age in years
  #sex (1 = male; 0 = female)
  #cp = chest pain type
  #trestbps = resting blood pressure (in mm Hg on admission to the hospital)
  #chol = serum cholestoral in mg/dl
  #fbs = (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
  #restecg = resting electrocardiographic results
  #thalach = maximum heart rate achieved
  #exang = exercise induced angina (1 = yes; 0 = no)
  #oldpeak = ST depression induced by exercise relative to rest
  #slope = the slope of the peak exercise ST segment
  #ca = number of major vessels (0-3) colored by flourosopy
  #thal (3 = normal; 6 = fixed defect; 7 = reversable defect)
  #target 1 or 0
  ```
