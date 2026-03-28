# ⚽ Barcelona vs Real Madrid Player Detection
 
AI-powered player detection system using YOLOv8, deployed with Flask and Docker.
 
## Features
- Detects Barcelona and Real Madrid players in match images
- Real-time inference with YOLOv8 Nano
- Web interface for easy image upload
- Dockerized for easy deployment
 
## Model Details
- Architecture: YOLOv8 Nano
- Training: 50 epochs on 289 images
- Classes: Barcelona players, Real Madrid players
- Framework: Ultralytics
 
## Technologies
- **Backend:** Flask
- **ML Model:** YOLOv8 (Ultralytics)
- **Deployment:** Docker
- **Hosting:** Render
 
## Local Setup
 
### Prerequisites
- Python 3.11+
- Docker
 
### Run with Docker
```bash
docker build -t yolo-flask-app .
docker run -p 5000:5000 yolo-flask-app
```
 
Open browser: http://localhost:5000
 
## Live Demo
https://yolo-player-detection.onrender.com/
 
## Screenshot
<img width="480" height="388" alt="image" src="https://github.com/user-attachments/assets/236a5734-c830-4dcd-90d4-5f16570ed1ba" />
<img width="483" height="387" alt="image" src="https://github.com/user-attachments/assets/bbfd7d1d-a9c9-4801-b481-3e40d5e737cb" />




