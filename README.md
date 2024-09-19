# Heart Disease Prediction System
This repository contains a Heart Disease Prediction System built using machine learning algorithms. The system is designed to predict the presence of heart disease in patients based on several medical features. The project uses Random Forest, Logistic Regression, and ID3 algorithms for prediction, along with a preprocessing step to clean and prepare the data.

## Table of Contents
<a name="Project Overview"></a>
### Project Overview
<a name="Features"></a>
### Features
<a name="Dataset"></a>
### Dataset
<a name="Installation"></a>
### Installation
<a name="Usage"></a>
### Usage
<a name="Model Training"></a>
### Model Training
<a name="Results"></a>
### Results
<a name="Contributing"></a>
### Contributing
<a name="License"></a>
### License

# Project Overview
The Heart Disease Prediction System is a project aimed at predicting whether a patient is at risk of heart disease. By analyzing patient data such as age, sex, cholesterol levels, and other medical parameters, the system predicts the likelihood of heart disease using multiple machine learning algorithms.

# Features
*Data Preprocessing:* Cleans and prepares the dataset by handling missing values, encoding categorical data, and normalizing features.  
*Model Training:* Utilizes machine learning algorithms like Random Forest, Logistic Regression, and ID3 for classification.  
*Prediction:* Predicts the risk of heart disease based on the patient's medical data.  
*Evaluation:* Measures the accuracy and performance of different models using metrics such as accuracy, precision, recall, and F1-score.  

# Dataset
The dataset used for this project is sourced from the UCI Machine Learning Repository. It contains patient records with several medical features, such as:

*Age*  
*Sex*  
*Chest Pain Type*  
*Resting Blood Pressure*  
*Cholesterol Levels*  
*Fasting Blood Sugar*  
*Resting Electrocardiographic Results*  
*Maximum Heart Rate Achieved*  
*Exercise-Induced Angina*  
*Oldpeak*  
*Slope of Peak Exercise ST Segment*  
*Number of Major Vessels*  
*Thalassemia*  
*Presence/Absence of Heart Disease (target)*  

# Installation

## Clone the repository:
```git clone https://github.com/J-lakher/heart-disease-prediction-system```

## Navigate to the project directory:
```cd heart-disease-prediction```

## Install the required dependencies using pip:

``` pip install -r requirements.txt ```  
``` pip install django-crispy-forms ```  
``` pip install crispy-bootstrap5 ```  
``` pip install ipython ```  
``` pip install notebook ```  
``` pip install django-extensions ```  
``` pip install ipython ```  
```python -m pip install Pillow ```  

### Custom Data
You can modify the dataset in the data/ directory with your custom patient data for predictions.

### Model Training
This project uses multiple machine learning algorithms for prediction, including:
*Random Forest:* An ensemble method that creates multiple decision trees to improve the model's accuracy and robustness.  
*Logistic Regression:* A statistical method used for binary classification.  
*ID3:* A decision tree-based algorithm that uses information gain to split the dataset.  
The models are trained on the heart disease dataset and evaluated using cross-validation.

## Results
The system outputs the following metrics for each model:

*Accuracy*  
*Precision*  
*Recall*  
*F1-Score*  
The best-performing model based on the dataset was Random Forest, achieving an accuracy of 85% (replace with actual results).

# Contributing
Contributions are welcome! Please follow these steps:

Fork the repository
Create a new branch: ```git checkout -b feature-branch```  
Commit your changes: ```git commit -m 'Add new feature'```  
Push the branch: ```git push origin feature-branch```  
Open a pull request

# License
This project is licensed under the MIT License - see the LICENSE file for details.
