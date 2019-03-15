# -*- coding: utf-8 -*-
'''
This file request server in json 
'''

import requests

url = 'http://127.0.0.1:5000/api/v01'

r = requests.post(url, json={'age': 68, 'sex': 1, 'cp': 0, 'trestbps': 144, 'chol': 193, 'fbs' :1, 'restecg': 1, 'thalach': 141, 'exang': 0, 'oldpeak':3.4, 'slope': 1, 'ca': 2, 'thal': 3 })

# 68,1,0,144,193,1,1,141,0,3.4,1,2,3,0
print("Traget Actual value is 0/No Heart Disease")

print(r.json())