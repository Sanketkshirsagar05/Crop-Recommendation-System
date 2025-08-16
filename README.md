# Crop Recommendation System

## Overview
A web‑based machine learning application that predicts the most suitable crop to grow based on environmental and soil parameters (N, P, K, temperature, humidity, pH, rainfall).

## Features
- User‑friendly web interface (Flask)
- Pre‑trained ML model for crop prediction
- Inputs validated and scaled for consistent results

## Tech Stack
- Python, Flask
- scikit‑learn, NumPy, pandas
- HTML/CSS/JavaScript for the frontend
- Dataset from Kaggle or similar sources

## Installation
1. `git clone https://github.com/Sanketkshirsagar05/Crop-Recommendation-System.git`
2. `cd Crop-Recommendation-System`
3. `pip install -r requirements.txt`
4. `python app.py`
5. Open browser at `http://127.0.0.1:5000/`

## 🌍 Railway Deployment

You can deploy this project on **[Railway](https://railway.app/)** for free hosting:

1. Push your project to **GitHub**.  
2. Go to [Railway](https://railway.app/) and log in.  
3. Create a **New Project → Deploy from GitHub Repo**.  
4. Set the following configurations in Railway:  

   - **Build Command**:  
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command**:  
     ```bash
     gunicorn app:app --bind 0.0.0.0:8080
     ```
   - **Port**:  
     ```
     8080
     ```

5. Railway will auto-assign a domain.  
6. Visit the generated link to access your deployed app 🚀  

## Usage
Enter values for soil and climate parameters and receive a recommended crop based on the trained model.

## Project Structure
- `app.py` – Flask backend
- `models/` – pre-trained `model.pkl`, scalers, encoders
- `templates/` – HTML views
- `dataset/`, `python notebook/` – raw data or exploratory code

## Contributing
Feel free to open issues or pull requests to improve model accuracy or UI.
