import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
from streamlit_option_menu import *
from option import *

df = pd.read_csv('Data Cleaned.csv')
df1 = pd.read_csv('FMC Marnaik Periode 13 - 24 Mei 2023.csv')
df2 = pd.read_csv('Data Cleaned Predict.csv')

def main():
    menu = st.sidebar.selectbox("", ["Beranda", "Distribusi", "Hubungan", "Perbandingan dan Komposisi", "Predict"])
    
    if menu == "Beranda":
        st.title("Analisis Komprehensif dan Perancangan Website untuk Periode 13-24 Mei 2023 pada Kapal FMC Marnaik")
        st.subheader("Penggunaan Bahan Bakar Setiap Harinya untuk Mengenali Pola Konsumsi Kapal FMC Marnaik")
        st.write("Memantau penggunaan bahan bakar setiap harinya untuk mengelola penggunaan bahan bakar dengan efisien, mengenali pola konsumsi, dan memastikan penggunaan yang terbaik selama perjalanan.")
        st.image("image/kapal1.jpg", use_column_width=True)
        
        st.subheader("Perjalanan Kapal FMC Marnaik untuk Melacak Jadwal Perjalanan")
        st.write("Memantau perjalanan kapal untuk memberikan pemahaman tentang kegiatan perjalanan sehari-hari, termasuk tanggal perjalanan, rute dari pelabuhan PSTB ke Somber, serta waktu keberangkatan dan kedatangan (main engine), dengan tujuan melacak jadwal perjalanan dan mengenali pola perjalanan yang memengaruhi penggunaan bahan bakar.")
        st.image("image/kapal2.jpg", use_column_width=True)

        st.subheader("Pemantauan Sisa Bahan Bakar Kapal FMC Marnaik yang Tersedia")
        st.write("Mengelola stok bahan bakar kapal dengan memantau data bunker (sisa bahan bakar yang tersedia), dengan tujuan merencanakan pengisian ulang bahan bakar dan menghindari kekosongan selama perjalanan.")
        st.image("image/kapal3.png", use_column_width=True)

        st.subheader("Pemantauan Tingkat Bahan Bakar Kapal FMC Marnaik dalam Tangki")
        st.write("Memantau tingkat bahan bakar dalam tangki kapal setiap harinya (fuel tank sounding) untuk memperkirakan konsumsi bahan bakar selama perjalanan, mencegah kekurangan bahan bakar di tengah perjalanan, dan merencanakan pengisian ulang bahan bakar dengan tepat.")
        st.image("image/kapal4.jpg", use_column_width=True)

    elif menu == "Distribusi":
        st.markdown("<h1 style='text-align: center;'>Data Distribusi</h1>", unsafe_allow_html=True)
        df1 = load_df1()
        hist_plot(df1)

    elif menu == "Hubungan":
        st.markdown("<h1 style='text-align: center;'>Hubungan</h1>", unsafe_allow_html=True)
        df1 = load_df1()
        plot_custom_correlation(df1)
    
    elif menu == "Perbandingan dan Komposisi":
        st.markdown("<h1 style='text-align: center;'>Perbandingan dan Komposisi</h1>", unsafe_allow_html=True)
        compositionAndComparison(df)
    
    elif menu == "Predict":
        st.markdown("<h1 style='text-align: center;'>Predict</h1>", unsafe_allow_html=True)
        df2 = load_df2()
        predict(df2)    

if __name__ == '__main__':
    main()