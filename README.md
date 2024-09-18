# Heart Disease Prediction System
This repository represents a Heart Disease Prediction System by implementing machine learning algorithms. The system predicts the presence of heart disease among patients based on several medical features of the patient. The project utilizes Random Forest, Logistic Regression, and ID3 algorithms for the prediction along with a preprocessing step to clean and prepare the data.

# Table of Contents
Project Overview
Features
Dataset
Installation
Usage
Model Training
Results
Contributing
License

# Project Overview
The Heart Disease Prediction System is a class of projects related to predicting possibilities for a patient to have heart disease. The system will make predictions in several ways using multiple machine learning algorithms for the estimation of possibilities based on various parameters such as age and sex of the patient, cholesterol level, among many others.

# Features
Data Preprocessing: Cleans and prepares the dataset by handling missing values, encoding categorical data, and normalizing features.
Model Training: It trains the models by the use of techniques such as Random Forest, Logistic Regression, and ID3. Prediction: It predicts the possibility of heart disease based on patient medical data. Evaluation: The performance of different models is determined by the use of accuracy, precision, recall, and F1-score metrics. Data Set The dataset used for this project is downloaded from the UCI Machine Learning Repository. It contains a set of patient records with various medical features. These include:

Age
Sex
Chest Pain Type
Resting Blood Pressure
Cholesterol Levels
Fasting Blood Sugar
Resting Electrocardiographic Results
Maximum Heart Rate Achieved
Exercise-Induced Angina
Oldpeak
Slope of Peak Exercise ST Segment
Number of Major Vessels
Thalassemia
Presence/Absence of Heart Disease (target)
Installation


# Clone the repository:
git clone https://github.com/J-lakher/heart-disease-prediction-system
# Navigate to the project directory:

cd heart-disease-prediction

# Install the required dependencies using pip:

pip install -r requirements.txt

# Usage
Preprocess the Data

You can pre-process the dataset by running the following script:

python preprocess_data.py

# Train the Model
The machine learning models can be trained by running the following command:

python train_model.py
# Make Predictions
You can use the already trained model to make predictions using the following:

python predict.py --input data/patient_data.csv

# Custom Data
You can replace the dataset in the data/ folder with your own custom patient data for making the prediction.

# Model Training
This repository trains various machine learning algorithms for prediction, including the following:

Random Forest: It is an ensemble method that grows several decision trees and delivers an average that increases the precision as well as stability of the model.
Logistic Regression: In this statistical approach, there are two values present for the target variable.
ID3 Decision Tree Algorithm: This uses information gain to split the data into subsets. The models will be trained using the heart disease dataset and evaluated using cross-validation.

# Results
The system outputs the following metrics for each model:

Accuracy
Precision
Recall
F1-Score
The best model performance for the dataset was Random Forest, which reached an accuracy of 80%.

# Contributing
Contributions are welcome! To contribute, please follow these steps:

# Fork the repository
Create a new branch: git checkout -b feature-branch
Commit: git commit -m 'Add new feature'
Push branch: git push origin feature-branch
Create a pull request

# License
This project is licensed under the MIT License - see the LICENSE file for details.