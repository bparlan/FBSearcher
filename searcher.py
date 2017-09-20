"""
FBSearcher

This program gets Facebook Group id's as list,
Key Terms as list, searches each key term within each group
and opens all results in separate windows.

2do: Warning should provided before flooding new browser tabs.

author: Baris Parlan
website: bparlan.com
last edited: September 2017
"""

import webbrowser

arabalar = ['307','C4','Golf']

gruplar = ['701784149839644','817517351675883','818667784849260',
            '1061873947223748','344080102421121','150110848525349',
            '448879365208324','1575389769372777','387552637953452','1037775422987359']
adet = len(arabalar) * len(gruplar)

#print('Toplam ' + str(adet) + 'adet pencere açılacak, emin misin?')
#print('E - Evet / H - Hayır')

for grup in gruplar:
    for araba in arabalar:
        url = 'https://www.facebook.com/groups/'+grup+'/for_sale_search/?forsalesearchtype=for_sale&availability=available&query='+araba
        webbrowser.open(url)