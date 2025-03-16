import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit.components.v1 import html

# Load Data
monthly_trend = pd.read_csv('dashboard/monthly_trend.csv', index_col=0, parse_dates=True)
correlation_matrix = pd.read_csv('dashboard/correlation_matrix.csv', index_col=0)

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
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
    st.pyplot(plt)

elif page == "Geospatial Analysis":
    st.title("Visualisasi Peta Air Quality")
    st.components.v1.html(open('./dashboard/heatmaps/Beijing_Air_Quality_HeatMap.html', 'r', encoding='utf-8').read(), height=600)

elif page == "Clustering Binning":
    st.title("Clustering Binning Polutan PM2.5")
    st.components.v1.html(open('./dashboard/heatmaps/PM2.5_HeatMap_Binning.html', 'r', encoding='utf-8').read(), height=600)

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