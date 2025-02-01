yaz = input('FTB ye giriş yapın ad: ')
yaz1 = input('FTB ye giriş yapın şifre: ')

şifre = 'Ahmet123'
ad = 'ahmet'

if yaz == ad:
    if yaz1 == şifre:
        print('Başarılı, hoş geldiniz!')
        while True:  # Sonsuz döngü başlatıyoruz, kullanıcı çıkana kadar devam edecek
            x = input('Yazmak istediğiniz komutu girin: örn. ls veya get: ')
            if x == 'ls':
                print('password.txt')
            elif x == 'get':
                
                print('Dosya indirildi, cat ile okuyabilirsiniz.')
                break  # Dosya indirildikten sonra çıkış yapacak
            else:
                print('Geçersiz komut! Tekrar deneyin.')
    else:
        print('Yanlış şifre!')
else:
    print('Yanlış kullanıcı adı!')