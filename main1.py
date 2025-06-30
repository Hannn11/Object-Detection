import os
import shutil
import cv2
from ultralytics import YOLO

# Konfigurasi
MODEL_PATH = "yolov8s.pt"  # Ganti dengan model yang lebih besar jika diperlukan
INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output"

def detect_all_objects():
    # Load model YOLOv8
    model = YOLO(MODEL_PATH)

    # Persiapan folder output
    if os.path.exists(OUTPUT_FOLDER):
        shutil.rmtree(OUTPUT_FOLDER)
    os.makedirs(OUTPUT_FOLDER)

    # Loop gambar di folder input
    for image_name in os.listdir(INPUT_FOLDER):
        input_path = os.path.join(INPUT_FOLDER, image_name)
        output_path = os.path.join(OUTPUT_FOLDER, image_name)

        # Proses hanya file gambar
        if not input_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        # Prediksi dengan YOLO
        results = model.predict(input_path, conf=0.5, save=False)  # Ubah threshold confidence jika perlu

        for result in results:
            # Plot hasil deteksi (dengan label dan box)
            annotated_image = result.plot()

            # Simpan hasil ke folder output
            cv2.imwrite(output_path, annotated_image)
            print(f"Hasil deteksi disimpan ke: {output_path}")

if __name__ == "__main__":
    detect_all_objects()
