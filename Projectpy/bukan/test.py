nilai_murid = {
	'murid1' : {
		'Nama' : 'Alice',
		'Usia' : 20,
		'Nilai' : {
			'matematika' : 88,
			'sains' : 92,
			'bahasa_inggris' : 85
		}
	},
	'murid2' : {
		'Nama' : 'Bob',
		'Usia' : 22,
		'Nilai' : {
			'matematika' : 78,
			'sains' : 85,
			'bahasa_inggris' : 80
		}
	},
	'murid3' : {
		'Nama' : 'Charlie',
		'Usia' : 21,
		'Nilai' : {
			'matematika' : 95,
			'sains' : 90,
			'bahasa_inggris' : 92
		}
	}
}

for i in nilai_murid:
	murid = (nilai_murid[i]['Nama'])
	print(murid)

nilai_murid2 = (nilai_murid['murid2']['Nilai']['matematika'])
print(f'Nilai matematika = {nilai_murid2}')

nilai_murid3 = (nilai_murid['murid3']['Nama'])
print(f"Nama murid3 = {nilai_murid3}")

for i in nilai_murid:
	nilai = (nilai_murid[i]['Nilai']['matematika'])
	if nilai > 80:
		print(f"nilai matematika diatas 80: {nilai_murid[i]['Nama']}")

