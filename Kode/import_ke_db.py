import pandas as pd
from sqlalchemy import create_engine
import os

# Mengatur koneksi ke database
username = 'root'  # Ganti dengan username MySQL Anda
password = ''  # Ganti dengan password MySQL Anda (biarkan kosong jika tidak ada)
database = 'produk_hp'
table_name = 'soc'
connection_string = f'mysql+mysqlconnector://{username}:{password}@localhost/{database}'
engine = create_engine(connection_string)

# Path ke folder Kode
kode_folder = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(kode_folder, 'soc.csv')

# Log: Membaca CSV
print(f"Membaca file CSV dari: {csv_path}")
data = pd.read_csv(csv_path)

# Log: Mengganti nama kolom
print("Mengganti nama kolom...")
data.columns = ['processor', 'rating', 'antutu_10']

# Log: Mengimpor data ke dalam tabel
print(f"Mengimpor data ke dalam tabel: {table_name}")
data.to_sql(table_name, con=engine, if_exists='replace', index=False)

print("Data berhasil diimpor ke dalam tabel:", table_name)
