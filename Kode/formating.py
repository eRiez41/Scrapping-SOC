import pandas as pd
import os

# Path ke folder Kode
kode_folder = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(kode_folder, 'soc.csv')

# Baca file CSV
df = pd.read_csv(csv_path)

# Fungsi untuk memformat nama prosesor
def format_processor_name(name):
    # Menghapus angka urutan di awal
    name_parts = name.split(' ', 1)[1]  # Ambil bagian setelah angka
    # Mencari brand dan menghapusnya dari nama
    for brand in ['Qualcomm', 'MediaTek', 'Apple', 'Google', 'HiSilicon', 'Unisoc', 'Samsung']:
        if brand in name:
            # Hapus brand dari nama
            formatted_name = name_parts.replace(brand, '').strip()  # Menghapus spasi ekstra
            print(f"Formatting: {name} -> {formatted_name}")  # Tambahkan log
            return formatted_name
    formatted_name = name_parts.strip()  # Kembalikan nama jika tidak ada brand yang cocok
    print(f"Formatting: {name} -> {formatted_name}")  # Tambahkan log
    return formatted_name

# Terapkan fungsi ke kolom Processor
df['Processor'] = df['Processor'].apply(format_processor_name)

# Simpan hasil ke file yang sama (mengupdate isinya)
df.to_csv(csv_path, index=False)

print(f"Proses selesai. Hasil disimpan di '{csv_path}'.")
