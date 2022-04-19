from operator import indexOf


days = ['bir','iki', 'üç','dört','beş', 'altı', 'yedi', 'sekiz', 'dokuz','on','onbir','oniki','onüç','ondört','onbeş',
    'onaltı','onyedi','onsekiz','ondokuz','yirmi','yirmibir', 'yirmiki', 'yirmiüç', 'yirmidört','yirmibeş', 'yirmialtı',
    'yirmiyedi', 'yirmisekiz','yirmidokuz', 'otuz', 'otuzbir'    
    ]

months = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim',
'Kasım', 'Aralık']

years_binler = ['bin','ikibin', 'üçbin', 'dörtbin', 'beşbin', 'altıbin']
years_yüzler = ['yüz', 'ikiyüz', 'üçyüz', 'dörtyüz', 'beşyüz', 'altıyüz', 'yediyüz', 'sekizyüz', 'dokuzyüz']
years_onlar = ['on', 'yirmi', 'otuz', 'kırk', 'elli', 'altmış', 'yetmiş', 'seksen', 'doksan']

birthday_text = ''

birthday = input('Enter your birthday please(1/1/1973): ')
birthday_list = birthday.split('/')

try:
    for i in birthday_list:
        if indexOf(birthday_list, i) == 0:
            birthday_text += days[int(i) - 1].capitalize() + ' '
        if indexOf(birthday_list, i) == 1:
            birthday_text += months[int(i) - 1] + ' '
        if indexOf(birthday_list,i) == 2:
            birthday_text +=  years_binler[int(i[0]) - 1] + ' '
            birthday_text += years_yüzler[int(i[1]) - 1] + ' '
            birthday_text += years_onlar[int(i[2]) - 1] + ' '
            birthday_text += days[int(i[3]) - 1]
    print(birthday_text)
except:
    print('Enter a valid date please .....')

        
    

    




    