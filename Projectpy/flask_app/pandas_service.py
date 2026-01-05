import pandas as pd
import os

# ======================================
# KONFIGURASI FILE
# ======================================
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
FILE_PATH = os.path.join(DATA_DIR, "jumlah_penderita_diabetes_jabar.csv")


# ======================================
# UTILITAS DASAR
# ======================================
def load_df():
    """
    Membaca file CSV menjadi DataFrame
    """
    return pd.read_csv(FILE_PATH)


def save_df(df):
    """
    Menyimpan DataFrame ke file CSV
    """
    df.to_csv(FILE_PATH, index=False)


# ======================================
# CRUD (WAJIB DARI DOSEN)
# ======================================
def get_all_data():
    """
    Mengambil seluruh data (untuk CRUD table)
    """
    return load_df().to_dict(orient="records")


def add_data(new_data: dict):
    """
    Menambahkan 1 baris data baru
    """
    df = load_df()
    df = pd.concat(
        [df, pd.DataFrame([new_data])],
        ignore_index=True
    )
    save_df(df)


def delete_data(index: int):
    """
    Menghapus data berdasarkan index baris
    """
    df = load_df()
    index = int(index)

    if 0 <= index < len(df):
        df = df.drop(index=index).reset_index(drop=True)

    save_df(df)


# ======================================
# SOAL A – PENGENALAN DATAFRAME
# ======================================
def soal_a():
    df = load_df()

    return {
        # 1. Menampilkan 5 baris pertama
        "a1_head_5_baris": df.head(),

        # 2. Menampilkan 5 baris terakhir
        "a2_tail_5_baris": df.tail(),

        # 3. Struktur dan tipe data
        # DIUBAH: supaya aman ditampilkan di HTML
        "a3_info_struktur": df.dtypes.astype(str),

        # 4. Statistik deskriptif
        "a4_statistik_deskriptif": df[
            ["jumlah_penderita_dm", "tahun"]
        ].describe(),

        # 5. Nilai unik tahun
        "a5_nilai_unik_tahun": sorted(df["tahun"].unique()),

        # 6. Nilai unik kabupaten & jumlahnya
        "a6_nilai_unik_kabupaten": df["nama_kabupaten_kota"].unique(),
        "a6_jumlah_kabupaten": df["nama_kabupaten_kota"].nunique(),

        # 7. Kolom terpilih
        "a7_kolom_terpilih": df[
            ["nama_kabupaten_kota", "jumlah_penderita_dm", "tahun"]
        ]
    }


# ======================================
# SOAL B – FILTERING & SORTING
# ======================================
def soal_b():
    df = load_df()

    data_2019 = df[df["tahun"] == 2019]

    return {
        # 8. Data tahun 2019
        "b8_data_tahun_2019": data_2019,

        # 9. Jumlah penderita > 100.000
        "b9_lebih_100k": df[df["jumlah_penderita_dm"] > 100000],

        # 10. Urut jumlah penderita (desc)
        "b10_sort_jumlah_desc": df.sort_values(
            by="jumlah_penderita_dm",
            ascending=False
        ),

        # 11. Urut tahun lalu jumlah
        "b11_sort_tahun_dan_jumlah": df.sort_values(
            by=["tahun", "jumlah_penderita_dm"],
            ascending=[True, False]
        ),

        # 12. Top 10 tahun 2019
        "b12_top10_2019": (
            data_2019
            .sort_values("jumlah_penderita_dm", ascending=False)
            .head(10)
        ),

        # 13. Data Kabupaten Bogor
        "b13_kabupaten_bogor": df[
            df["nama_kabupaten_kota"] == "KABUPATEN BOGOR"
        ]
    }


# ======================================
# SOAL C – AGREGASI & TRANSFORMASI
# ======================================
def soal_c():
    df = load_df()

    # 14. Total penderita per tahun
    c14_total_per_tahun = (
        df.groupby("tahun")["jumlah_penderita_dm"]
        .sum()
        .reset_index(name="total_jumlah_penderita_dm")
    )

    # 15. Rata-rata per kabupaten/kota
    c15_rata_per_kabupaten = (
        df.groupby("nama_kabupaten_kota")["jumlah_penderita_dm"]
        .mean()
        .reset_index(name="rata_rata_penderita_dm")
    )

    # 16. Kabupaten tertinggi & terendah
    total_per_kab = (
        df.groupby("nama_kabupaten_kota")["jumlah_penderita_dm"]
        .sum()
    )

    c16_kabupaten_tertinggi = total_per_kab.idxmax()
    c16_kabupaten_terendah = total_per_kab.idxmin()

    # 17. Kategori penderita DM
    df_kategori = df.copy()
    df_kategori["kategori_dm"] = df_kategori[
        "jumlah_penderita_dm"
    ].apply(
        lambda x: "Rendah" if x < 50000
        else "Sedang" if x < 100000
        else "Tinggi"
    )

    # 18. Persentase per tahun
    df_persen = df_kategori.copy()
    df_persen["persentase_tahun"] = (
        df_persen["jumlah_penderita_dm"]
        / df_persen.groupby("tahun")["jumlah_penderita_dm"].transform("sum")
        * 100
    )

    # 19. Tabel ringkas per tahun
    c19_tabel_ringkas = (
        df.groupby("tahun")
        .agg(
            total_jumlah_penderita_dm=("jumlah_penderita_dm", "sum"),
            jumlah_kabupaten_kota=("nama_kabupaten_kota", "count")
        )
        .reset_index()
    )

    return {
        "c14_total_per_tahun": c14_total_per_tahun,
        "c15_rata_per_kabupaten": c15_rata_per_kabupaten,
        "c16_kabupaten_tertinggi": c16_kabupaten_tertinggi,
        "c16_kabupaten_terendah": c16_kabupaten_terendah,
        "c17_data_dengan_kategori": df_kategori,
        "c18_data_dengan_persentase": df_persen,
        "c19_tabel_ringkas": c19_tabel_ringkas
    }
