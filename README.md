# Face Recognition
Tugas Project Based Learning IF 2024 Aljabar Linier 
<br />
Aplikasi Nilai Eigen dan EigenFace pada Pengenalan Wajah (Face Recognition) 

## Table of Contents
* [General Info](#general-information)
* [Tampilan Program](#tampilan-program)
* [How To Run](#how-to-run)
* [Tech Stack](#tech-stack)
* [Project Structure](#project-structure)
* [Credits](#credits)

## General Information
Teknologi pengenalan wajah (face recognition) sebagai salah satu bentuk biometrik yang sangat berguna untuk mengidentifikasi identitas seseorang, terutama dalam konteks keamanan. Teknologi ini bekerja dengan cara menyimpan sekumpulan gambar wajah di dalam sebuah basis data. Melalui gambar-gambar tersebut, sistem akan mempelajari pola dan struktur wajah, sehingga nantinya dapat mencocokkannya dengan gambar wajah lain yang ingin dikenali.

## Tampilan Program
![Main View](C:\Users\user\Documents\Face-Recognition\Face-Recognition-main\src\assets)

## How To Run
### Run Using Windows Batch File
#### Cara 1 (Manual check the dependencies)
1. Pastikan semua dependencies berikut sudah terinstall
pip install numpy          # Untuk operasi numerik
pip install opencv-python  # Untuk pengolahan citra & face recognition
pip install pillow         # Untuk manipulasi gambar
pip install streamlit      # Untuk membuat tampilan antarmuka (GUI)
2. Masuk ke direktori src
shell
Copy
Edit
cd src
3. Jalankan program dengan Streamlit
shell
Copy
Edit
streamlit run main.py
Jika berhasil, aplikasi akan terbuka secara otomatis di browser dengan URL seperti http://localhost:8501.

Tech Stack
Bahasa Pemrograman
Python 3.10.6

Library & Tools
Streamlit — Antarmuka pengguna berbasis web
OpenCV — Deteksi dan pengenalan wajah
Numpy — Operasi komputasi numerik
Pillow — Manipulasi gambar

Struktur Proyek
bash
Copy
Edit
.
│   README.md
│   requirements.txt
│   .gitignore
│
├───bin
│
├───doc
│
├───src
│   │   eigenface2.py
│   │   main.py         # File utama Streamlit
│   │
│   └───assets          # Menyimpan gambar, model, dll
│
└───test
Credits
This project is implemented by:

Brian Kheng (13521049)
Jimly Firdaus (13521102)
Marcel Ryan A. (13521127)
