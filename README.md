# AirQuality-Analysis

## Identitas
- **Nama Lengkap**: Maulana Seno Aji Yudhantara  
- **Cohort ID**: MC117D5Y1789  
- **Mentor**: Yeftha Joshua Ezekiel  

## Deskripsi Proyek
AirQuality-Analysis adalah submission proyek analisis data yang berfokus pada pemantauan kualitas udara dengan menggunakan teknik analisis data dan visualisasi interaktif. Proyek ini bertujuan untuk menjawab dua pertanyaan bisnis utama:  
1. Bagaimana tren tingkat polutan (PM2.5, PM10, NO2, SO2, CO, O3) berubah sepanjang tahun?  
2. Bagaimana pola korelasi antara polutan udara (PM2.5, PM10, NO2, SO2, CO, O3) dengan faktor cuaca (Suhu, Tekanan Udara, Kelembaban, dan Kecepatan Angin), serta bagaimana pengaruhnya terhadap konsentrasi polutan?  

## Fitur
- ✅ Visualisasi data tren polutan  
- ✅ Heatmap Geospasial  
- ✅ Dashboard interaktif dengan Streamlit  
- ✅ Analisis korelasi polutan dan faktor lingkungan 

## Cara Menjalankan
1. **Clone Repository**
   ```bash
   git clone https://github.com/bangaji313/AirQuality-Analysis.git
   ```
   **Masuk ke Folder Proyek**
   ```bash
   cd AirQuality-Analysis/dashboard
   ```
2. **Install dependensi**
   ```bash
   pip install -r ../requirements.txt
   ```
3. **Jalankan Aplikasi**
   ```bash
   streamlit run dashboard.py
   ```

## Hasil Analisis
- 📈 Tren Bulanan Polutan: Visualisasi tren dari berbagai polutan selama satu tahun penuh
- 🔥 Korelasi Faktor Lingkungan: Hubungan antara polutan dan variabel lingkungan seperti suhu, kelembaban, dan kecepatan angin
- 🌐 Heatmap Geospasial: Distribusi polutan di berbagai wilayah Beijing
