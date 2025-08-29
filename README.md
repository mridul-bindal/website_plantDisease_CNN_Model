<img width="789" height="915" alt="image" src="https://github.com/user-attachments/assets/f2aa5535-3aa5-47a4-a960-a2bdf7b467bf" />
Overview

Plant diseases are one of the biggest threats to agricultural productivity worldwide. Farmers often lack access to expert knowledge for early disease detection, leading to reduced crop yield and food insecurity.
The Plant Village Disease Checker is a web-based application that allows users to upload an image of a plant leaf and instantly receive predictions about whether the plant is healthy or diseased. If diseased, the system also identifies the specific disease.

This project integrates:

Frontend (React) → Provides a user-friendly interface for uploading leaf images.
Backend (Flask) → Processes the uploaded image and passes it to the trained model for prediction.
Deep Learning Model (Keras/TensorFlow) → Trained on the PlantVillage dataset a CNN with a accuracy of more than 95%

Features

Upload plant leaf images directly from the browser.
Get instant predictions on plant health.
Identify the exact disease if detected.
Simple and intuitive web interface.
Flask backend serving predictions from a trained Keras CNN model.

Tech Stack

Frontend
React.js
Axios (for API requests)
CSS (for styling)

Backend
Flask (Python)
TensorFlow / Keras (for ML model)
NumPy, Pillow (image preprocessing)

Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/mridul-bindal/plantVillage_disease_checker.git
cd plantVillage_disease_checker

2️⃣ Backend Setup (Flask)
Navigate to backend folder
cd backend

Create & activate virtual environment

Windows:

python -m venv venv
.\venv\Scripts\activate

(if you want to run these commands faster use uv)


Mac/Linux:

python3 -m venv venv
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Run backend server
python app.py


Backend will run on http://127.0.0.1:5000/

3️⃣ Frontend Setup (React)
Navigate to frontend folder

cd frontend
npm install
npm run dev

Frontend will run on http://localhost:5173/

4️⃣ Model File Setup

Since the trained model .keras file is large, it’s not uploaded to GitHub.
👉 You can train the model yourself using the provided Jupyter Notebook (plantVillage_disease_checker.ipynb) in the repo (Google Colab compatible), link is as follows 
https://github.com/mridul-bindal/plantVillage_disease_checker

👉 Save the trained model as model.h5 or model.keras and place it inside the backend/ folder.

How it Works

User uploads a plant leaf image on the React frontend.
Image is sent via API request to Flask backend.
Flask backend preprocesses the image and passes it to the Keras CNN model.
Model predicts if the plant is healthy or diseased.
Result is sent back and displayed on the frontend.

📊 Model Training
Dataset: PlantVillage Dataset
Framework: TensorFlow/Keras
Architecture: Convolutional Neural Network (CNN)

Accuracy: ~95% on validation set

🌍 Why This Project is Important
Early detection of plant diseases → prevents crop losses.
Helps farmers and agricultural researchers.
Affordable and scalable solution → works with just a smartphone camera.
Can be extended for mobile apps or offline edge device deployment.

🔮 Future Improvements
Deploy backend on cloud (AWS/GCP/Heroku).
Optimize model for mobile devices (TensorFlow Lite).
Support multiple languages for farmers.

Improve dataset size for better accuracy.

👨‍💻 Author

Mridul Bindal
📌 GitHub: mridul-bindal
