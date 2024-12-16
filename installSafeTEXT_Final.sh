#!/bin/bash

# Script Instalasi SafeTEXT dengan Tampilan Halaman Akhir
echo "==========================================="
echo "          Menginstal SafeTEXT              "
echo "==========================================="

# 1. Update dan Instal Dependensi Dasar
echo "[1] Memperbarui sistem dan instal dependensi..."
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv tar wget xdg-utils -y

# 2. Mengekstrak File Arsip
echo "[2] Mengekstrak file SafeTEXT_Final.tar.gz..."
tar -xvf SafeTEXT_Final.tar.gz
cd SafeTEXT

# 3. Membuat Virtual Environment
echo "[3] Membuat virtual environment..."
python3 -m venv venv
source venv/bin/activate

# 4. Instalasi Library dari requirements.txt
echo "[4] Menginstal library dari requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

# 5. Menjalankan Program SafeTEXT
echo "[5] Menjalankan SafeTEXT.py..."
nohup python SafeTEXT.py > safetext.log 2>&1 &

# 6. Menunggu Program Berjalan dan Membuka Halaman
echo "[6] Membuka halaman SafeTEXT di browser..."
sleep 5  # Beri waktu 5 detik agar program siap
xdg-open http://localhost:5000  # Sesuaikan jika alamat berbeda

echo "==========================================="
echo "   Instalasi Selesai! SafeTEXT Siap Digunakan."
echo "==========================================="
