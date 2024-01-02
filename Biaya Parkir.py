import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from datetime import datetime

def hitung_biaya_parkir(jam_masuk, jam_keluar, tarif_perjam=3000):
    try:
        jam_masuk = datetime.strptime(jam_masuk, "%Y-%m-%d-%H:%M")
        jam_keluar = datetime.strptime(jam_keluar, "%Y-%m-%d-%H:%M")
        
        total_jam = (jam_keluar - jam_masuk).total_seconds() / 3600
        
        if total_jam <= 0:
            return "Waktu keluar harus lebih besar dari waktu masuk."

        biaya = tarif_perjam * total_jam
        return f"Biaya Parkir: {biaya} Rupiah"
    except ValueError:
        return "Format waktu tidak valid."

def hitung_biaya_parkir_tkinter():
    jam_masuk = entry_masuk.get()
    jam_keluar = entry_keluar.get()

    hasil = hitung_biaya_parkir(jam_masuk, jam_keluar)
    label_hasil.config(text=hasil)

# Membuat aplikasi Tkinter
root = tk.Tk()
root.title("Hitung Biaya Parkir")

style = Style('cyborg')  # Pilih tema 'cyborg'

# Judul Aplikasi
label_judul = ttk.Label(root, text="Aplikasi Penghitung Biaya Parkir", font=('Helvetica', 14, 'bold'), foreground='white')
label_judul.grid(row=0, column=0, columnspan=2, pady=(10, 20))

# Membuat dan menempatkan entri untuk waktu masuk
label_masuk = ttk.Label(root, text="Masuk Parkir: ")
label_masuk.grid(row=1, column=0, sticky="E", padx=10, pady=5)
entry_masuk = ttk.Entry(root)
entry_masuk.grid(row=1, column=1, padx=10, pady=5)
entry_masuk.insert(0, "2023-01-01-10:00")  # Nilai awal untuk waktu masuk

# Membuat dan menempatkan entri untuk waktu keluar
label_keluar = ttk.Label(root, text="Keluar Parkir:")
label_keluar.grid(row=2, column=0, sticky="E", padx=10, pady=5)
entry_keluar = ttk.Entry(root)
entry_keluar.grid(row=2, column=1, padx=10, pady=5)
entry_keluar.insert(0, "2023-01-01-11:00")  # Nilai awal untuk waktu keluar

# Membuat tombol untuk menghitung biaya parkir
button_hitung = ttk.Button(root, text="Biaya Parkir", command=hitung_biaya_parkir_tkinter, style="success-outline")
button_hitung.grid(row=3, column=0, columnspan=2, pady=10)

# Membuat label untuk menampilkan hasil
label_hasil = ttk.Label(root, text="")
label_hasil.grid(row=4, column=0, columnspan=2)

# Menyusun elemen-elemen dalam grid agar tetap di tengah
for i in range(10):
    root.grid_rowconfigure(i, weight=10)
    root.grid_columnconfigure(i, weight=10)

# Menjalankan loop utama Tkinter
root.mainloop()
