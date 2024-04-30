import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pickle

df = pd.read_csv('Data Cleaned.csv')
df1 = pd.read_csv('FMC Marnaik Periode 13 - 24 Mei 2023.csv')
df2 = pd.read_csv('Data Cleaned Predict.csv')

def load_df():
    df = pd.read_csv("Data Cleaned.csv")
    return df

def load_df1():
    df1 = pd.read_csv("FMC Marnaik Periode 13 - 24 Mei 2023.csv")
    return df1

def load_df2():
    df2 = pd.read_csv("Data Cleaned Predict.csv")
    return df2

def hist_plot(df1):
    fig, ax = plt.subplots(figsize=(10, 6))  
    sns.histplot(df1['Fuel Tank Stock After'].dropna(), bins=20, kde=True, ax=ax) 
    ax.set_title('Normalisasi Penggunaan Bahan Bakar')
    ax.set_xlabel("Fuel Tank Stock After")
    ax.set_ylabel('Frequency')
    st.pyplot(fig)  
    text = """
    Interpretasi:
    Grafik batang menunjukkan normalisasi penggunaan bahan bakar dengan start ME (Mengoperasikan Mesin) dalam rentang 600 hingga 1000. Terdapat peningkatan yang signifikan dalam penggunaan bahan bakar saat start ME mendekati nilai 1000, dengan nilai tertinggi mencapai sekitar 14 STOP ME.

    Insight:
    Peningkatan signifikan dalam penggunaan bahan bakar saat start ME mendekati nilai 1000 menunjukkan adanya korelasi antara start ME dan penggunaan bahan bakar. Grafik juga menunjukkan adanya pola kurva yang menurun setelah mencapai puncak, yang mungkin mengindikasikan bahwa penggunaan bahan bakar akan menurun setelah mencapai nilai start ME tertinggi.

    Actionable Insight:
    Berdasarkan insight ini, mungkin perlu untuk memperhatikan penggunaan bahan bakar saat start ME mendekati nilai 1000 dan mencari cara untuk
    mengoptimalkan efisiensi penggunaan bahan bakar pada titik ini. Ini dapat dilakukan melalui penyesuaian teknis atau strategi operasional yang lebih efisien untuk mengurangi konsumsi bahan bakar dan menghemat biaya operasional.
    """
    st.write(text)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='Fuel Daily Consumption', y='Opening Fuel Tank Sounding', data=df, ax=ax)
    ax.set_xlabel('Fuel Daily Consumption')
    ax.set_ylabel('Opening Fuel Tank Sounding')
    ax.set_title('Tingkat Efisiensi Bahan Bakar Harian Pada Kapal FMC Marnik')
    st.pyplot(fig)
    text = """
    Interpretasi:
    Grafik ini menunjukkan hubungan antara tingkat konsumsi bahan bakar harian dengan volume awal bahan bakar di dalam tangki pada Kapal FMC Marnik. Garis yang dihasilkan memberikan gambaran visual tentang bagaimana perubahan dalam konsumsi bahan bakar harian berdampak pada volume bahan bakar yang tersedia di tangki sebelum kapal berlayar.

    Insight:
    Grafik menunjukkan tren umum bahwa semakin tinggi tingkat konsumsi bahan bakar harian, semakin rendah volume awal bahan bakar di dalam tangki. Hal ini dapat diinterpretasikan sebagai indikasi bahwa tingkat konsumsi bahan bakar harian memiliki hubungan negatif dengan volume bahan bakar yang tersedia di tangki sebelum berlayar.

    Actionable Insight:
    Berbagai strategi dapat dipertimbangkan untuk meningkatkan efisiensi penggunaan bahan bakar, seperti:

    1. Menganalisis faktor-faktor yang mempengaruhi tingkat konsumsi bahan bakar harian dan mencari cara untuk menguranginya.
    2. Mengoptimalkan pengisian bahan bakar sebelum berlayar berdasarkan proyeksi konsumsi bahan bakar harian, sehingga volume bahan bakar yang tersedia di tangki dapat lebih terjaga.
    3. Menjaga konservasi bahan bakar selama perjalanan untuk memaksimalkan penggunaan bahan bakar yang tersedia dan mengurangi kebutuhan pengisian ulang di tengah perjalanan.
    """
    st.write(text)

    plt.figure(figsize=(8, 6))
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(df['Closing Fuel Tank Sounding'].dropna(), bins=20, ax=ax)
    ax.set_title('Distribusi Volume Bahan Bakar Setelah Perjalanan Selesai')
    ax.set_xlabel('Volume Bahan Bakar Setelah Perjalanan Selesai')
    ax.set_ylabel('Frekuensi')
    st.pyplot(fig)
    text = """
    Interpretasi:
    Histogram menunjukkan distribusi frekuensi volume bahan bakar setelah perjalanan selesai, dengan tiap batang histogram merepresentasikan seberapa sering volume bahan bakar jatuh dalam rentang tertentu. Ini memberikan gambaran tentang seberapa umum berbagai volume bahan bakar ditemukan dalam tangki setelah kapal mencapai tujuan.

    Insight:
    Distribusi volume bahan bakar setelah perjalanan selesai memberikan pemahaman tentang seberapa sering kapal mencapai tujuan dengan volume bahan bakar tertentu. Pola distribusi ini dapat memberikan wawasan tentang seberapa efisien pengelolaan bahan bakar selama perjalanan dan apakah perlu dilakukan penyesuaian untuk meningkatkan efisiensi penggunaan bahan bakar.

    Actionable Insight:
    Distribusi volume bahan bakar setelah perjalanan selesai dapat memberikan wawasan tentang keefektifan manajemen bahan bakar selama perjalanan. Jika terdapat pola yang menunjukkan bahwa sebagian besar pengukuran berada pada volume bahan bakar yang rendah, hal ini bisa mengindikasikan bahwa kapal sering mencapai tujuan dengan sisa bahan bakar yang minim. Sebagai tindak lanjut, perusahaan dapat mempertimbangkan strategi untuk meningkatkan efisiensi penggunaan bahan bakar, seperti melakukan pengisian bahan bakar yang lebih sering atau melakukan evaluasi terhadap kebutuhan bahan bakar selama perjalanan.
    """
    st.write(text)

    st.set_option('deprecation.showPyplotGlobalUse', False)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(df['Fuel Tank Stock After'].dropna(), bins=20, kde=True, ax=ax)
    ax.set_title('Normalisasi Penggunaan Bahan Bakar')
    ax.set_xlabel("Start ME")
    ax.set_ylabel('Stop ME')
    st.pyplot(fig)
    text = """
    Interpretasi:
    Visualisasi histogram ini memberikan gambaran tentang sebaran stok bahan bakar setelah penggunaan pada Kapal FMC Marnaik selama periode 13-24 Mei 2023. Histogram tersebut menunjukkan seberapa sering stok bahan bakar mencapai level tertentu setelah digunakan dalam suatu periode.

    Insight:
    Dari histogram, terlihat bahwa sebagian besar stok bahan bakar setelah penggunaan berada pada level yang relatif tinggi, dengan sedikit observasi yang mencapai level rendah. Hal ini menunjukkan bahwa mesin mungkin tidak dijalankan sampai habis bahan bakarnya secara konsisten, dan ada upaya untuk mempertahankan tingkat stok yang cukup tinggi setelah penggunaan.

    Actionable Insight:
    Berdasarkan insight tersebut, ada beberapa langkah yang dapat diambil untuk meningkatkan efisiensi penggunaan bahan bakar dan manajemen stok, salah satunya evaluasi dan perbaiki keefektifan proses penggunaan bahan bakar saat mesin berjalan, mungkin dengan mengatur kebiasaan penggunaan bahan bakar atau mengoptimalkan proses pembakaran.
    """
    st.write(text)

    plt.figure(figsize=(10, 6))
    sns.countplot(x='To', data=df, palette='Set2')
    plt.title('Volume Bahan Bakar Perjalanan Kapal FMC Marnaik ke Destinasi Tujuan')
    plt.xlabel('To')
    plt.ylabel('Closing Fuel Tank Sounding')
    st.pyplot()
    text = """
    Interpretasi:
    Grafik yang diberikan menampilkan volume bahan bakar yang dikonsumsi oleh Kapal FMC Marnaik selama perjalanan menuju tujuan. Setiap batang pada grafik mewakili tahap tertentu dalam perjalanan, dengan sumbu x menunjukkan tahapan dan sumbu y menunjukkan konsumsi bahan bakar untuk setiap tahap.

    Insight:
    Grafik ini memberikan wawasan tentang seberapa besar bahan bakar yang dikonsumsi oleh kapal pada setiap tahapan perjalanan. Ini membantu dalam pemahaman pola penggunaan bahan bakar kapal dan memungkinkan pengamat untuk melihat apakah ada tahapan tertentu yang memerlukan perhatian lebih lanjut dalam hal efisiensi bahan bakar.

    Actionable Insight:
    Dengan memperhatikan pola penggunaan bahan bakar yang tergambar dalam grafik, langkah-langkah tertentu dapat diambil untuk meningkatkan efisiensi bahan bakar kapal. Misalnya, jika terdapat tahapan perjalanan di mana konsumsi bahan bakar lebih tinggi dari yang diharapkan, langkah-langkah perbaikan seperti penyesuaian rute, manajemen kecepatan, atau perbaikan mesin dapat dipertimbangkan untuk mengurangi konsumsi bahan bakar dan meningkatkan efisiensi perjalanan kapal.
    """
    st.write(text)


