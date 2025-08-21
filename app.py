from flask import Flask, render_template, request
import joblib
import numpy as np
from datetime import datetime  
import os

app = Flask(__name__)


with open(os.path.join('models', 'scaler.pkl'), 'rb') as f:
    scaler = joblib.load(f)

with open(os.path.join('models', 'crop_recommender.pkl'), 'rb') as f:
    model = joblib.load(f)

with open(os.path.join('models', 'label_encoder.pkl'), 'rb') as f:
    label_encoder = joblib.load(f)


prediction_history = []

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/predictor', methods=['GET', 'POST'])
def predictor():
    if request.method == 'POST':
        try:
            
            N = float(request.form['N'])
            P = float(request.form['P'])
            K = float(request.form['K'])
            temperature = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            ph = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])

            
            features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            scaled_features = scaler.transform(features)
            prediction_encoded = model.predict(scaled_features)[0]
            predicted_crop = label_encoder.inverse_transform([prediction_encoded])[0].capitalize()

            
            prediction_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            
            prediction_history.append({
                'date': prediction_time,
                'N': N,
                'P': P,
                'K': K,
                'temperature': temperature,
                'humidity': humidity,
                'ph': ph,
                'rainfall': rainfall,
                'crop': predicted_crop
                })

            

            return render_template('predictor.html', prediction=predicted_crop)

        except Exception as e:
            return render_template('predictor.html', error=str(e))

    return render_template('predictor.html', prediction=None)

@app.route('/history')
def history():
    return render_template('history.html', history=prediction_history)

@app.route('/crop_info')
def crop_info():
    return render_template('crop_info.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
