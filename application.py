from flask import Flask, render_template, request
import pandas as pd
import config
import utils

df = pd.read_csv(config.CSV_PATH)

app = Flask(__name__)

@app.route('/')
def index():
    location = df['location'].unique()
    return render_template('index.html', locations = location)

@app.route('/predict', methods = ['POST'])
def predict():
    user_data = request.form

    HPP = utils.HousePricePrediction(user_data)
    prediction = HPP.get_prediction()
    return str(prediction)


if __name__ == '__main__':
    app.run('0.0.0.0', port= config.PORT_NUMBER)