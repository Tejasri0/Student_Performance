from flask import Flask, render_template, request
import numpy as np
import pickle

# Load trained model
with open("MLR.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    try:
        values = [float(x) for x in request.form.values()]

        prediction = model.predict([values])[0]

        return render_template(
            'index.html',
            prediction_text=f"Predicted Performance Index = {prediction:.2f}"
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction_text=f"Error: {str(e)}"
        )

if __name__ == '__main__':
    app.run(debug=True)