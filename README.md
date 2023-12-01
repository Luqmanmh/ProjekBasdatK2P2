<a name="readme-top"></a>
<h1 align="center">THITIPAN</h1>
<h2 align="center">Karena semua hanyalah titipan</h2>
<p align="center">Webapp pengelolaan daycare bagi pegawai<p>
<p align="center">Basis Data 2023 - P2 Kelompok 2</p>

<details>
  <summary>Anggota Kelompok</summary>
  <ul>
    <li>G6401221012 Luqman Mohammad Hakim</li>
    <li>G6401221017 Khansa Fitri Zhafirah</li>
    <li>G6401221067 Chairul Rifky Tirtacahyadi</li>
    <li>G6401221117 Yuuka Salsabila Sisvi</li>
  </ul>
</details>

## Tentang Projek
Webapp yang debuat untuk memudahkan pegawai Daycare untuk mengelola daycarenya. data yang dapat dikelola (CRUD) berisi data pegawai, data logistik (perlengkapan, mainan dan persediaan), data orangtua, dan data anak. Teknologi yang digunakan dalam membuat website ini adalah Django dan DB Browser for SQLite.

## Menjalankan Website
Berikut adalah hal-hal yang diperlukan beserta langkah-langkah agar dapat menjalankan website ini secara lokal.
### Prerequisite
- Python (minimal versi 3.8)  
  Download python <a href="https://www.python.org/downloads/">disini</a>  
  Cek di terminal apakah sudah terinstall dengan benar, ketik:
  ```sh
  python --version
  ```
- Django  
  Download Django, di terminal ketik:
  ```sh
  python -m pip install django==4.1.6
  ```
  Cek di terminal apakah sudah terinstall dengan benar, ketik:
  ```sh
  python -m pip show django
  ```
### Cara Menjalankan
1. Download repositori ini dan ekstrak
2. Buka terminal, pastikan alamat sudah masuk ke dalam folder yang sudah diekstrak
3. Dalam terminal, ketik:
   ```sh
   python manage.py runserver
   ```
4. Salin alamat yang muncul ke browser dan jalankan
   ```sh
   http://127.0.0.1:8000/
   ```
<p align="right">(<a href="#readme-top">Kembali ke atas</a>)</p>
