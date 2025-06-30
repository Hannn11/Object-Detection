import os, shutil
from ultralytics import YOLO
import cv2

# Pastikan YOLOv8 model diunduh atau dilatih terlebih dahulu
MODEL_PATH = "yolov8n.pt"  # Gunakan model pretrained dari YOLOv8
INPUT_FOLDER = "input_images"  # Folder untuk gambar input
OUTPUT_FOLDER = "output"  # Folder untuk menyimpan hasil

def detect_bottles():
    # Load model YOLOv8
    model = YOLO(MODEL_PATH)

    if os.path.exists(OUTPUT_FOLDER):
        shutil.rmtree(OUTPUT_FOLDER) #hapus folder output
        os.makedirs(OUTPUT_FOLDER)

    # Iterasi melalui semua gambar di folder input
    for image_name in os.listdir(INPUT_FOLDER):
        input_path = os.path.join(INPUT_FOLDER, image_name)
        output_path = os.path.join(OUTPUT_FOLDER, image_name)

        # Pastikan hanya file gambar yang diproses
        if not input_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        # Deteksi objek pada gambar
        results = model.predict(input_path, conf=0.5, save=False)

        # Simpan hasil deteksi ke file baru
        for result in results:
            filtered_boxes = []
            for box in result.boxes:
                class_id = int(box.cls)  # ID kelas deteksi
                if model.names[class_id] == "bottle": #cek hanya objek botol yang terdeteksi
                    filtered_boxes.append(box)
            # Jika tidak ada botol yang terdeteksi, lanjutkan ke gambar berikutnya
            if not filtered_boxes:
                print(f"Tidak ada botol terdeteksi di: {image_name}")
                continue

            annotated_image = result.plot(boxes=filtered_boxes)  # Gambar hasil deteksi
            cv2.imwrite(output_path, annotated_image)
            print(f"Hasil deteksi disimpan ke: {output_path}")

if __name__ == "__main__":
    detect_bottles()