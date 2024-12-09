import subprocess
import os

# Daftar file yang akan dijalankan
scripts = [
    'ambil_soc.py',
    'formating.py',
    'import_ke_db.py'
]

# Path ke folder Kode
kode_folder = 'Kode'

# Menjalankan setiap skrip
for script in scripts:
    script_path = os.path.join(kode_folder, script)
    print(f"Menjalankan {script_path}...")
    result = subprocess.run(['python3', script_path], capture_output=True, text=True)

    # Menampilkan output dari skrip
    if result.stdout:
        print(f"Output dari {script}:")
        print(result.stdout)
    if result.stderr:
        print(f"Error dari {script}:")
        print(result.stderr)

print("Semua skrip berhasil dijalankan.")
