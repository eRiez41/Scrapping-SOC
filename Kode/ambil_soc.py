import requests
from bs4 import BeautifulSoup
import csv
import os

# Ganti dengan URL halaman yang ingin di-scrape
url = 'https://nanoreview.net/en/soc-list/rating'

# Mengirimkan permintaan GET
response = requests.get(url)

# Memastikan permintaan berhasil
if response.status_code == 200:
    # Membuat objek BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Mencari tabel dengan class 'table-list sortable'
    table = soup.find('table', class_='table-list sortable')

    # Menyimpan data yang diinginkan
    soc_data = []

    # Mengambil semua baris dari tabel
    rows = table.find_all('tr')[1:]  # Lewati baris header
    for row in rows:
        columns = row.find_all('td')  # Temukan elemen <td> dalam baris
        if columns:  # Pastikan ada kolom dalam baris
            # Gabungkan nama prosesor dan manufacturer serta nomor
            manufacturer = columns[0].text.strip().replace('\n', ' ')
            processor_name = columns[1].text.strip().replace('\n', ' ')
            processor_full_name = f"{manufacturer} {processor_name}".strip()

            # Pisahkan rating dan skor AnTuTu
            rating = columns[2].text.strip().replace('\n', ' ')
            antutu_score = columns[3].text.strip().replace('\n', ' ')

            # Tampilkan log data yang sedang diambil
            print(f"Mengambil data: {processor_full_name}, Rating: {rating}, AnTuTu Score: {antutu_score}")

            # Simpan dalam tuple
            soc_data.append((processor_full_name, rating, antutu_score))

    # Path ke folder Kode
    kode_folder = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(kode_folder, 'soc.csv')

    # Menyimpan data ke dalam file CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # Menulis header
        csv_writer.writerow(['Processor', 'Rating', 'AnTuTu Score'])
        # Menulis data
        for processor_name, rating, antutu_score in soc_data:
            # Menyimpan data dengan format sesuai keinginan
            csv_writer.writerow([processor_name, rating, antutu_score])

    print(f"Data berhasil disimpan ke {csv_path}.")
else:
    print(f'Gagal mengambil data: {response.status_code}')
