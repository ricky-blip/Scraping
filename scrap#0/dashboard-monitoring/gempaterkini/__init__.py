from bs4 import BeautifulSoup
import requests

def ekstrasi_data():
    """
    Tanggal     : 2 Maret 2022 
    Waktu       : 08:52:08 WIB
    Magnitudo   : 3.2
    Kedalaman   : 8 km
    Koordinat   : 6.95 LS - 107.06 BT
    Pusat Gempa : Pusat gempa berada di darat 14 km tenggara Kota Sukabumi
    Dirasakan   : Dirasakan (Skala MMI): II Kebonpedes, II Cireunghas
    :return:
    """
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None
    
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        
        datetime = soup.find('span', {'class': 'waktu'}) # date & time with tag SPAN
        datetime = datetime.text.split(', ')
        date = datetime[0]
        time = datetime[1]
        
        # scrap data magnitude until dirasakan
        
        datascrap = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'}) 
        datascrap = datascrap.findChildren('li') # Output = List
        #print List using FOR LOOP
        
        i = 0 # knowing sequence
        magnitude = None
        kedalaman = None
        ls = None
        bt = None
        location  = None
        dirasakan = None
        
        for datalist in datascrap:
            # print(i, datalist) # print knowing list sequence
            if i == 1: # 1 is index list magnitude
                magnitude = datalist.text
            elif i == 2:
                kedalaman = datalist.text
            elif i == 3:
                coordinate = datalist.text.split(' - ')
                ls = coordinate[0]
                bt = coordinate[1]
            elif i == 4:
                location = datalist.text
            elif i == 5:
                dirasakan = datalist.text
                
            i = i + 1 # count from 0 to End data
        
        hasil = dict()
        hasil['tanggal']       = date
        hasil['waktu']         = time
        hasil['magnitudo']     = magnitude
        hasil['kedalaman']     = kedalaman
        hasil['koordinat']     = {'ls':ls, 'bt':bt}
        hasil['lokasi']        = location
        hasil['dirasakan']     = dirasakan
        
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print("Data Not Found")
        return
    
    print("Latest Earthquake based on BMKG")
    print(f"Tanggal    : {result['tanggal']}")
    print(f"Waktu      : {result['waktu']}")
    print(f"Magnitudo  : {result['magnitudo']}")
    print(f"Kedalaman  : {result['kedalaman']}")
    print(f"Koordinat  : LS = {result['koordinat']['ls']} | BT = {result['koordinat']['bt']}")
    print(f"Lokasi     : {result['lokasi']}")
    print(f"Dirasakan  : {result['dirasakan']}")
    
if __name__ == '__main__':
    print('Package Gempa Terkini')