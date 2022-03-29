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

Docs:

*line 14      = # date & time with tag SPAN
*line 19 - 46 = # scrap data magnitude until dirasakan

* datascrap = datascrap.findChildren('li') # Output = List

*line 21 - 46 = #print List using FOR LOOP

*i = 0 # knowing sequence

*line after begin looping FOR # 
print(i, datalist) # print knowing list sequence

*if i == 1: # 1 is index list magnitude

*i = i + 1 # count from 0 to End data

"""



import LatestEarthquake

if __name__ == '__main__':
   print('==========MAIN APPS==========\n') 
   result = LatestEarthquake.DataExtraction()
   LatestEarthquake.ShowData(result)