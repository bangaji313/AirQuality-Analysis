import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit.components.v1 import html

# Load Data
monthly_trend = pd.read_csv('monthly_trend.csv', index_col=0, parse_dates=True)
correlation_matrix = pd.read_csv('correlation_matrix.csv', index_col=0)

# Sidebar Navigation
st.sidebar.title("Air Quality Dashboard")
page = st.sidebar.radio("Go to", ["Tren Polutan", "Korelasi Polutan", "Geospatial Analysis", "Clustering Binning", "Interactive Filtering & Analysis"])

if page == "Tren Polutan":
    st.title("Tren Tingkat Polutan Sepanjang Tahun")
    selected_pollutant = st.selectbox("Pilih Polutan", ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3'])
    plt.figure(figsize=(10, 5))
    plt.plot(monthly_trend.index, monthly_trend[selected_pollutant], label=selected_pollutant)
    plt.xlabel("Waktu")
    plt.ylabel("Konsentrasi Polutan")
    plt.legend()
    st.pyplot(plt)

elif page == "Korelasi Polutan":
    st.title("Korelasi antara Polutan dan Faktor Cuaca")

    # Buat figure baru untuk plot
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Buat heatmap
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5, center=0, ax=ax)

    # Tambahkan garis batas pada korelasi kuat (misalnya di atas 0.5 atau di bawah -0.5)
    for i in range(len(correlation_matrix.columns)):
        for j in range(len(correlation_matrix.index)):
            value = correlation_matrix.iloc[i, j]
            if abs(value) > 0.5 and i != j:  # Abaikan korelasi dengan diri sendiri
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='black', lw=2))

    # Tampilkan plot di Streamlit
    st.pyplot(fig)

    # Tambahkan insight setelah heatmap
    st.markdown("""
    ## **Insight:**
    1. **Polutan PM2.5, PM10, NO2, dan CO memiliki korelasi positif yang tinggi satu sama lain.**  
       - _Hal ini menunjukkan bahwa polutan ini mungkin berasal dari sumber emisi yang sama, seperti kendaraan bermotor dan aktivitas industri._

    2. **Ozon (O3) menunjukkan korelasi positif dengan suhu (TEMP) sebesar 0.59.**  
       - _Ini sesuai dengan fenomena ilmiah bahwa ozon meningkat pada suhu yang lebih tinggi karena reaksi fotokimia yang lebih intens._  
       - _Artinya, di musim panas atau siang hari, kadar O3 cenderung meningkat._

    3. **Tekanan udara (PRES) memiliki korelasi negatif yang signifikan dengan polutan (-0.81 dengan suhu, -0.75 dengan kelembaban).**  
       - _Ketika tekanan udara tinggi, polutan cenderung berkurang, kemungkinan karena pergerakan massa udara yang lebih stabil._  
       - _Tekanan udara yang rendah bisa menyebabkan stagnasi udara, meningkatkan akumulasi polutan._

    4. **Kelembaban (DEWP) menunjukkan korelasi negatif dengan polutan utama seperti NO2 (-0.40) dan PM2.5 (-0.27).**  
       - _Kelembaban tinggi cenderung membantu proses deposisi polutan ke tanah atau air, mengurangi kadar polutan di udara._

    5. **Kecepatan angin (WSPM) berkorelasi negatif dengan beberapa polutan, terutama NO2 (-0.40) dan PM2.5 (-0.27).**  
       - _Ini menunjukkan bahwa angin berperan dalam menyebarkan polutan dan mengurangi konsentrasinya di lokasi tertentu._  
       - _Kecepatan angin yang lebih tinggi dapat membantu membersihkan udara dari polutan yang terkonsentrasi di daerah perkotaan._
    """)

elif page == "Geospatial Analysis":
    st.title("Visualisasi Peta Air Quality")

    # Menampilkan heatmap menggunakan komponen HTML
    st.components.v1.html(open('./heatmaps/Beijing_Air_Quality_HeatMap.html', 'r', encoding='utf-8').read(), height=600)

    # Tambahkan insight setelah heatmap
    st.markdown("""
    ## **Insight:**
    - 📍 **Stasiun-stasiun pemantauan kualitas udara tersebar di berbagai area Beijing**, mencakup wilayah urban (seperti Dongsi dan Tiantan) serta area pinggiran (seperti Huairou dan Shunyi).
    - 🏭 **Area seperti Dongsi dan Nongzhanguan yang berada di pusat kota Beijing** berpotensi memiliki **konsentrasi polutan yang lebih tinggi**, karena tingginya aktivitas manusia dan industri.
    - 🌿 **Stasiun di daerah seperti Changping dan Huairou yang terletak di pinggiran cenderung merekam polusi yang lebih rendah**, karena lebih jauh dari pusat aktivitas industri dan memiliki lebih banyak vegetasi.
    - 🔥 **Titik panas (hotspots) yang lebih terang menunjukkan area dengan konsentrasi polutan yang lebih tinggi** atau wilayah yang lebih sering dipantau.
    - 🗺️ **Heatmap ini menunjukkan cakupan pemantauan yang luas**, mencakup area urban, industri, serta wilayah hijau dan perbukitan di utara Beijing.
    """)

elif page == "Clustering Binning":
    st.title("Clustering Binning Polutan PM2.5")

    # Menampilkan heatmap menggunakan komponen HTML
    st.components.v1.html(open('./heatmaps/PM2.5_HeatMap_Binning.html', 'r', encoding='utf-8').read(), height=600)

    # Tambahkan insight setelah heatmap
    st.markdown("""
    ## **Insight:**
    - 🔴 **Titik merah yang intens menunjukkan konsentrasi PM2.5 yang tinggi** di pusat kota Beijing, yang kemungkinan besar dipengaruhi oleh aktivitas industri dan lalu lintas padat.
    - 🔵 **Area dengan warna biru yang lebih terang menunjukkan konsentrasi polusi yang lebih rendah**, yang cenderung berada di daerah pinggiran atau area dengan vegetasi yang lebih banyak.
    - 📍 **Beberapa hotspot yang jelas di berbagai lokasi menunjukkan adanya area dengan kualitas udara yang buruk**, yang bisa menjadi target untuk intervensi atau pengendalian polusi.
    - 🌿 **Area yang lebih hijau dan pegunungan di utara Beijing memiliki konsentrasi PM2.5 yang lebih rendah**, yang menunjukkan dampak positif dari lingkungan alami dalam mengurangi polusi udara.
    """)

elif page == "Interactive Filtering & Analysis":
    st.title("Analisis Interaktif")
    selected_pollutant = st.multiselect("Pilih Polutan untuk Analisis", ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3'], default=['PM2.5'])
    start_date = st.date_input("Pilih Tanggal Awal", monthly_trend.index.min().date())
    end_date = st.date_input("Pilih Tanggal Akhir", monthly_trend.index.max().date())

    filtered_data = monthly_trend.loc[start_date:end_date, selected_pollutant]
    st.line_chart(filtered_data)

    st.write("Statistik Deskriptif")
    st.write(filtered_data.describe())

# Additional Feature: Data Download
if st.sidebar.button("Download Data CSV"):
    csv_data = monthly_trend.to_csv().encode('utf-8')
    st.sidebar.download_button(label="Download Data CSV", data=csv_data, file_name='air_quality_data.csv', mime='text/csv')