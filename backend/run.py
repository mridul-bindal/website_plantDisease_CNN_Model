from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow import keras
import numpy as np
from PIL import Image
import os

app = Flask(__name__)
CORS(app)

# Folders
UPLOAD_FOLDER = "app/uploads"
MODEL_PATH = "app/models/plant_prediction_model.keras"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model
model = keras.models.load_model(MODEL_PATH)

# Hardcoded class names mapping
CLASS_NAMES = {
    "0": 'Apple___Apple_scab',
    "1": 'Apple___Black_rot',
    "2": 'Apple___Cedar_apple_rust',
    "3": 'Apple___healthy',
    "4": 'Blueberry___healthy',
    "5": 'Cherry_(including_sour)___Powdery_mildew',
    "6": 'Cherry_(including_sour)___healthy',
    "7": 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    "8": 'Corn_(maize)___Common_rust_',
    "9": 'Corn_(maize)___Northern_Leaf_Blight',
    "10": 'Corn_(maize)___healthy',
    "11": 'Grape___Black_rot',
    "12": 'Grape___Esca_(Black_Measles)',
    "13": 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    "14": 'Grape___healthy',
    "15": 'Orange___Haunglongbing_(Citrus_greening)',
    "16": 'Peach___Bacterial_spot',
    "17": 'Peach___healthy',
    "18": 'Pepper,_bell___Bacterial_spot',
    "19": 'Pepper,_bell___healthy',
    "20": 'Potato___Early_blight',
    "21": 'Potato___Late_blight',
    "22": 'Potato___healthy',
    "23": 'Raspberry___healthy',
    "24": 'Soybean___healthy',
    "25": 'Squash___Powdery_mildew',
    "26": 'Strawberry___Leaf_scorch',
    "27": 'Strawberry___healthy',
    "28": 'Tomato___Bacterial_spot',
    "29": 'Tomato___Early_blight',
    "30": 'Tomato___Late_blight',
    "31": 'Tomato___Leaf_Mold',
    "32": 'Tomato___Septoria_leaf_spot',
    "33": 'Tomato___Spider_mites Two-spotted_spider_mite',
    "34": 'Tomato___Target_Spot',
    "35": 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    "36": 'Tomato___Tomato_mosaic_virus',
    "37": 'Tomato___healthy'
}

# Test route
@app.route("/", methods=["GET"])
def home():
    return {"message": "Flask server is running 🚀"}

# Simple upload route (for testing)
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    filename = file.filename
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)
    
    print(f"New file uploaded: {filename}")
    return jsonify({"message": f"File {filename} uploaded successfully"})

# Upload & Predict route
@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    filename = file.filename
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)
    print(f"New file uploaded: {filename}")

    # Open and preprocess image
    img = Image.open(file_path).resize((224, 224))  # adjust to model input size
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

    # Run prediction
    preds = model.predict(img_array)
    predicted_index = int(np.argmax(preds, axis=1)[0])
    predicted_label = CLASS_NAMES[str(predicted_index)]
    confidence = float(np.max(preds))

    return jsonify({
        "predicted_class_index": predicted_index,
        "predicted_label": predicted_label,
        "confidence": confidence
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
