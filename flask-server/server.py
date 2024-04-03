# Backend (Flask)
from flask import Flask, request, jsonify
from flask_cors import CORS 
import cv2
import base64
import numpy as np
from ultralytics import YOLO

app = Flask(__name__)
model = YOLO('ShoeModel.pt')
CORS(app)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        image_data = request.form['image_data']
        # Remove the header from base64 string
        img_bytes = base64.b64decode(image_data.split(',')[1])
        img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)

        print(f"Received image with shape {img.shape}")

        # Perform model prediction
        results = model.predict(img)

        # Convert processed image to base64
        _, img_encoded = cv2.imencode('.jpg', results.imgs[0])
        img_base64 = base64.b64encode(img_encoded).decode()

        print(f"Processed image with shape {results.imgs[0].shape}")
        return jsonify({"image_data": img_base64})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)