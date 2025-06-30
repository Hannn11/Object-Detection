# 📸 Object Detection Dashboard

Object Detection Dashboard is a web-based application that allows users to upload images or videos, perform object detection automatically using the YOLOv8 model, and view the results visually on the dashboard.

## 🚀 Features

- 🖼️ Upload images (PNG, JPG, JPEG)

- 🎥 Upload videos (MP4, AVI, MOV, MPEG4)

- ⚙️ Run object detection on both images and videos

- 📦 View detection results directly on the dashboard

- 🎯 Powered by YOLOv8 for fast and accurate object detection

## 📁 Project Structure
├──app.py                  # Main application using Streamlit
├── detect.py               # Object detection logic using YOLOv8
├── requirements.txt        # Python dependencies
├── assets/                 # Optional UI icons
├── uploads/
│   ├── images/             # Uploaded image files
│   └── videos/             # Uploaded video files# 📸 Object Detection Dashboard

Object Detection Dashboard is a web-based application that allows users to upload images or videos, perform object detection automatically using the YOLOv8 model, and view the results visually on the dashboard.

## 🚀 Features

- 🖼️ Upload images (PNG, JPG, JPEG)

- 🎥 Upload videos (MP4, AVI, MOV, MPEG4)

- ⚙️ Run object detection on both images and videos

- 📦 View detection results directly on the dashboard

- 🎯 Powered by YOLOv8 for fast and accurate object detection

## 📁 Project Structure
├──app.py                  # Main application using Streamlit
├── detect.py               # Object detection logic using YOLOv8
├── requirements.txt        # Python dependencies
├── assets/                 # Optional UI icons
├── uploads/
│   ├── images/             # Uploaded image files
│   └── videos/             # Uploaded video files
├── outputs/
│   ├── images/             # Processed images with detections
│   └── videos/             # Processed videos with detections

## 📃 Requirements

Create a file named requirements.txt with the following:
- streamlit
- ultralytics
- opencv-python
- Pillow

install using:
``` 
pip install -r requirements.txt
```
## 📄 detect.py
This file handles image and video detection:
```
from ultralytics import YOLO
import cv2
import os

model = YOLO('yolov8n.pt')

def detect_image(image_path, output_path):
    results = model(image_path)
    for r in results:
        im_array = r.plot()
        cv2.imwrite(output_path, im_array)

def detect_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    width  = int(cap.get(3))
    height = int(cap.get(4))
    fps = cap.get(cv2.CAP_PROP_FPS)

    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        results = model(frame)
        annotated_frame = results[0].plot()
        out.write(annotated_frame)
    cap.release()
    out.release()
```

## 💻 How to Run

Clone the repository:
```
git clone https://github.com/Hannn11/object-detection-dashboard.git
```
```
cd yolo-dashboard
```
Create and activate a virtual environment (optional):
```
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
```
Install dependencies:
```
pip install -r requirements.txt
```
Run the application:
```
streamlit run dashboard.py
```
Open in browser:
```
Visit http://localhost:8501
```
## 🧠 Technologies Used

- Streamlit – to build the interactive dashboard

- Ultralytics YOLOv8 – for object detection

- Python (OpenCV, PIL, etc.)

## 📷 Sample Outputs

Image Detection Result:

Add a sample result like:
```
![Hasil](https://github.com/user-attachments/assets/6e42d5f1-d134-4a40-a68e-d6dc4bdb340a)
```

## 📌 Notes

- Maximum file size: 200MB per image/video

- For best results, use high-quality media with good lighting

- Outputs are automatically saved to the outputs/ folder

## 🙌 Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
