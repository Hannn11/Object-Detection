import os

# Nama folder utama
project_dir = "yolo-dashboard"

# Struktur folder dan file
folders = ["input_images", "output"]
files = {
    "detect_objects.py": '''
import os
import shutil
import cv2
from ultralytics import YOLO

MODEL_PATH = "yolov8s.pt"
INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output"

def detect_all_objects():
    model = YOLO(MODEL_PATH)

    if os.path.exists(OUTPUT_FOLDER):
        shutil.rmtree(OUTPUT_FOLDER)
    os.makedirs(OUTPUT_FOLDER)

    for image_name in os.listdir(INPUT_FOLDER):
        input_path = os.path.join(INPUT_FOLDER, image_name)
        output_path = os.path.join(OUTPUT_FOLDER, image_name)

        if not input_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        results = model.predict(input_path, conf=0.5, save=False)

        for result in results:
            annotated_image = result.plot()
            cv2.imwrite(output_path, annotated_image)
            print(f"Hasil deteksi disimpan ke: {output_path}")

if __name__ == "__main__":
    detect_all_objects()
''',
    "dashboard.py": '''
import streamlit as st
import os
from PIL import Image

INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output"

st.set_page_config(page_title="YOLOv8 Object Detection", layout="wide")

st.title("📸 YOLOv8 Object Detection Dashboard")
st.markdown("Upload gambar ke sistem, jalankan deteksi objek, lalu lihat hasilnya!")

with st.sidebar:
    st.header("📤 Upload Gambar")
    uploaded_files = st.file_uploader("Pilih gambar", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

    if uploaded_files:
        os.makedirs(INPUT_FOLDER, exist_ok=True)
        for uploaded_file in uploaded_files:
            with open(os.path.join(INPUT_FOLDER, uploaded_file.name), "wb") as f:
                f.write(uploaded_file.getbuffer())
        st.success("✅ Gambar berhasil diunggah!")

    if st.button("🚀 Jalankan Deteksi"):
        with st.spinner("⏳ Deteksi objek sedang dijalankan..."):
            os.system("python detect_objects.py")
        st.success("🎉 Deteksi selesai!")

st.markdown("## 📂 Hasil Deteksi Gambar")
if os.path.exists(OUTPUT_FOLDER):
    image_files = [f for f in os.listdir(OUTPUT_FOLDER) if f.endswith(('.jpg', '.png', '.jpeg'))]
    if image_files:
        col1, col2 = st.columns(2)
        for idx, img_name in enumerate(image_files):
            img_path = os.path.join(OUTPUT_FOLDER, img_name)
            img = Image.open(img_path)
            with col1 if idx % 2 == 0 else col2:
                st.image(img, caption=img_name, use_column_width=True)
    else:
        st.info("Belum ada gambar hasil deteksi.")
else:
    st.info("Klik tombol 'Jalankan Deteksi' untuk melihat hasilnya.")
''',
    ".gitignore": '''
__pycache__/
*.pyc
output/
'''
}

# Buat folder utama
os.makedirs(project_dir, exist_ok=True)

# Buat subfolder
for folder in folders:
    os.makedirs(os.path.join(project_dir, folder), exist_ok=True)

# Tulis file
for filename, content in files.items():
    with open(os.path.join(project_dir, filename), "w", encoding="utf-8") as f:
        f.write(content.strip())
        print(f"[✓] File dibuat: {filename}")

print("\n[✔️] Proyek 'yolo-dashboard/' berhasil disiapkan.")
print("📌 Jalankan dashboard dengan: streamlit run dashboard.py")
