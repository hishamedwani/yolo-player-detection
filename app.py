from flask import Flask, render_template, request, send_file
from ultralytics import YOLO
import cv2
import os
from werkzeug.utils import secure_filename
import numpy as np


app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

model = YOLO('best.pt')
print("model loaded successfully")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('index.html', error='no file uploaded')
    
    file = request.files['file']
    
    if file.filename == '':
        return render_template('index.html', error='no file selected')
    
    if file and allowed_file(file.filename):
        # save the image
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # detect players with yolo
        results = model(filepath)
        
        result = results[0]
        
        result_filename = 'result_' + filename
        result_path = os.path.join(app.config['RESULT_FOLDER'], result_filename)
        
        img = result.plot()
        cv2.imwrite(result_path, img)
        
        detections = []
        for box in result.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            cls_name = result.names[cls_id]
            detections.append({
                'class': cls_name,
                'confidence': f"{conf:.2%}"
            })
        
        # count how many players from rach team
        barca_count = sum(1 for d in detections if 'barcelona' in d['class'].lower())
        real_count = sum(1 for d in detections if 'real' in d['class'].lower() or 'madrid' in d['class'].lower())
        
        return render_template('result.html', 
                             result_image=result_filename,
                             detections=detections,
                             barca_count=barca_count,
                             real_count=real_count)
    
    return render_template('index.html', error='invalid file type')

@app.route('/results/<filename>')
def result_file(filename):
    return send_file(os.path.join(app.config['RESULT_FOLDER'], filename))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
