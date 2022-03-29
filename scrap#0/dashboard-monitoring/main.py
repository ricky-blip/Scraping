"""
Detect Latest Earthquake from database BMKG
1. Modularisasi dengan Function
    - membuat name = main
    - membuat ekstraksi data dengan function
    - membuat tampilkan data dengan function
    - ekstraksi manual data dengan COPAS dari website nya ke dalam function ekstraksi data
    - lalu cetak di function tampilkan data
2. Modularisasi dengan Package
    - membuat package/folder untuk menyimpan function yang sebelumnya dibuat di module
    - buat file __init__.py lalu masukkan function
    - kembali ke module utama lalu import package yang telah dibuat 
"""

import gempaterkini

if __name__ == '__main__':
   print('==========MAIN APPS==========\n') 
   result = gempaterkini.ekstrasi_data()
   gempaterkini.tampilkan_data(result)