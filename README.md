# Student Performance Prediction Using Machine Learning

## Project Overview

This project predicts a student's Performance Index using Machine Learning. A Linear Regression model is trained on student performance data and deployed using a Flask web application. Users can enter student details through a web interface and obtain a predicted performance score.

---

## Objective

The objective of this project is to:

* Analyze student performance data.
* Build a Linear Regression model.
* Evaluate model performance using regression metrics.
* Save the trained model using Pickle.
* Deploy the model using a Flask web application.

---

## Dataset Information

The dataset contains information related to student academic performance.

### Features

* Hours Studied
* Previous Scores
* Extracurricular Activities
* Sleep Hours
* Sample Question Papers Practiced

### Target Variable

* Performance Index

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Flask
* Pickle

---

## Project Structure

Student_Performance_Regression/

├── data/

│   └── Student_Performance.csv

├── templates/

│   └── index.html

├── model.pkl

├── app.py

├── requirements.txt

├── Student_Performance_Regression.ipynb

└── README.md

---

## Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the dataset.
2. Checked for missing values.
3. Analyzed data types.
4. Generated statistical summaries.
5. Performed exploratory data analysis.
6. Split the dataset into training and testing sets.

---

## Model Building

A Linear Regression model was used for prediction.

### Steps

1. Import Linear Regression.
2. Split data into training and testing sets.
3. Train the model.
4. Generate predictions.
5. Evaluate model performance.

---

## Evaluation Metrics

The model was evaluated using:

* R² Score
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

A high R² score and low RMSE indicate good model performance.

---

## Model Serialization

The trained model was saved using Pickle.

```python
import pickle

with open("MLR.pkl", "wb") as file:
    pickle.dump(model, file)
```

The saved model is loaded in the Flask application for making predictions.

---

## Flask Web Application

The Flask application provides a user-friendly interface where users can:

* Enter student details.
* Submit input values.
* Receive predicted Performance Index results.

---

## Installation Steps

### Clone Repository

```bash
git clone <repository_url>
```

### Navigate to Project Directory

```bash
cd Student_Performance_Regression
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open the browser and visit:

```text
http://127.0.0.1:5000
```

---

## Results

The Linear Regression model successfully predicts student performance based on academic and lifestyle factors.

The web application allows users to interact with the trained model and obtain predictions in real time.

---

## Future Enhancements

* Improve UI design.
* Compare multiple regression algorithms.
* Deploy the application on Render or Heroku.
* Add user authentication and database integration.

---
