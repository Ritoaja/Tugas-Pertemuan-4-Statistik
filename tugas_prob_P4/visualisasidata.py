import pandas as pd
import matplotlib.pyplot as plt


# Tabel Data

path = "raihan.xlsx"

dataraw = pd.read_excel(
    path,
    header=6,
    usecols="B:H"
)

dataraw.columns = [
    "ID",
    "Name",
    "Kuis",
    "UTS",
    "UAS",
    "Nilai Akhir",
    "Nilai Huruf"
]

print("TABEL DATA")
print(dataraw)


# Tabel Frekuensi

datafrq = pd.crosstab(
    index=dataraw["Nilai Huruf"],
    columns="Frekuensi"
)

print("\nTABEL FREKUENSI")
print(datafrq)


# Grafik Garis

datafrq.plot(marker="o")

plt.title("Grafik Frekuensi Nilai Huruf")
plt.xlabel("Nilai Huruf")
plt.ylabel("Frekuensi")
plt.show()


# Grafik Batang

datafrq.plot(kind="bar")

plt.title("Grafik Batang Nilai Huruf")
plt.xlabel("Nilai Huruf")
plt.ylabel("Frekuensi")
plt.xticks(rotation=0)
plt.show()


# Pie Chart

datafrq.plot(
    kind="pie",
    y="Frekuensi",
    autopct="%1.0f%%",
    legend=False
)

plt.title("Persentase Nilai Huruf")
plt.ylabel("")
plt.show()


# Statistika Deskriptif

dataraw["Nilai Akhir"] = pd.to_numeric(
    dataraw["Nilai Akhir"],
    errors="coerce"
)

dt = dataraw["Nilai Akhir"]

stats = dt.describe()

stats["Standard Error"] = dt.sem()
stats["Median"] = dt.median()
stats["Mode"] = dt.mode().iloc[0]
stats["Variance"] = dt.var()
stats["Range"] = dt.max() - dt.min()
stats["Skewness"] = dt.skew()
stats["Kurtosis"] = dt.kurtosis()

print("\nSTATISTIKA DESKRIPTIF")
print(stats)