def plot_custom_correlation(df1):
    selected_columns = ['Fuel Tank Stock After', 'Fuel Daily Consumption', 'Opening Fuel Tank Sounding', 'Closing Fuel Tank Sounding']

    selected_df = df1[selected_columns]

    corr_matrix = selected_df.corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    st.pyplot(fig)

    text = """
    Interpretasi:
    Heatmap ini memvisualisasikan korelasi antara variabel-variabel terkait penggunaan bahan bakar pada Kapal FMC Marnaik untuk periode 13-24 Mei 2023. Warna merah menunjukkan korelasi positif yang kuat, sementara warna biru menunjukkan korelasi negatif yang kuat. Warna netral menunjukkan hubungan yang lemah atau tidak signifikan antara variabel.

    Insight:
    Dari heatmap, terlihat bahwa beberapa variabel terkait penggunaan bahan bakar memiliki korelasi yang kuat, terutama pada beberapa pasangan variabel. Korelasi yang kuat ini dapat memberikan wawasan tentang bagaimana variabel-variabel tersebut saling memengaruhi dalam konteks penggunaan bahan bakar di kapal.

    Actionable Insight:
    Berdasarkan korelasi yang terlihat, pihak terkait dapat mengambil tindakan untuk mengoptimalkan penggunaan bahan bakar. Misalnya, jika terdapat korelasi negatif yang kuat antara dua variabel, mereka dapat mempertimbangkan strategi untuk mengurangi dampak negatif tersebut. Selain itu, mereka dapat menggunakan informasi korelasi positif untuk mengembangkan strategi efisiensi bahan bakar yang lebih baik.
    """
    st.write(text)


