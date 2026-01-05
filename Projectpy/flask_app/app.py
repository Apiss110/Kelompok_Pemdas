from flask import Flask, render_template, request, redirect, url_for
import os

from pandas_service import (
    get_all_data,
    add_data,
    delete_data,
    soal_a,
    soal_b,
    soal_c
)

from analysis_service import (
    plot_bar_kabupaten_2019,
    plot_line_total_per_tahun,
    plot_barh_top10_2019,
    plot_pie_kategori_2019,
    plot_bar_3_tahun_terakhir
)

app = Flask(__name__)

# ===============================
# HOME
# ===============================
@app.route("/")
def index():
    return render_template("index.html")


# ===============================
# CRUD (WAJIB DOSEN)
# ===============================
@app.route("/crud")
def crud():
    data = get_all_data()
    return render_template("crud.html", data=data)


@app.route("/add", methods=["POST"])
def add():
    new_data = {
        "kode_provinsi": request.form["kode_provinsi"],
        "nama_provinsi": request.form["nama_provinsi"],
        "kode_kabupaten_kota": request.form["kode_kabupaten_kota"],
        "nama_kabupaten_kota": request.form["nama_kabupaten_kota"],
        "jumlah_penderita_dm": int(request.form["jumlah_penderita_dm"]),
        "satuan": request.form["satuan"],
        "tahun": int(request.form["tahun"])
    }
    add_data(new_data)
    return redirect(url_for("crud"))


@app.route("/delete/<int:index>")
def delete(index):
    delete_data(index)
    return redirect(url_for("crud"))


# ===============================
# SOAL A – C (PANDAS)
# ===============================
@app.route("/data")
def data():
    return render_template(
        "data.html",
        a=soal_a(),
        b=soal_b(),
        c=soal_c()
    )


# ===============================
# SOAL D (MATPLOTLIB → IMAGE)
# ===============================
@app.route("/grafik")
def grafik():
    plot_dir = os.path.join("static", "plots")
    os.makedirs(plot_dir, exist_ok=True)

    plot_bar_kabupaten_2019()
    plot_line_total_per_tahun()
    plot_barh_top10_2019()
    plot_pie_kategori_2019()
    plot_bar_3_tahun_terakhir()

    return render_template("grafik.html")


if __name__ == "__main__":
    app.run(debug=True)
