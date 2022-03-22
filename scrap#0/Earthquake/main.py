"""
Detect Latest Earthquake from database BMKG
1. Modularisasi dengan Function
    - membuat name = main
    - membuat ekstraksi data dengan function
    - membuat tampilkan data dengan function
    - ekstraksi manual data dengan COPAS dari website nya ke dalam function ekstraksi data
    - lalu cetak di function tampilkan data


"""

def ekstrasi_data():
    """
    Tanggal     : 2 Maret 2022 
    Waktu       : 08:52:08 WIB
    Magnitudo   : 3.2
    Kedalaman   : 8 km
    Lokasi      : 6.95 LS - 107.06 BT
    Pusat Gempa : Pusat gempa berada di darat 14 km tenggara Kota Sukabumi
    Dirasakan   : Dirasakan (Skala MMI): II Kebonpedes, II Cireunghas
    :return:
    """
    hasil = dict()
    hasil['tanggal']       = '2 Maret 2022'
    hasil['waktu']         = '08:52:08 WIB' 
    hasil['magnitudo']     = 3.2
    hasil['kedalaman']     = '8 km' 
    hasil['lokasi']        = {'ls': 6.95, 'bt': 107.06}
    hasil['pusat_gempa']   = 'Pusat gempa berada di darat 14 km tenggara Kota Sukabumi' 
    hasil['dirasakan']     = 'Dirasakan (Skala MMI): II Kebonpedes, II Cireunghas' 
    
    return hasil


def tampilkan_data(result):
    print("Latest Earthquake based on BMKG")
    print(f"Tanggal    : {result['tanggal']}")
    print(f"Waktu      : {result['waktu']}")
    print(f"Magnitudo  : {result['magnitudo']}")
    print(f"Kedalaman  : {result['kedalaman']}")
    print(f"Lokasi     : LS = {result['lokasi']['ls']} | BT = {result['lokasi']['bt']}")
    print(f"Pusat Gempa: {result['pusat_gempa']}")
    print(f"Dirasakan  : {result['dirasakan']}")

if __name__ == '__main__':
   print('==========MAIN APPS==========\n') 
   result = ekstrasi_data()
   tampilkan_data(result)