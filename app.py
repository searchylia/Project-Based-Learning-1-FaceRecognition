import streamlit as st
import tempfile
import os
import zipfile
import shutil
from PIL import Image
import time
import eigenface2
import main

from main import run

st.set_page_config(page_title="Face Recognition with Eigenfaces", layout="wide")
st.title("Face Recognition with PCA / Eigenfaces")

# 1. Upload Dataset
st.subheader("Upload Dataset Folder or ZIP File")
upload_type = st.radio("Input Type", ["Folder Path", "Upload ZIP"])
dataset_path = ""

if upload_type == "Folder Path":
    dataset_path = st.text_input("Enter full dataset folder path")
elif upload_type == "Upload ZIP":
    uploaded_zip = st.file_uploader("Upload a ZIP of face images", type="zip")
    if uploaded_zip is not None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            zip_path = os.path.join(tmp_dir, "faces.zip")
            with open(zip_path, "wb") as f:
                f.write(uploaded_zip.read())
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(tmp_dir)
                dataset_path = tmp_dir
            st.success("ZIP file extracted successfully")

# 2. Upload Test Image
st.subheader("Upload Test Image")
test_image = st.file_uploader("Choose an image to test", type=["jpg", "jpeg", "png"])

if test_image:
    st.image(test_image, caption="Uploaded Test Image", width=256)

# 3. Threshold Slider
st.subheader("Set Similarity Threshold")
threshold = st.slider("Threshold for recognition (%)", min_value=0, max_value=100, value=50)

# 4. Jalankan Face Recognition
if dataset_path and test_image:
    st.subheader("Run Face Recognition")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Run Recognition (With Threshold)", key="run_with_threshold"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_img:
                tmp_img.write(test_image.read())
                test_image_path = tmp_img.name

            start_time = time.time()
            result_path, similarity = run(dataset_path, test_image_path, threshold)
            end_time = time.time()
            exec_time = round(end_time - start_time, 3)

            st.success(f"Recognition complete in {exec_time} seconds")
            st.metric("Similarity", f"{similarity:.2f}%" if similarity > 0 else "No match")

            if os.path.exists(result_path):
                result_img = Image.open(result_path)
                st.image(result_img, caption="Most Similar Image", width=256)
            else:
                st.warning("No similar face found.")
