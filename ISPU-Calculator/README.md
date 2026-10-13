# Kalkulator ISPU (Indeks Standar Pencemar Udara) & Analisis Kualitas Udara

Program Python untuk menghitung Indeks Standar Pencemar Udara (ISPU) berdasarkan data konsentrasi nyata polutan udara, mengacu pada standar regulasi lingkungan di Indonesia.

## 📋 Fitur Utama
1. **Perhitungan ISPU Otomatis**: Mengonversi nilai konsentrasi nyata berbagai parameter polutan ke dalam skala nilai ISPU menggunakan metode interpolasi linier.
2. **Penentuan Kategori Kualitas Udara**: Mengidentifikasi status mutu udara wilayah (mulai dari *Baik*, *Sedang*, *Tidak Sehat*, *Sangat Tidak Sehat*, hingga *Berbahaya*) diambil dari nilai ISPU tertinggi.
3. **Identifikasi Polutan Ekstrem**: Otomatis mendeteksi parameter pencemar utama terbesar dan terkecil di area tersebut.

## 📊 Parameter Polutan yang Dianalisis
* **$PM_{2.5}$** (Partikulat halus)
* **$PM_{10}$** (Partikulat kasar)
* **$SO_{2}$** (Sulfur Dioksida)
* **$CO$** (Karbon Monoksida)
* **$NO_{2}$** (Nitrogen Dioksida)
* **$O_{3}$** (Ozon)

## 🚀 Cara Menjalankan Program
Pastikan Python sudah terinstal di perangkatmu, lalu jalankan perintah berikut di terminal atau CMD:

```bash
python main_2.py
