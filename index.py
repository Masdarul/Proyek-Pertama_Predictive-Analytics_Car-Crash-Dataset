    # -*- coding: utf-8 -*-
    """python

    ## **Proyek Pertama Machine Learning : Car Crash**
    *   **Nama: Masdarul Rizqi**
    *   **Email: m.rizqi1221@gmail.com**
    *   **ID Dicoding: masdarulrizqi**

    ###  **1.   Import**
    """

    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import calendar
    import zipfile
    import chardet
    from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
    from sklearn.mixture import GaussianMixture
    from sklearn.preprocessing import StandardScaler, LabelEncoder
    from sklearn.metrics import silhouette_score, calinski_harabasz_score
    from sklearn.model_selection import cross_val_score

    local_zip = './Data/Car Crash Dataset.zip'
    zip_ref = zipfile.ZipFile(local_zip, 'r')
    zip_ref.extractall('./Data')
    zip_ref.close()

    """### **2. Load Dataset**

    #### **2.1 Mengecek tipe encoding file**
    """

    df = "data/monroe county car crach 2003-2015.csv"
    rawdata = open(df, 'rb').read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']

    print(f"Encoding file adalah: {encoding}")

    """####  **2.2 Memanggil dataframe**"""

    df = pd.read_csv(df, delimiter=',', encoding='ISO-8859-1')
    df.head()

    """### **3. Data Understanding**
    Attribute  | Keterangan
    ------------- | -------------
    Year | merepresentasikan tahun kejadian tabrakan
    Month | merepresentasikan bulan kejadian tabrakan
    Day | merepresentasikan hari kejadian tabrakan
    Weekend? | merepresentasikan apakah tabrakan terjadi di akhir pekan atau bukan
    Hour | merepresentasikan jam kejadian tabrakan.       
    Collision Type | merepresentasikan jenis tabrakan
    Injury Type  | merepresentasikan jenis cedera
    Primary Factor |merepresentasikan faktor utama penyebab tabrakan
    Reported_Location |merepresentasikan lokasi kejadian tabrakan
    Latitude |merepresentasikan garis lintang lokasi kejadian
    Longitude |merepresentasikan garis bujur lokasi kejadian

    #### **3.1  mengecek semua hal tentang Data**
    """

    # Mengecek Deskripsi
    df.describe()

    # Mengecek Informasi
    df.info()

    # Mengecek dimensi dari data struktur
    df.shape

    # Mengecek jumlah baris data dari setiap nilai unik
    def show_value_counts(df, column):
        return df[column].value_counts().sort_index(ascending=False)

    result_year = show_value_counts(df, 'Year')
    result_month = show_value_counts(df, 'Month')
    result_day = show_value_counts(df, 'Day')
    result_weekend = show_value_counts(df, 'Weekend?')
    result_hour = show_value_counts(df, 'Hour')

    result_year

    result_month

    result_day

    result_weekend

    result_hour

    result_collision = show_value_counts(df, 'Collision Type')
    result_injury = show_value_counts(df, 'Injury Type')
    result_primary = show_value_counts(df, 'Primary Factor')
    result_rl = show_value_counts(df, 'Reported_Location')
    result_long = show_value_counts(df, 'Longitude')

    result_collision

    result_injury

    result_primary

    result_rl

    result_long

    """### **4. Visualisasi Data**

    #### **4.1 Visualisasi distribusi setiap atribut**
    """

    fig, axes = plt.subplots(nrows=4, figsize=(16, 16))

    # Distribusi Kecelakaan per Tahun
    df['Year'].value_counts().sort_index().plot(kind='bar', ax=axes[0])
    axes[0].set_title('Distribusi Kecelakaan per Tahun')
    axes[0].set_xlabel('Tahun')
    axes[0].set_ylabel('Jumlah Kecelakaan')

    # Distribusi Kecelakaan per Bulan
    months = df['Month'].value_counts().sort_index().index
    df['Month'].value_counts().sort_index().plot(kind='bar', ax=axes[1])
    axes[1].set_title('Distribusi Kecelakaan per Bulan')
    axes[1].set_xlabel('Bulan')
    axes[1].set_ylabel('Jumlah Kecelakaan')
    axes[1].set_xticks(range(0, 12))
    axes[1].set_xticklabels([calendar.month_abbr[i] for i in range(1, 13)])

    # Distribusi Kecelakaan per Hari
    bahasa = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    days = df['Day'].value_counts().sort_index().index
    df['Day'].value_counts().sort_index().plot(kind='bar', ax=axes[2])
    axes[2].set_title('Distribusi Kecelakaan per Hari')
    axes[2].set_xlabel('Hari')
    axes[2].set_ylabel('Jumlah Kecelakaan')
    axes[2].set_xticks(range(0, 7))
    axes[2].set_xticklabels(bahasa)

    # Distribusi Kecelakaan per Jam
    hours = df['Hour'].value_counts().sort_index().index
    df['Hour'].value_counts().sort_index().plot(kind='bar', ax=axes[3])
    axes[3].set_title('Distribusi Kecelakaan per Jam')
    axes[3].set_xlabel('Jam')
    axes[3].set_ylabel('Jumlah Kecelakaan')
    axes[3].set_xticks(range(24))
    axes[3].set_xticklabels([str(i) for i in range(1, 25)])

    # Adjust layout
    plt.tight_layout()

    # Show the combined plot
    plt.show()

    # Set up the figure and axes
    fig, axes = plt.subplots(nrows=2, figsize=(16, 8))

    # Distribusi Kecelakaan pada akhir minggu atau tidak
    sns.countplot(df['Weekend?'], ax=axes[0])
    axes[0].set_title('Distribusi Kecelakaan pada akhir minggu atau tidak')
    axes[0].set_xlabel('Jumlah Kecelakaan')
    axes[0].set_ylabel('Weekend?')

    # Distribusi Jenis Tabrakan
    sns.countplot(df['Collision Type'], ax=axes[1])
    axes[1].set_title('Distribusi Jenis Tabrakan')
    axes[1].set_xlabel('Jumlah Kecelakaan')
    axes[1].set_ylabel('Jenis Tabrakan')

    # Adjust layout
    plt.tight_layout()

    plt.figure(figsize=(14, 14))

    value_counts = df['Primary Factor'].value_counts().head(10)
    value_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)

    plt.title('Distribusi Faktor Utama Kecelakaan (Top 10)')
    plt.ylabel('')

    plt.figure(figsize=(14, 14))

    value_counts = df['Reported_Location'].value_counts().head(10)
    value_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)

    plt.title('Distribusi Lokasi Pelaporan Kecelakaan (Top 10)')
    plt.ylabel('')

    """### **5. Data Preparation**
    #### **5.1 Menghapus duplikasi**
    """

    df.drop_duplicates(inplace=True)

    """#### **5.2 Mengisi nilai missing value**"""

    df.isnull().sum()

    column = ['Weekend?', 'Hour', 'Collision Type', 'Primary Factor', 'Reported_Location', 'Latitude', 'Longitude']

    for nan in column:
        median = df[nan].mode()[0]
        df[nan].fillna(median, inplace=True)

    df.isnull().sum()

    """#### **5.3 Melakukan Subset Data, Encoding dan Scaling**"""

    data_subset = df[['Hour', 'Collision Type', 'Injury Type', 'Primary Factor']]
    data_subset = data_subset.sample(frac=0.6, random_state=42)

    label_encoder = LabelEncoder()
    data_encoded = data_subset.apply(label_encoder.fit_transform)

    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data_encoded)

    """### **6. Modeling**
    #### **6.1 Algoritma yang digunakan**
    """

    # Partitioning_Cluster (KMEANS Clustering)
    kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
    data_subset['Partitioning_Cluster'] = kmeans.fit_predict(data_scaled)

    # Hierarchical Clustering (Agglomerative Clustering)
    agg_cluster = AgglomerativeClustering(n_clusters=3)
    data_subset['Hierarchical_Cluster'] = agg_cluster.fit_predict(data_scaled)

    # Density-based Clustering (DBSCAN)
    dbscan = DBSCAN(eps=0.5, min_samples=20)
    data_subset['Density_Cluster'] = dbscan.fit_predict(data_scaled)

    # Model-based Clustering (Gaussian Mixture Model)
    gmm = GaussianMixture(n_components=3, random_state=42)
    data_subset['Model_Based_Cluster'] = gmm.fit_predict(data_scaled)

    print(f"{data_subset['Partitioning_Cluster'].value_counts()}\n")
    print(f"{data_subset['Hierarchical_Cluster'].value_counts()}\n")
    print(f"{data_subset['Model_Based_Cluster'].value_counts()}")

    data_subset['Density_Cluster'].value_counts()

    """#### **6.2 Visualisasi hasil modeling**"""

    cluster_columns = ['Partitioning_Cluster', 'Hierarchical_Cluster', 'Density_Cluster', 'Model_Based_Cluster']

    plt.figure(figsize=(15, 16))
    for i, column in enumerate(cluster_columns, 1):
        plt.subplot(4, 1, i)
        sns.countplot(data=data_subset, x=column, hue=column, palette='viridis', legend=False)
        plt.title(f'{column} Clustering')

    plt.tight_layout()
    plt.show()

    """#### **6.3 Metrik Evaluasi**"""

    # Fit and predict clusters
    data_subset['Partitioning_Cluster'] = kmeans.fit_predict(data_scaled)
    data_subset['Hierarchical_Cluster'] = agg_cluster.fit_predict(data_scaled)
    data_subset['Density_Cluster'] = dbscan.fit_predict(data_scaled)
    data_subset['Model_Based_Cluster'] = gmm.fit_predict(data_scaled)

    # Calculate Silhouette Score
    silhouette_scores = {
        'KMeans': silhouette_score(data_scaled, data_subset['Partitioning_Cluster']),
        'Agg_Cluster': silhouette_score(data_scaled, data_subset['Hierarchical_Cluster']),
        'DBSCAN': silhouette_score(data_scaled, data_subset['Density_Cluster']),
        'GMM': silhouette_score(data_scaled, data_subset['Model_Based_Cluster'])
    }

    # Calculate Calinski-Harabasz Index
    calinski_harabasz_scores = {
        'KMeans': calinski_harabasz_score(data_scaled, data_subset['Partitioning_Cluster']),
        'Agg_Cluster': calinski_harabasz_score(data_scaled, data_subset['Hierarchical_Cluster']),
        'DBSCAN': calinski_harabasz_score(data_scaled, data_subset['Density_Cluster']),
        'GMM': calinski_harabasz_score(data_scaled, data_subset['Model_Based_Cluster'])
    }

    # Display the results
    print("Silhouette Scores:")
    for algorithm, score in silhouette_scores.items():
        print(f"{algorithm}: {score:.4f}")

    print("\nCalinski-Harabasz Scores:")
    for algorithm, score in calinski_harabasz_scores.items():
        print(f"{algorithm}: {score:.4f}")

    """### **7. Tunning Model**"""

    inertia_values = []

    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, n_init=10, random_state=42)
        kmeans.fit(data_scaled)
        inertia_values.append(kmeans.inertia_)

    # Plot Elbow Method
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, 11), inertia_values, marker='o')
    plt.title('Elbow Method for Optimal K')
    plt.xlabel('Number of Clusters (K)')
    plt.ylabel('Inertia')
    plt.show()