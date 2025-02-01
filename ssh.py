# Kullanıcı adı ve şifre doğrulama işlemi
yaz = input('SSH giriş yapın, kullanıcı adı: ')
yaz1 = input('SSH giriş yapın, şifre: ')

# Doğru kullanıcı adı ve şifre
kullanici_adi = 'Ali'
sifre = 'Ali123'

# Kullanıcı adı kontrolü
if yaz == kullanici_adi:
    # Şifre kontrolü
    if yaz1 == sifre:
        print('Tebrikler, sistemi hackledin!')
    else:
        print('Yanlış şifre!')
else:
    print('Yanlış kullanıcı adı!')