def compositionAndComparison(df):
    # Hitung rata-rata fitur untuk setiap kelas
    df['Fuel Capacity'].replace({0: 'low', 1: 'high'}, inplace=True)
    class_composition = df.groupby('Fuel Capacity').mean()
    
    plt.figure(figsize=(10, 6))
    sns.heatmap(class_composition.T, annot=True, cmap='YlGnBu', fmt='.2f')
    plt.title('Composition for each class')
    plt.xlabel('Class')
    plt.ylabel('Feature')
    st.pyplot(plt)
    text = """
    Interpretasi:
    Heatmap ini memvisualisasikan rata-rata nilai fitur untuk setiap kategori kapasitas bahan bakar pada Kapal FMC Marnaik untuk periode 13-24 Mei 2023. Warna gelap menunjukkan nilai tinggi, sedangkan warna terang menunjukkan nilai rendah.

    Insight:
    Rata-rata nilai fitur seperti Fuel Tank Stock After dan Closing Fuel Tank Sounding cenderung lebih tinggi pada kapal dengan kapasitas bahan bakar 'high' daripada 'low'.

    Actionable Insight:
    Pertimbangkan strategi manajemen bahan bakar yang lebih efisien untuk kapal-kapal dengan kapasitas bahan bakar tinggi, seperti pengisian bahan bakar yang lebih sering atau kapasitas tangki yang lebih besar.
    """
    st.write(text)

    from_counts = df1['From'].value_counts()
    plt.figure(figsize=(8, 8))
    from_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'lightcoral'])
    plt.title('Distribution of "From" Categories')
    plt.ylabel('')
    st.pyplot(plt)
    text = """
    Interpretasi:
    Pie chart tersebut memvisualisasikan persentase penggunaan tempat awal sebelum berlayar oleh Kapal FMC Marnaik, yang diukur dalam interval harian. Setiap sektor dalam pie chart mewakili proporsi penggunaan tempat oleh masing-masing kategori.

    Insight:
    Dari pie chart, dapat dilihat bahwa mayoritas penggunaan tempat awal sebelum berlayar terbagi antara tiga kategori utama: PSTB, Somber, dan Running ME/Stand by. Ketiganya memiliki persentase yang hampir seimbang, dengan PSTB mendominasi dengan 34.6%, diikuti oleh Somber dan Running ME/Stand by, masing-masing 32.4%. Sementara itu, Jetty Bunker memiliki kontribusi yang relatif kecil dengan hanya 0.7%.

    Actionable Insight:
    Optimalkan penggunaan tempat awal sebelum berlayar dengan mempertimbangkan peningkatan efisiensi operasional dan evaluasi terhadap penggunaan Jetty Bunker.
    """
    st.write(text)

