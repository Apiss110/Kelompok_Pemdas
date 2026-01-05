data_sampah = {
    'organik' : {'jumlah_sampah' : 120, 'lokasi_pembuangan' : 'TPA Organik'},
    'anorganik' : {'jumlah_sampah' : 250, 'lokasi_pembuangan' : 'Pusat Daur Ulang'},
    'B3' : {'jumlah_sampah' : 60, 'lokasi_pembuangan' : 'Tempat Pengelolaan B3'}
}

jumlah_anorganik = data_sampah['anorganik']['jumlah_sampah']
lokasi_B3 = data_sampah['B3']['lokasi_pembuangan']
print(f"Jumlah sampah anorganik adalah: {jumlah_anorganik} kg, sedangkan lokasi pembuangan sampah B3 berada di {lokasi_B3}")

data_sampah['elektronik'] = {'jumlah_sampah' : 40, 'lokasi_pembuangan' : 'Pusat Pengelolaan Elektronik'}
#print(data_sampah)

data_sampah['organik']['jumlah_sampah'] = 130
#print(data_sampah)

for jenis, info in data_sampah.items():
    if info["jumlah_sampah"] > 100:
        print(f"Pengelolaan intensif diperlukan untuk {jenis}")
    else:
        print(f"{jenis} dalam batas aman")