def predict(df2):
    def display_category_table():
        # Membuat DataFrame untuk tabel penjelasan
        category_data = {
            'Kategori': ['PSTB', 'SOMBER', 'Running ME/Stand by'],
            'Kode': [0, 1, 2]
        }
        category_df = pd.DataFrame(category_data)

        # Menampilkan tabel penjelasan di Streamlit
        st.write("Tabel Penjelasan Kategori:")
        st.write(category_df.set_index('Kategori'))

    display_category_table()

    selected_options = st.selectbox('From:', df2['From'].unique())
    selected_options1 = st.selectbox('To:', df2['To'].unique())
    selected_options2 = st.slider('Fuel Daily Consumption:', 0.0, 100.0)
    selected_options3 = st.slider('Opening Fuel Tank Sounding:', 0.0, 50.0)
    selected_options4 = st.slider('Closing Fuel Tank Sounding:', 0.0, 50.0)
    selected_options5 = st.slider('Fuel Tank Stock After:', 0.0, 1000.0)
    selected_date = st.selectbox('Date:', df2['Date'].unique())

    value = [selected_options, selected_options1, selected_options2, selected_options3, selected_options4, selected_options5]

    index_options = {
        'From': selected_options,
        'To': selected_options1,
        'Date': selected_date,
    }

    data_selected = pd.DataFrame({
        'From': [index_options['From']],
        'To': [index_options['To']],
        'Fuel Daily Consumption': [selected_options2],
        'Opening Fuel Tank Sounding': [selected_options3],
        'Closing Fuel Tank Sounding': [selected_options4],
        'Fuel Tank Stock After': [selected_options5],
        'Date': [index_options['Date']]
    })


    st.write("Features selected:")
    st.write(data_selected)

    button = st.button('Predict')

    if button:
        with open('gnb.pkl', 'rb') as file:
            loaded_model = pickle.load(file)

        predicted = loaded_model.predict(data_selected)

        if predicted[0] == 0:
            msg = 'Bahan bakar Kapal FMC Marnaik hampir habis'
        else:
            msg = 'Bahan bakar Kapal FMC Marnaik masih cukup terpenuhi'

        st.success(msg)